# flask Other Functionality 
=======================

Most used functionality and Flask Feature.

- [DOCS](https://flask.palletsprojects.com/en/1.1.x/patterns/)


-----------------------------------------------------------------------------------------------------

## Larger Applications


```
/yourapplication
    /yourapplication
        __init__.py
        /static
            style.css
        /templates
            layout.html
            index.html
            login.html
            ...

```
```

from setuptools import setup

setup(
    name='yourapplication',
    packages=['yourapplication'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)

```

```

$ export FLASK_APP=yourapplication
$ export FLASK_ENV=development
$ pip install -e .
$ flask run

```
-----------------------------------------------------------------------------------------------------

## Application Dispatching

- [DOCS](https://flask.palletsprojects.com/en/1.1.x/patterns/appdispatch/)

Each of the techniques and examples below results in an application object that can be run with any WSGI server.

- [ werkzeug.serving.run_simple():](https://werkzeug.palletsprojects.com/en/1.0.x/serving/#werkzeug.serving.run_simple)

```

from flask import Flask
from werkzeug.serving import run_simple

app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    run_simple('localhost', 5000, app,
               use_reloader=True, use_debugger=True, use_evalex=True)

```

-----------------------------------------------------------------------------------------------------

## Deploying with SetupTools

### Features:

- [Virtualenv](https://click.palletsprojects.com/en/7.x/quickstart/#virtualenv)
- [Deploying with Fabric](https://flask.palletsprojects.com/en/1.1.x/patterns/fabric/#fabric-deployment)


```

from setuptools import setup

setup(
    name='Your Application',
    version='1.0',
    long_description=__doc__,
    packages=['yourapplication'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask']
)


```
If you want setuptools to lookup the packages for you automatically, you can use the find_packages function:

```

from setuptools import setup, find_packages

setup(
    ...
    packages=find_packages()
)

```

Create a MANIFEST.in file next to your setup.py file. This file lists all the files that should be added to your tarball. he reason for this is that setuptools does not know which files to add for you.

```
recursive-include yourapplication/templates *
recursive-include yourapplication/static *
```
By default it will always use the most recent version, but you can also provide minimum and maximum version requirements.

```
install_requires=[
    'Flask>=0.2',
    'SQLAlchemy>=0.6',
    'BrokenPackage>=0.7,<=1.0'
]
```

Provide a list of alternative locations where setuptools should look for tarballs:

```
dependency_links=['http://example.com/yourfiles']
```

```
$ python setup.py install

# If you are developing on the package and also want the requirements to be installed, you can use the develop command instead:

$ python setup.py develop
```
-----------------------------------------------------------------------------------------------------

## Caching

Flask itself does not provide caching for you, but Flask-Caching, an extension for Flask does. Flask-Caching supports various backends, and it is even possible to develop your own caching backend.

- [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/)

## Lazily Loading Views

- [DOCS](https://flask.palletsprojects.com/en/1.1.x/patterns/lazyloading/)

Flask is usually used with the decorators. Decorators are simple and you have the URL right next to the function that is called for that specific URL. However there is a downside to this approach: it means all your code that uses decorators has to be imported upfront or Flask will never actually find your function.

This can be a problem if your application has to import quick. It might have to do that on systems like Google’s App Engine or other systems. So if you suddenly notice that your application outgrows this approach you can fall back to a centralized URL mapping.

The system that enables having a central URL map is the add_url_rule() function. Instead of using decorators, you have a file that sets up the application with all URLs.

- [ add_url_rule()](https://flask.palletsprojects.com/en/1.1.x/api/#flask.Flask.add_url_rule)

-----------------------------------------------------------------------------------------------------

## Adding Favicon

- [DOCS](https://flask.palletsprojects.com/en/1.1.x/patterns/favicon/)
- [send_from_directory](https://flask.palletsprojects.com/en/1.1.x/api/#flask.send_from_directory)

```
<link rel="shortcut icon" href="{{ url_for('static', filename='favicon.ico') }}">
```

```
app.add_url_rule('/favicon.ico',
                 redirect_to=url_for('static', filename='favicon.ico'))
```
```
import os
from flask import send_from_directory

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

```

-----------------------------------------------------------------------------------------------------

## Celery Background Tasks

- [DOCS](https://flask.palletsprojects.com/en/1.1.x/patterns/celery/)
- [Celery](https://docs.celeryproject.org/en/latest/getting-started/first-steps-with-celery.html)

Celery is a powerful task queue that can be used for simple background tasks as well as complex multi-stage programs and schedules.

-----------------------------------------------------------------------------------------------------

### 


-----------------------------------------------------------------------------------------------------