# Flask-Admin - auth-flask-login
=============================

#### Taken from [Flask-Admin Docs](#https://github.com/flask-admin/flask-admin/blob/master/examples/auth-flask-login/app.py)



## Important Notes

```

 class MyModelView(sqla.ModelView):

    def is_accessible(self):
        return login.current_user.is_authenticated

```

> This class add and overides the index view, adding a 'User' in the navbar, it inherits from the db.Model User.

The def is_accessible(self) defines who can enter, in this case implemented with flask-login, only if the current_user is authenticated

----------------------------------

```

{% block access_control %}

```

> Section to the right of the menu (can be used to add login/logout buttons)

----------------------------------

```

app.config['FLASK_ADMIN_SWATCH'] = 'flatly'

```

> Customize the look by specifying a Bootswatch theme that suits your needs- 

Check [Here](#http://bootswatch.com/3/) for bootstrap 3 available swatches.

----------------------------------


### Note.

> For some reason User.login can't be named username or anything else, if do this  **def validate_login(self, field):** would not work.

----------------------------------

        


