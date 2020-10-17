from flask import Flask 

import flask_admin as admin


#######################
#-------<VIEWS>-------#
#######################

# First
class FirstView(admin.BaseView):
    @admin.expose('/')
    def index(self):
        return self.render('first.html')


# Second
class SecondView(admin.BaseView):
    @admin.expose('/')
    def index(self):
        return self.render('second.html')


# Create Flask app
app = Flask(__name__, template_folder='templates')


# Flask Views
@app.route('/')
def index():
     return '<a href="/admin1">Click me to get to Admin 1</a><br/><a href="/admin2">Click me to get to Admin 2</a>'


if __name__ == '__main__':
    # Create First Administrative interface under /admin1
    admin1 = admin.Admin(app, url='/admin1')
    admin1.add_view(FirstView())

    #Create Second Administrative interface under /admin2
    admin2 = admin.Admin(app, url='/admin2', endpoint='admin2')
    admin2.add_view(SecondView())

    app.run(debug=True)