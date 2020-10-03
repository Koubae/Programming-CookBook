# The Request Context
=======================

- [DOCS](https://flask.palletsprojects.com/en/1.1.x/reqcontext/)



## How the Context Works

======================================================  
Flask.wsgi_app() = _app_ctx_stack + _request_ctx_stack
======================================================
======================================================
- 1. AppContext ==> RequestContext
-----------------------------
### If signals_available is true => request_started

- **BEFORE_REQUEST()**

---< *PROXIES OF THREAD* >---

- **current_app**
- **g**
- **request**
- **session**

-----------------------------

- **AFTER_REQUEST()**

### If signals_available is true => request_finished
======================================================
### If signals_available is true => got_request_exception 
--->> *errorhandler() *---> 

.1 teardown_request()
### If signals_available is true => request_tearing_down
.2 teardown_appcontext()
======================================================


-----------------------------------------------------------------------------------------------------

## Features


- [Context Locals](https://werkzeug.palletsprojects.com/en/1.0.x/local/)

Context locals are implemented in Werkzeug.

- [test_client](https://flask.palletsprojects.com/en/1.1.x/api/#flask.Flask.test_client)

```

app.testing = True
client = app.test_client()


# OR

with app.test_client() as c:
    rv = c.get('/?vodka=42')
    assert request.args['vodka'] == '42'

```

Additionally, you may pass optional keyword arguments that will then be passed to the application’s test_client_class constructor.

```

from flask.testing import FlaskClient

class CustomClient(FlaskClient):
    def __init__(self, *args, **kwargs):
        self._authentication = kwargs.pop("authentication")
        super(CustomClient,self).__init__( *args, **kwargs)

app.test_client_class = CustomClient
client = app.test_client(authentication='Basic ....')


```


- [test_request_context](https://flask.palletsprojects.com/en/1.1.x/api/#flask.Flask.test_request_context)

```
with test_request_context(...):
    generate_report()
```
When using the shell, it may be easier to push and pop the context manually to avoid indentation.

```
ctx = app.test_request_context(...)
ctx.push()
...
ctx.pop()

```

- [wsgi_app](https://flask.palletsprojects.com/en/1.1.x/api/#flask.Flask.wsgi_app)

```
app.wsgi_app = MyMiddleware(app.wsgi_app)

```
**Parameters:**

environ – A WSGI environment.

start_response – A callable accepting a status code, a list of headers, and an optional exception context to start the response.


- [_get_current_object](https://werkzeug.palletsprojects.com/en/1.0.x/local/#werkzeug.local.LocalProxy._get_current_object)

Return the current object. This is useful if you want the real object behind the proxy at a time for performance reasons or because you want to pass the object into a different context.

If you need to access the underlying object that is proxied, use the _get_current_object() method:


```
app = current_app._get_current_object()
my_signal.send(app)

```



### 


-----------------------------------------------------------------------------------------------------
