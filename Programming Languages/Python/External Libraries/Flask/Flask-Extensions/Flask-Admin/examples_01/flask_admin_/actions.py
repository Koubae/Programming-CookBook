from flask import request, redirect

import tools
from _compat import text_type
from helpers import get_redirect_target, flash_errors


def action(name, text, confirmation=None):

    def wrap(f):
        f._action = (name, text, confirmation)
        return f
    return wrap


class ActionsMixin(object):

    def __init__(self):
        self._actions = []
        self._actions_data = {}
    
    def init_actions(self):
        self._actions = []
        self._actions_data = {}

        for p in dir(self):
            attr = tools.get_dict_attr(self, p)

            if hasattr(attr, '_action'):
                name, text, desc = attr._action
                self._actions.append((name, text))
                # TODO: Use namedtuple
                # Reason why we need getattr here - what's in attr is not
                # bound to the object.
                self._actions_data[name] = (getattr(self, p), text, desc)
    
    def is_action_allowed(self, name):
        return True
    
    def get_actions_list(self):

        actions = []
        actions_confirmation = {}

        for act in self._actions:
            name, text = act
            
            if self.is_action_allowed(name):
                actions.append((name, text_type(text)))
                
                confirmation = self._actions_data[name][2]
                if confirmation:
                    actions_confirmation[name] = text_type(confirmation)
        return actions, actions_confirmation
    
    def handle_action(self, return_view=None):

        form = self.action_form()

        if self.validate_form(form):
            ids = request.form.getlist('rowid')
            action = form.action.data

            handler = self._actions_data.get(action)

            if handler and self.is_action_allowed(action):
                response = handler[0](ids)
                if response is not None:
                    return response
        else:
            flash_errors(form, message='Failed to perform action. %(error)s')
        
        if return_view:
            url = self.get_url('.' + return_view)
        else:
            url = get_redirect_target() or self.get_url('.index_view')
        
        return redirect(url)
