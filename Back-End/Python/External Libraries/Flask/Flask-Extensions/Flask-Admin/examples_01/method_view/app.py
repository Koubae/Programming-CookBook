from flask import Flask, redirect, request
from flask.views import MethodView

import flask_admin as admin


class ViewWithMethodViews(admin.BaseView):
    @admin.expose('/')
    def index(self):
        return self.render('method.test.html')
    
    @admin.expose_plugview('/_api/1')
    class API_v1(MethodView):
        def get(self, cls):
            return cls.render('test.html', request=request, name='API_v1')
        
        def post(self, cls):
            return cls.render('test.html', request=request, name='API_v1')
    
    @admin.expose_plugview('/_api/2')
    class API_v2(MethodView):
        def get(self, cls):
            return cls.render('test.html', request=request, name='API_v2')
        
        def post(self, cls):
            return cls.render('test.html', request=request, name='API_v2')


# Create Flask app

app = Flask(__name__, template_folder='templates')


# Flask View
@app.route('/')
def index():
    return redirect('/admin')


if __name__ == '__main__':
    # Create admin interface
    admin = admin.Admin(name='Admin Console')
    admin.add_view(ViewWithMethodViews(name='API'))
    admin.init_app(app)
    app.run(debug=True)