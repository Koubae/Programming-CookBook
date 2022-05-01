# The Application Context
=======================

- [DOCS](https://flask.palletsprojects.com/en/1.1.x/appcontext/)


-----------------------------------------------------------------------------------------------------

## Features

- [Werkzeug.LocalProxy](https://werkzeug.palletsprojects.com/en/1.0.x/local/#werkzeug.local.LocalProxy)

-----------------------------------------------------------------------------------------------------

- **app_context()**

An application context is automatically pushed by RequestContext.push() when handling a request, and when running a CLI command. Use this to manually create a context outside of these situations.

```


def create_app():
    app = Flask(__name__)

    with app.app_context():
        init_db()

    return app


```

Common use for g is to manage resources during a request.

get_X() creates resource X if it does not exist, caching it as g.X.

teardown_X() closes or otherwise deallocates the resource if it exists. It is registered as a teardown_appcontext() handler.

```

from flask import g

def get_db():
    if 'db' not in g:
        g.db = connect_to_database()

    return g.db

@app.teardown_appcontext
def teardown_db():
    db = g.pop('db', None)

    if db is not None:
        db.close()

```

### 


-----------------------------------------------------------------------------------------------------
