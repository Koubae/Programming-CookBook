import os

from flask import Flask, redirect, url_for
# Jinja2
from jinja2 import Markup



def create_app(test_config=None):
    
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=os.urandom(16),
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
    )

    if test_config is None:
        print('>>> No Config File Provided')
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.update(test_config)
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from flaskr import db

    db.init_app(app)

    from flaskr import auth, blog
    
    app.register_blueprint(auth.bp)
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')
    

    @app.route('/')
    @app.route('/hello')
    def hello():

        go_to_register = Markup(url_for('auth.register'))
        go_to_login = Markup(url_for('auth.login'))
        
        return f'''
        
        <!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Index</title>
            </head>
            <body>
                <br><br><br>
                <button><a href="{ go_to_register }">Signup</a></button>
                <br><br><br>
                <hr>
                <br><br><br>
                <button><a href="{ go_to_login }">Login</a></button>
                
            </body>
        </html>
        
        '''
    
    
    # Register Database Command
    

    return app





