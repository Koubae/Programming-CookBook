from flask_admin import BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.fileadmin import FileAdmin

from werkzeug.security import generate_password_hash
from flask_login import current_user, logout_user
from models import *
from app import admin, path

class UserView(ModelView):

    column_exclude_list = []
    column_display_pk = True
    can_edit = True
    can_delete = False
    can_export = True

    def on_model_change(self, form, model, is_created):
        model.password = generate_password_hash(model.password, method='sha256')

        inline_models = [Comment]
    
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return '<h1> You are logged in</h1>'


class CommentView(ModelView):
    
    create_modal = True


class NotificationsView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/notification.html')


# Add views to Admin

admin.add_view(UserView(User, db.session))
admin.add_view(CommentView(Comment, db.session))
admin.add_view(FileAdmin(path, '/uploads/', name='Uploads'))
admin.add_view(NotificationsView(name='Notifications', endpoint='notify'))



