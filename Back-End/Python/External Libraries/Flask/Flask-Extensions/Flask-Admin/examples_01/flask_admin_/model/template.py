#  Note taken from --> https://gist.github.com/JungeAlexander/6ce0a5213f3af56d7369 & https://stackoverflow.com/questions/714063/importing-modules-from-parent-folder/11158224#11158224
import os, sys, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from jinja2 import contextfunction

from _compat import string_types, reduce


class BaseListRowAction(object):

    def __init__(self, title=None):
        self.title = title
    
    def render(self, context, row_id, row):
        raise NotImplementedError()
    
    @contextfunction
    def render_ctx(self, context, row_id, row):
        return self.render(context, row_id, row)
    
    def _resolve_symbol(self, context, symbol):
        if '.' in symbol:
            parts = symbol.split('.')
            m = context.resolve(parts[0])
            return reduce(getattr, parts[1:], m)
        else:
            return context.resolve(symbol)


class LinkRowAction(BaseListRowAction):

    def __init__(self, icon_class, url, title=None):
        super(LinkRowAction, self).__init__(title=title)
        self.url = url
        self.icon_class = icon_class
    
    def render(self, context, row_id, row):
        m = self._resolve_symbol(context, 'row_actions.link')

        if isinstance(self.url, string_types):
            url = self.url.format(row_id=row_id)
        else:
            url = self.url(self, row_id, row)
        return m(self, url)


class EndpointLinkRowAction(BaseListRowAction):

    def __init__(self, icon_class, endpoint, title=None, id_arg='id', url_args=None):
        super(EndpointLinkRowAction, self).__init__(title=title)
        self.icon_class = icon_class
        self.endpoint = endpoint
        self.id_args = id_arg
        self.url_args = url_args
    
    def render(self, context, row_id, row):
        m = self._resolve_symbol(context, 'row_actions.link')
        get_url = self._resolve_symbol(context, 'get_url')
        kwargs = dict(self.url_args) if self.url_args else {}
        kwargs[self.id_args] = row_id

        url = get_url(self.endpoint, **kwargs)
        return m(self, url)


class TemplateLinkRowAction(BaseListRowAction):

    def __init__(self, template_name, title=None):
        super(TemplateLinkRowAction, self).__init__(title=title)
        self.template_name = template_name
    
    def render(self, context, row_id, row):
        m = self._resolve_symbol(context, self.template_name)
        return m(self, row_id, row)


class ViewRowAction(TemplateLinkRowAction):

    def __init__(self):
        super(ViewRowAction, self).__init__('row_actions.view_row', 'View Record')


class ViewPopupRowAction(TemplateLinkRowAction):

    def __init__(self):
        super(ViewPopupRowAction, self).__init__('row_actions.view_row_popup', 'View Record')


class EditRowAction(TemplateLinkRowAction):

    def __init__(self):
        super(EditRowAction, self).__init__('row_actions.edit_row', 'Edit Record')


class EditPopupRowAction(TemplateLinkRowAction):

    def __init__(self):
        super(EditPopupRowAction, self).__init__('row_actions.edit_row_popup', 'Edit Record')


class DeleteRowAction(TemplateLinkRowAction):

    def __init__(self):
        super(DeleteRowAction, self).__init__('row_actions.delete_row', 'Delete Record')

def marco(name):

    def inner(view, context, model, column):
        m = context.resolve(name)
        if not m:
            return m
        return m(model=model, column=column)
    return inner
    