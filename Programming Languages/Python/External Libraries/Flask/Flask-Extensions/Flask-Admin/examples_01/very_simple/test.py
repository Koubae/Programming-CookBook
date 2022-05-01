from flask import Flask, session
from flask_admin import Admin, AdminIndexView, BaseView, BaseViewClass, AdminViewMeta
from flask_admin.contrib import sqla
from flask_admin import helpers, expose
import flask_admin
from flask_admin._compat import with_metaclass




# class X(with_metaclass(AdminViewMeta, BaseViewClass)):
#             pass


# x = X()
# print(x.__dict__)
# # print(dir(x))

# print(x._urls)
my_d = {'field':'field'}

class View(type):

    def __init__(cls, classname, bases, fields):
        type.__init__(cls, classname, bases, fields)




class X(with_metaclass(View)):
            pass

# x = View('New Class', ('bases',), my_d)
# print(x)


x = X()
# print(x.__class__)
# print(dir(x))