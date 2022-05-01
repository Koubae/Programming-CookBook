#  Note taken from --> https://gist.github.com/JungeAlexander/6ce0a5213f3af56d7369 & https://stackoverflow.com/questions/714063/importing-modules-from-parent-folder/11158224#11158224
import os, sys, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import warnings
import re
import csv
import mimetypes
import time
from math import ceil

from werkzeug.utils import secure_filename
from flask import (current_app, request, redirect, flash, abort, json, 
                    Response, get_flashed_messages, stream_with_context)
from jinja2 import contextfunction
from wtforms.fields import HiddenField
from wtforms.fields.core import UnboundField
from wtforms.validators import ValidationError, InputRequired

try: 
    import tablib
except ImportError:
    tablib: None

from base import BaseView, expose
from flask_admin_.form import BaseForm, FormOpts, rules
from flask_admin_.model import filters, typefmt, template
from actions import ActionsMixin
from helpers import (get_form_data, validate_form_on_submit, get_redirect_target, flash_errors)
from tools import rec_getattr
from _backwards import ObsoleteAttr
from _compat import (iteritems, itervalues, OrderedDict, as_unicode, csv_encode, text_type)
from flask_admin_.model.helpers import prettify_name, get_mdict_item_or_list
from flask_admin_.model.ajax import AjaxModelLoader


# Used to generate filter query string name
filter_char_re = re.compile('[^a-z0-9 ]')
filter_compact_re = re.compile(' +')


class Viewargs(object):

    def __init__(self, page=None, page_size=None, sort=None, sort_desc=None, 
                search=None, filters=None, extra_args=None):
        self.page = page
        self.page_size = page_size
        self.sort = sort
        self.sort_desc = bool(sort_desc)
        self.search = search
        self.filters = filters
        
        if not self.search:
            self.search = None
        self.extra_args = extra_args or dict()
    
    def clone(self, **kwargs):
        if self.filters:
            flt = list(self.filters)
        else:
            flt = None
        
        kwargs.setdefault('page', self.page)
        kwargs.setdefault('page_size', self.page_size)
        kwargs.setdefault('sort', self.sort)
        kwargs.setdefault('sort_desc', self.sort_desc)
        kwargs.setdefault('search', self.search)
        kwargs.setdefault('filters', flt)
        kwargs.setdefault('extra_args', dict(self.extra_args))

        return ViewArgs(**kwargs)


class FilterGroup(object):

    def __init__(self, label):
        self.label = label
        self.filters = []
    
    def append(self, filter):
        self.filters.append(filter)
    
    def non_lazy(self):
        filters = []

        for item in self.filters:
            copy = dict(item)
            copy['operation'] = as_unicode(copy['operation'])
            options = copy['options']
            if options:
                copy['options'] =[(k, text_type(v)) for k,v in options]
            filters.append(copy)
        return as_unicode(self.label), filters

    def __iter__(self):
        return iter(self.filters)


class BaseModelView(BaseView, ActionsMixin):

    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = False
    can_export = False
    # ----------------------------------------------
    list_template = 'admin/model/list.html'
    edit_template = 'admin/model/eidt.html'
    create_template='admin/model/create.html'
    detailts_template = 'admin/model/detailts.html'
    edit_modal_template ='admin/model/edit.html'
    create_modal_template = 'admin/model/modals/create.html'
    details_modal_template = 'admin/model/modals/details.html'
    # ----------------------------------------------
    edit_modal = False
    create_modal = False
    details_modal = False
    # ----------------------------------------------
    column_list = ObsoleteAttr('column_list', 'list_columns', None)
    column_exclude_list = ObsoleteAttr('column_exclude_list', 'excluded_list_columns', None)
    column_details_list = None
    column_details_exclude_list = None
    column_export_list = None
    column_export_exclude_list = None
    column_formatters = ObsoleteAttr('column_formatters', 'list_formatters', dict())
    column_formatters_export = None    
    column_formatters_detail = None
    column_type_formatters = ObsoleteAttr('column_type_formatters', 'list_type_formatters', None)
    column_type_formatters_export = None
    column_type_formatters_detail = None
    column_labels = ObsoleteAttr('column_labels', 'rename_columns', None)
    column_descriptions = None
    column_sortable_list = ObsoleteAttr('column_sortable_list', 'sortable_columns', None)
    column_default_sort = None
    column_searchable_list = ObsoleteAttr('column_searchable_list', 'searchable_columns', None)
    column_editable_list = None
    column_choices = None
    column_filters = None
    named_filter_urls = False
    column_display_pk = ObsoleteAttr('column_display_pk', 'list_display_pk', False)
    column_display_actions = True
    column_extra_row_actions = None
    simple_list_pager = False
    form = None
    form_base_class = BaseForm
    form_args = None
    form_columns = None
    form_excluded_columns = ObsoleteAttr('form_excluded_columns', 'excluded_form_columns', None)
    form_overrides = None
    form_widget_args = None
    form_extra_fields = None
    form_ajax_refs = None
    form_rules = None
    form_edit_rules = None
    form_create_rules = None
    action_disallowed_list = ObsoleteAttr('action_disallowed_list', 'disallowed_actions', [])
    export_max_rows = 0
    export_types = ['csv']
    page_size = 20
    can_set_page_size = False
    def __init__(self, model,
                name=None, category=None, endpoint=None, url=None, static_folder=None,
                menu_class_name=None, menu_icon_type=None, menu_icon_value=None):
        self.model = model
        if name is None:
            name = '%s' % self._prettify_class_name(model.__name__)
        super(BaseModelView, self).__init__(name, category, endpoint, url, static_folder,
                                            menu_class_name=menu_class_name,
                                            menu_icon_type=menu_icon_type,
                                            menu_icon_value=menu_icon_value)
        self.init_actions()
        self._refresh_cache()
    
    def _get_endpoint(self, endpoint):
        if endpoint:
            return super(BaseModelView, self),_get_endpoint(endpoint)
        return self.model.__name__.lower()
    
    def _refresh_forms_cache(self):
        self._form_ajax_refs = self._process_ajax_references()

        if self.form_widget_args is None:
            self.form_widget_args = {}
        self._create_form_class = self.get_create_form()
        self._edit_form_class = self.get_edit_form()
        self._delete_form_class = self.get_delete_form()
        self._action_form_class = self.get_action_form()

        if self.column_editable_list:
            self._list_form_class = self.get_list_form()
        else:
            self.column_editable_list = {}
    
    def _refresh_filters_cache(self):

        self._filters = self.get_filters()

        if self._filters:
            self._filter_groups = OrderedDict()
            self._filter_args = {}

            for i, flt in enumerate(self._filters):
                key = as_unicode(flt.name)
                if key not in self._filter_groups:
                    self._filter_group[key] = FilterGroup(flt.name)
                self._filter_groups[key].append({
                    'index': 1,
                    'arg': self.get_filter_arg(i, flt),
                    'operation': flt.operation(),
                    'options': flt.get_options(self) or None,
                    'type': flt.data_type
                })

                self._filter_args[self.get_filter_arg(i, flt)] = (i, flt)
        else:
            self._filter_groups = None
            self._filter_args = None
    
    def _refresh_form_rules_cache(self):

        if self.form_create_rules:
            self._form_create_rules = rules.RuleSet(self, self.form_create_rules)
        else:
            self._form_create_rules = None
        
        if self.form_edit_rules:
            self._form_edit_rules = rules.RuleSet(self, self.form_edit_rules)
        else:
            self._form_edit_rules = None
        
        if self.form_rules:
            form_rules = rules.RuleSet(self, self.form_rules)

            if not self._form_create_rules:
                self._form_create_rules = form_rules
            
            if not self._form_edit_rules:
                self._form_edit_rules = form_rules
    
    def _refresh_cache(self):
        """
            Refresh various cached variables.
        """
        # List view
        self._list_columns = self.get_list_columns()
        self._sortable_columns = self.get_sortable_columns()

        # Details view
        if self.can_view_details:
            self._details_columns = self.get_details_columns()

        # Export view
        self._export_columns = self.get_export_columns()

        # Labels
        if self.column_labels is None:
            self.column_labels = {}

        # Forms
        self._refresh_forms_cache()

        # Search
        self._search_supported = self.init_search()

        # Choices
        if self.column_choices:
            self._column_choices_map = dict([
                (column, dict(choices))
                for column, choices in self.column_choices.items()
            ])
        else:
            self.column_choices = self._column_choices_map = dict()

        # Column formatters
        if self.column_formatters_export is None:
            self.column_formatters_export = self.column_formatters

        if self.column_formatters_detail is None:
            self.column_formatters_detail = self.column_formatters

        # Type formatters
        if self.column_type_formatters is None:
            self.column_type_formatters = dict(typefmt.BASE_FORMATTERS)

        if self.column_type_formatters_export is None:
            self.column_type_formatters_export = dict(typefmt.EXPORT_FORMATTERS)

        if self.column_type_formatters_detail is None:
            self.column_type_formatters_detail = dict(typefmt.DETAIL_FORMATTERS)

        if self.column_descriptions is None:
            self.column_descriptions = dict()

        # Filters
        self._refresh_filters_cache()

        # Form rendering rules
        self._refresh_form_rules_cache()

        # Process form rules
        self._validate_form_class(self._form_edit_rules, self._edit_form_class)
        self._validate_form_class(self._form_create_rules, self._create_form_class)

    def get_pk_value(self, model):
        raise NotImplementedError()
    
    def scaffold_list_column(self):
        raise NotImplementedError('Please implement scaffold_list_columns method')

    def get_column_name(self, field):

        if self.column_labels and field in self.column_labels:
            return self.column_labels[field]
        else:
            return self._prettify_name(field)
    
    def get_list_row_actions(self):

        actions = []
        if self.can_view_details:
            if self.details_modal:
                actions.append(template.ViewPopupRowAction())
            else:
                actions.append(template.ViewRowAction())

        if self.can_edit:
            if self.edit_modal:
                actions.append(template.EditPopupRowAction())
            else:
                actions.append(template.EditRowAction())

        if self.can_delete:
            actions.append(template.DeleteRowAction())

        return actions + (self.column_extra_row_actions or [])
    
    def get_column_names(self, only_columns, excluded_columns):

        if excluded_columns:
            only_columns = [c for c in only_columns if c not in excluded_columns]
        return [(c, self.get_column_name(c)) for c in only_columns]
    
    def get_list_columns(self):

        return self.get_column_names(
            only_columns=self.column_list or self.scaffold_list_columns(),
            excluded_columns=self.column_exclude_list,
        )

    def get_details_columns(self):

        try:
            only_columns = self.column_details_list or self.scaffold_list_columns()
        except NotImplementedError:
            raise Exception('Please define column_details_list')

        return self.get_column_names(
            only_columns=only_columns,
            excluded_columns=self.column_details_exclude_list,
        )
    def get_export_columns(self):
        only_columns = (self.column_export_list or self.column_list or
                        self.scaffold_list_columns())

        return self.get_column_names(
            only_columns=only_columns,
            excluded_columns=self.column_export_exclude_list,
        )

    def scaffold_sortable_columns(self):

        raise NotImplementedError('Please implement scaffold_sortable_columns method')
    
    def get_sortable_columns(self):
    
        if self.column_sortable_list is None:
            return self.scaffold_sortable_columns() or dict()
        else:
            result = dict()

            for c in self.column_sortable_list:
                if isinstance(c, tuple):
                    result[c[0]] = c[1]
                else:
                    result[c] = c

            return result
    
    def init_search(self):
        return False
    
    def search_placeholder(self):
        return None
    
    def scaffold_filters(self, name):
        return None
    
    def is_valid_filter(self, filter):
        return isinstance(filter, filters.BaseFilter)
    
    def handle_filter(self, filter):
        return filter
    
    def get_filters(self):

        if self.column_filters:
            collection = []

            for n in self.column_filters:
                if self.is_valid_filter(n):
                    collection.append(self.handle_filter(n))
                else:
                    flt = self.scaffold_filters(n)
                    if flt:
                        collection.extend(flt)
                    else:
                        raise Exception('Unsupported filter type %s' % n)
            return collection
        else:
            return None
    
    def get_filter_arg(self, index, flt):

        if self.named_filter_urls:
            operation = flt.operation()

            try:
                operation = operation._args[0]
            except AttributeError:
                pass
            name = ('%s %s' % (flt.name, as_unicode(operation))).lower()
            name = filter_char_re.sub('', name)
            name = filter_compact_re.sub('_', name)
            return name
        else:
            return str(index)
    
    def _get_filter_groups(self):

        if self._filter_groups:
            results = OrderedDict()

            for group in itervalues(self._filter_groups):
                key, items = group.non_lazy()
                result[key] = items
            return results
        return None
    
    def scaffold_form(self):
        raise NotImplementedError('Please implement scaffold_form method')
    
    def scaffold_list_form(self, widget=None, validators=None):
        raise NotImplementedError('Please implement scaffold_list_form method')

    def get_form(self):

        if self.form is not None:
            return self.form

        return self.scaffold_form()
    def get_list_form(self):

        if self.form_args:
            # get only validators, other form_args can break FieldList wrapper
            validators = dict(
                (key, {'validators': value["validators"]})
                for key, value in iteritems(self.form_args)
                if value.get("validators")
            )
        else:
            validators = None

        return self.scaffold_list_form(validators=validators)
    def get_create_form(self):
        return self.get_form()

    def get_edit_form(self):
        return self.get_form()

    def get_delete_form(self):

        class DeleteForm(self.form_base_class):
            id = HiddenField(validators=[InputRequired()])
            url = HiddenField()

        return DeleteForm

    def get_action_form(self):
        
        class ActionForm(self.form_base_class):
            action = HiddenField()
            url = HiddenField()
            # rowid is retrieved using getlist, for backward compatibility

        return ActionForm

    def create_form(self, obj=None):
        return self._create_form_class(get_form_data(), obj=obj)

    def edit_form(self, obj=None):
        return self._edit_form_class(get_form_data(), obj=obj)

    def delete_form(self):

        if request.form:
            return self._delete_form_class(request.form)
        elif request.args:
            # allow request.args for backward compatibility
            return self._delete_form_class(request.args)
        else:
            return self._delete_form_class()

    def list_form(self, obj=None):
        return self._list_form_class(get_form_data(), obj=obj)

    def action_form(self, obj=None):
        return self._action_form_class(get_form_data(), obj=obj)

    def validate_form(self, form):
        return validate_form_on_submit(form)

    def get_save_return_url(self, model, is_created=False):
        return get_redirect_target() or self.get_url('.index_view')
    
    def _get_ruleset_missing_fields(self, ruleset, form):
        
        missing_fields = []
        
        if ruleset:
            visible_fields = ruleset.visible_fields
            for field in form:
                if field.name not in visible_fields:
                    missing_fields.append(field.name)
        return missing_fields
    
    def _show_missing_fields_warning(self, text):
        warnings.warn(text)
    
    def _validate_form_class(self, ruleset, form_class, remove_missing=True):

        form_fields = []

        for name, obj in iteritems(form_class.__dict__):
            if isinstance(obj, UnboundField):
                form_fields.append(name)
        
        missing_fields = []
        if ruleser:
            visible_fields = ruleset.visible_fields
            for field_name in form_fields:
                if field_name not in visible_fields:
                    missing_fields.append(field_name)
        
        if missing_fields:
            self._show_missing_fields_warning('Fields missing from ruleset: %s' % (','.join(missing_fields)))
        if remove_missing:
            self._remove_fields_from_form_class(missin, form_class)

    def _validate_form_instance(self, ruleset, form, remove_missing=True):

        missing_fields = self._get_ruleset_missing_fields(ruleset=ruleset, form=form)
        if missing_fields:
            self._show_missing_fields_warning('Fields missing from ruleset: %s' % (','.join(missing_fields)))
        if remove_missing:
            self._remove_fields_from_form_instance(missing_fields, form)
    
    def _remove_fields_from_form_instance(self, field_names, form):

        for field_name in field_names:
            form.__delitem__(field_name)
    
    def _remove_fields_from_form_class(self, field_names, form_class):

        for field_name in field_names:
            delattr(form_class, field_name)
    
    # ------------------------------------------------------------------------------

    def is_sortable(self, name):
        return name.lower() in (x.lower() for x in self._sortable_columns)
    
    def is_editable(self, name):
        return name in self.column_editable_list
    
    def _get_column_by_idx(self, idx):

        if idx is None or idx < 0 or idx >= len(self._list_columns):
            return None
        return self._list(columns[idx])
    
    def _get_default_order(self):

        if self.column_default_sort:

            if self.column_default_sort:
                if isinstance(self.column_default_sort, list):
                    return self.column_default_sort
                if isinstance(self.column_default_sort, tuple):
                    return [self.column_default_sort]
                else:
                    return [(self.column_default_sort, False)]
            return None
    
    # ---------------------------------------------------------------
    # Database-related API

    def get_list(self, page, sort_field, sort_desc, search, filters, 
                page_size=None):
        raise NotImplementedError('Please implement get_list method')

    def get_one(self, id):
        raise NotImplementedError('Please implement get_one method')

    # ---------------------------------------------------------------
    # Exception handler

    def handle_view_exception(self, exc):

        if isinstance(exc, ValidationError):
            flash(as_unicode(exc), 'error')
            return True
        if current_app.config.get('ADMIN_RAISE_ON_VIEW_EXCEPTION'):
            raise
        if self._debug:
            raise

        return False

    def on_model_change(self, form, model, is_created):
        pass

    def _on_model_change(self, form, model, is_created):

        try:
            self.on_modeL_change(form, model, is_created)
        except TypeError as e:
            if re.match(r'on_model_change\(\) takes .* 3 .* arguments .* 4 .* given .*', str(e)):
                msg = ('%s.on_model_change() now accepts third ' +
                    'parameter is_created. Please update your code') % self.model
                warnings.warn(msg)

                self.on_model_change(form, model)
            else:
                raise
    def after_model_change(self, form, model, is_created):
        pass

    def on_model_delete(self, model):
        pass

    def after_model_delete(self, model):
        pass

    def on_form_prefill(self, form, id):
        pass

    def create_model(self, form):
        raise NotImplementedError()

    def update_model(self, form, model):
        raise NotImplementedError()

    def delete_model(self, model):
        raise NotImplementedError()

    # Various helpers
    def _prettify_name(self, name):
        return prettify_name(name)

    def get_empty_list_message(self):
        return gettext('There are no items in the table.')

    def get_invalid_value_msg(self, value, filter):
        return gettext('Invalid Filter Value: %(value)s', value=value)
    
    # ------------------------------------------------------------------------------------------
    # URL generation helpers

    def _get_list_filter_args(self):

        if self._filters:
            filter = []

            for arg in request.args:
                if not arg.strartswith('flt'):
                    continue

                if '_' not in arg:
                    continue

                pos, key = arg[3:].split('_', 1)

                if key in self._filter_args:
                    idx, flt = self._filter_args[key]

                    value = request.args[arg]

                    if flt.validate(value):
                        data = (pos, (idx, as_unicode(flt.name), value))
                        filters.append(data)
                    else:
                        flash(self.get_invalid_value_msg(value, flt), 'error')
            return [v[1] for v in sorted(filters, key=lambda n: n[0])]
        return None
    
    def _get_list_extra_args(self):
        return ViewArgs(page=request.args.get('page', 0, type=int),
                        page_size=request.args.get('page_size', 0, type=int),
                        sort=request.args.get('sort', None, type=int),
                        sort_desc=request.args.get('desc', None, type=int),
                        search=request.args.get('search', None),
                        filters=self._get_list_filter_args(),
                        extra_args=dict([
                            (k, v) for k, v in request.args.items()
                            if k not in ('page', 'page_size', 'sort', 'desc', 'search', ) and
                            not k.startswith('flt')
                        ]))

    def _get_filters(self, filters):

        kwargs = {}

        if filters:
            for i, pair in enumerate(filters):
                idx, flt_name, value = pair

                key = 'flt%d_%s' % (i, self.get_filter_arg(idx, self._filters[idx]))
                kwargs[key] = value

        return kwargs
    
    def _get_list_url(self, view_args):

        page = view_args.page or None
        desc = 1 if view_args.sort_desc else None

        kwargs = dict(page=page, sort=view_args.sort, desc=desc, search=view_args.search)
        kwargs.update(view_args.extra_args)

        if view_args.page_size:
            kwargs['page_size'] = view_args.page_size
        
        kwargs.update(self._get_filters(view_args.filters))
        return self.get_url('index_view', **kwargs)
    
    def is_action_allowed(self, name):
        return name not in self.action_disallowed_list

    def _get_field_value(self, model, name):
        return rec_getattr(model, name)
    
    def _get_list_value(self, context, model, name, column_formatters,
                        column_type_formatters):
        column_fmt = column_formatters.get(name)
        if column_fmt is not None:
            value = column_fmt(self, context, model, name)
        else:
            value = self._get_field_value(model, name)

        choices_map = self._column_choices_map.get(name, {})
        if choices_map:
            return choices_map.get(value) or value
        
        type_fmt = None
        for typeobj, formatter in column_type_formatters.items():
            if isinstance(value, typeobj):
                type_fmt = formatter
                break
        if type_fmt is not None:
            value = type_fmt(self, value)
        return value
    
    @contextfunction
    def get_list_value(self, context, model, name):

        return self._get_list_value(
            context,
            model,
            name,
            self.column_formattes,
            self.column_type_formatters,
        )
    
    @contextfunction
    def get_detail_value(self, context, model, name):

        return self._get_list_value(
            context, 
            model,
            name, 
            self.column_formatters_detail,
            self.column_type_fomrattes_details,
        )
    
    def get_export_value(self, model, name):
    
        return self._get_list_value(
            None,
            model,
            name,
            self.column_formatters_export,
            self.column_type_formatters_export,
        )

    def get_export_name(self, export_type='csv'):
    
        filename = '%s_%s.%s' % (self.name,
                                time.strftime("%Y-%m-%d_%H-%M-%S"),
                                export_type)
        return filename
    
    def _process_ajax_references(self):

        result = {}

        if self.form_ajax_refs:
            for name, options in iteritems(self.form_ajax_refs):
                if isinstance(options, dict):
                    result[name] = self._create_ajax_loader(name, options)
                elif isinstance(options, AjaxModelLoader):
                    result[name] = options
                else:
                    raise ValueError('%s.form_ajax_refs can not handle %s types' % (self, type(options)))
        return result
    
    def _create_ajax_loader(self, name, options):
        raise NotImplementedError()

    #-------------------------------------------------------------------------------------------------------
    ###############
    #---<VIEWS>---#
    ###############

    @expose('/')
    def index_view(self):

        if self.can_delete:
            delete_form = self.delete_form()
        else:
            delete_form = None
        
        view_args = self._get_list_extra_args()

        # Map column Index
        sort_column = self._get_column_by_idx(view_args.sort)
        if sort_column is not None:
            sort_column = sort_column[0]
        
        page_size = view_args.page_size or self.page_size

        count, data = self.get_list(view_args.page, sort_column, view_args.sort_desc,
                                    view_args.search, view_args.filters, page_size=page_size)

        list_forms = {}
        if self.column_editable_list:
            for row in data:
                list_forms[self.get_pk_value(row)] = self.list_form(obj=row)

        # Calcukate n pages
        if count is not None and page_size:
            num_pages = int(ceil(count / float(page_size)))
        elif not page_size:
            num_pages = 0
        else:
            num_pages

        # URL gen helpers
        def pager_url(p):
            if p == 0:
                p = None
            return self._get_list_url(view_args.clone(page=p))

        def sort_url(column, invert=False, desc=None):
            if not desc and invert and not view_args.sort_desc:
                desc = 1
            return self._get_list_url(view_args.clone(sort=column, sort_desc=desc))

        def page_size_url(s):
            if not s:
                s= self.page_size
            return self._get_list_url(view_args.clone(page_size=s))

        actions, actions_confirmation = self.get_action_list()
        if acionts:
            action_form = self.action_form()    
        else:
            action_form = None
        
        clear_search_url = self._get_list_url(view_args.clone(page=0,
                                                            sort=view_args.sort,
                                                            sort_desc=view_args.sort_desc,
                                                            search=None,
                                                            filters=None))
        return self.render(
            self.list_template,
            data=data,
            list_forms=list_forms,
            delete_form=delete_form,
            action_form=action_form,

            # List
            list_columns=self._list_columns,
            sortable_columns=self._sortable_columns,
            editable_columns=self.column_editable_list,
            list_row_actions=self.get_list_row_actions(),

            # Pagination
            count=count,
            pager_url=pager_url,
            num_pages=num_pages,
            can_set_page_size=self.can_set_page_size,
            page_size_url=page_size_url,
            page=view_args.page,
            page_size=page_size,
            default_page_size=self.page_size,

            # Sorting
            sort_column=view_args.sort,
            sort_desc=view_args.sort_desc,
            sort_url=sort_url,

            # Search
            search_supported=self._search_supported,
            clear_search_url=clear_search_url,
            search=view_args.search,
            search_placeholder=self.search_placeholder(),

            # Filters
            filters=self._filters,
            filter_groups=self._get_filter_groups(),
            active_filters=view_args.filters,
            filter_args=self._get_filters(view_args.filters),

            # Actions
            actions=actions,
            actions_confirmation=actions_confirmation,

            # Misc
            enumerate=enumerate,
            get_pk_value=self.get_pk_value,
            get_value=self.get_list_value,
            return_url=self._get_list_url(view_args),

            # Extras
            extra_args=view_args.extra_args,
        )

        @expose('/new/', methods=('GET', 'POST'))
        def create_view(self):

            return_url = get_redirect_target() or self.get_url('.index_view')

            if not self.can_create:
                return redirect(returl_url)
            
            form = self.create_form()
            if not hasattr(form, '_validated_ruleset') or not form._validate_ruleset:
                self._validate_form_instance(ruleset=self._form_create_rules, form=form)
            
            if self.validate_form(form):

                model = self.create_model(form)
                if model:
                    flash('Record was successfully created.', 'success')
                    if '_add_another' in request.form:
                        return redirect(request.url)
                    elif '_continue_editing' in request.form:
                        if model is not True:
                            url = self.get_url('.edit_view', id=self.get_pk_value(mode), url=return_url)
                        else:
                            url = returl_url
                        return redirect(url)
                    else:
                        # Save Btn
                        return redirect(self.get_save_return_url(mode, is_created=True))
            form_opts = FormOpts(widget_args=self.form_widget_args,
                                form_rules=self._form_create_rules())
            
            if self.create_modal and request.args.get('modal'):
                template = self.create_modal_template
            else:
                template = self.create_template
            
            return self.render(template,
                                form=form,
                                form_opts=form_opts,
                                return_url=return_url)
        
        @expose('/edit/', methods=('GET', 'POST'))
        def edit_view(self):

            return_url = get_redirect_target() or self.get_url('.index_view')

            if not self.can_edit:
                return redirect(return_url)
            
            id = get_mdict_item_or_list(request.args, 'id')
            if id is None:
                return redirect(return_url)
            
            model = self.get_one(id)

            if model is None:
                flash('Record does not exists.', 'error')
                return redirect(return_url)
            
            form = self.edit_form(obj=model)

            if not hasattr(form, '_validated_ruleset') or not form._validated_ruleset:
                self._validate_form_instance(ruleset=self._form_edit_rules, form=form)
            
            if self.validate_form(form):
                if self.update_model(form, model):
                    flash('Recod was successfully saved.', 'success')
                    if '_add_another' in request.form:
                        return redirect(self.get_url('.create_view', url=return_url))
                    elif '_continue_editing' in request.form:
                        return redirect(request.url)
                    else:
                        # Save BTN
                        return redirect(self.get_save_return_url(mode, is_created=False))
            
            if request.method == 'GET' or form.errors:
                self.on_form_prefill(form, id)
            
            form_opts = FormOpts(widget_args=self.form_widget_args,
                                form_rules=self._form_edit_rules)
            
            if self.edit_modal and request.args.get('modal'):
                template = self.edit_modal_template
            else:
                template = self.edit_template
            
            return self.render(template,
                                model=model,
                                form=form,
                                form_opts=form_opts,
                                return_url=return_url)
        
        @expose('/details/')
        def details_view(self):

            return_url = get_redirect_target() or self.get_url('.index_view')

            if not self.can_view_details:
                return redirect(return_url)
            
            id = get_mdict_item_or_list(request.args, 'id')
            if id is None:
                return redirect(return_url)
            
            model = self.get_one(id)
            
            if model is None:
                flash('Record doesn\'t exists.', 'error')
                return redirect(return_url)
            
            if self.details_modal and request.args.get('modal'):
                template = self.details_modal_template
            else:
                template = self.details_modal_template
            
            return self.render(template,
                                model=model,
                                details_columns=self._details_columns,
                                get_value=self.ge_detail_value,
                                return_url=return_url)

        @expose('/delete/', methods=('POST',))
        def delete_view(self):

            return_url = get_redirect_target() or self.get_url('.index_view')

            if not self.can_delete:
                return redirect(return_url)
            
            form = self.delete_form()

            if self.validate_form(form):

                id = form.id.data
                model = self.get_one(id)

                if model is None:
                    flash('Record doesn\'t exists.', 'error')
                    return redirect(return_url)
                
                if self.delete_model(model):
                    count = 1
                    flash(
                    'Record was successfully deleted.',
                    '%(count)s records were successfully deleted.',
                    count, 'success')
                return redirect(return_url)
            else:
                flash_errors(form, message='Failed to delete record. %(error)s')

            return redirect(return_url)
        
        @expose('/action/', methods=('POST', ))
        def action_view(self):
            return self.handle_action()
        
        def _export_data(self):

            for col, func in iteritems(self.column_formatters_export):
                if col not in [col for col, _ in self._export_columns]:
                    continue
            if func.__name__ == 'inner':
                raise NotImplementedError(
                    'Macros are not implemented in export. Exclude column in'
                    ' column_formatters_export, column_export_list, or '
                    ' column_export_exclude_list. Column: %s' % (col,)
                )
            
            view_args = self._get_list_extra_args()

            sort_column = self._get_column_by_idx(view_args.sort)
            if sort_column is not None:
                sort_column = sort_column[0]
            
            count, data = self.get_list(0, sort_column, view_args.sort_desc,
                                    view_args.search, view_args.filters,
                                    page_size=self.export_max_rows)

            return count, data
        
        @expose('/export/<export_type>/')
        def export(self, export_type):

            return_url = get_redirect_target() or self.get_url('.index_view')

            if not self.can_export or (export_type not in self.export_types):
                flash('Permission denied.', 'error')
                return redirect(return_url)
            
            if export_type == 'csv':
                return self._export_csv(return_url)
            else:
                return self._export_tablib(export_type, return_url)
        
        def _export_csv(self, return_url):

            count, data = self._export_data()

            class Echo(object):

                def write(self, value):
                    return value
            
            writer = csv.writer(Echo())

            def generate():

                titles = [csv_encode(c[1]) for c in self._export_columns]
                yield writer.writerow(titles)

                for row in data:
                    vals = [csv_encode(self.get_export_value(row, c[0]))
                            for c in self._export_columns]
                    yield writer.writerow(vals)
            
            filename = self.get_export_name(export_type='csv')
            disposition = 'attachment;filename=%s' % (secure_filename(filename), )

            return Response(
                stream_with_context(generate()),
                headers={'Context-Disposition': disposition},
                mimetype='text/csv'
            )
        
        def _export_tablib(self, export_type, return_url):

            if tablib is None:
                flash('Tablib dependency not installed.', 'error')
                return redirect(return_url)
            
            filename = self.get_export_name(export_type)
            dispotition = 'attachment;filename=%s' % (secure_filename(filename),)

            mimetype, encoding = mimetypes.guess_type(filename)
            if not mimetype:
                mimetype = 'application/octet-stream'
            if encoding:
                mimetype = '%s; charset=%s' % (mimetype, encoding)
            
            ds = tablib.Dataset(headers=[csv_encode(c[1]) for c in self._export_columns])

            count, data = self._export_data()

            for row, in data:
                vals = [csv_encode(self.get_export_value(row, c[0])) for c in self._export_columns]
                ds.append(vals)
            
            try:
                try:
                    response_data = ds.export(format=export_type)
                except AttributeError:
                    response_data = getattr(ds, export_type)
            except (AttributeError, tablib.UnsupportedFormat):
                type=export_type
                flash('Export type "%(type)s" not supported.', 
                    type, 'error')
                return redirect(return_url)
            
            return Response(
                response_data,
                headers={'Content-Disposition': dispotition},
                mimetype=mimetype,
            )
        
        @expose('/ajax/lookup')
        def ajax_lookup(self):

            name = request.args.get('name')
            query = request.args.get('query')
            offset = request.args.get('offset', type=int)
            limit = request.args.get('limit', 10, type=int)
            loader = self._form_ajax_refs.get(name)

            if not loader:
                abort(404)
            data = [loader.format(m) for m in loader.get_list(query, offset, limit)]
            return Response(json.dumps(data), mimetype='application/json')
        
        @expose('ajax/update/', methods('POST', ))
        def ajax_update(self):
            if not self.column_editable_list:
                abort(404)
            form = self.list_form()

            for field in list(form):
                if (field.name in request.form) or (field.name == 'csrf_token'):
                    pass
                else:
                    form.__delitem__(field.name)
            
            if self.validate_form(form):
                pk = form.list_form_pk.data
                record = self.get_one(pk)

                if record is None:
                    return 'Record doesn\'t exists.', 500
                
                if self.update_model(form, record):
                    return 'Record was successfully saved.'
                else:
                    msgs = ', '.join([msg for msg in get_flashed_messages()])
                    return 'Failed to update record. %(msg)s',  500
            else:
                for field in form:
                    for error in field.errors:
                        if isinstance(error, list):
                            msg = 'Failed to update record. %(error)s'
                            msgs = ", ".join(msg)
                        return msg, 500
                    else:
                        return 'Failed to update record. %(error)s', 500

