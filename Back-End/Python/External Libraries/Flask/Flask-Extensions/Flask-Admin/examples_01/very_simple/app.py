from flask import Flask, session
from flask_admin import Admin, AdminIndexView, BaseView, BaseViewClass, AdminViewMeta
from flask_admin.contrib import sqla
from flask_admin import helpers, expose
import flask_admin
from flask_admin._compat import with_metaclass

app = Flask(__name__)

app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'


class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age

###############################
#---<CUSTOMIZED Index View>---#
###############################

class CustomView_3(AdminIndexView):

    @expose('/')
    def index(self):

        return super(CustomView, self).index()


###################
#---<BASE VIEW>---#
###################

# class Other(BaseView):
#     pass

class MyBaseView(BaseView):

    @expose('/')
    def index(self):

        #print(super()._template_args)
        #print(self)

        # y = with_metaclass(AdminViewMeta, BaseViewClass)
        # class X(with_metaclass(AdminViewMeta, BaseViewClass)):
        #     pass
        # x = X()
        # print(x)
        # print(y)
        # print(self._urls)
        # for url, name, methods in self._urls:
        #     print(url)
        #     print(name)
        #     print(methods)
        #     print('==='*30)
        # print(super()._urls)

        # if hasattr(self, '_urls'):
        #     x = getattr(self, '_urls')
        #     y = getattr(BaseView, '_urls')
        #     print(x)
        #     print(y)

        x = MyBaseView.__class__.__bases__[0]
        y = MyBaseView.__class__.__bases__
        z = MyBaseView.__bases__[0].__dict__
        print(x)
        print('==='*10)
        print(y)
        print(z)
        return 'Hello World'

    @expose('_urls/another')
    def another(self):

        x = 'Another page'
        return f'{x}'




admin = Admin(app, name='microblog', template_mode='bootstrap3')
# admin.add_view(MyView(name='My View', menu_icon_type='glyph', menu_icon_value='glyphicon-home'))
admin.add_view(MyBaseView(name='Base View'))



@app.route('/')
def index():
    

    #type.__init__(cls, classname, bases, fields)
    # for i in BaseView._template_args:
    #     print(i)
    print(BaseView._template_args)
    return '<a href="/admin/"><h1>Go to Admin</h1></a>'\
  



if __name__ == '__main__':
    app.run(debug=True)


