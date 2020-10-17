from flask import Flask

import flask_admin as admin
from flask_admin import BaseView, AdminIndexView
from flask_admin import BaseM
###################################
#---<Create custom Admin ViewS>---#
###################################

# View 1
class MyAdminView(admin.BaseView):
    @admin.expose('/')
    def index(self):
        return self.render('myadmin.html')


# View 2
class AnotherAdminView(admin.BaseView):
    @admin.expose('/')
    def index(self):
        
        
        return self.render('anotheradmin.html')
    
    @admin.expose('/test/')
    def test(self):
        return self.render('test.html')

# View 3
class MyAdmin(admin.BaseView):

    @admin.expose('/')
    def index(self):

        return self.render('myadmin.html')


# Create Flask App
app = Flask(__name__, template_folder='templates')
app.debug = True


# Flask Views
@app.route('/')
def index():
    return '<a href="/admin/">Click me to get to Admin!</a>'

# Create Admin Interface
admin = admin.Admin(name='Admin Console', template_mode='bootstrap4', url='/hi', endpoint='fede')
# print(admin.index_view)
# for i in dir(admin):
#     print(i)
#     print('- - -'*30)
#     print(getattr(admin, i))
#     print('==='*30)
print(admin._views[0]._urls)
print(admin.index_view[0])

admin.add_view(MyAdminView(name='view1', category='Test'))
admin.add_view(AnotherAdminView(name='view2', category='Test'))
admin.add_view(MyAdmin(name='My Admin'))
admin.init_app(app)


if __name__ == '__main__':
    app.run() 