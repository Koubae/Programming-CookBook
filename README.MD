# Flask Recipes CookBook
=======================


### Features


> #### [Sentry](https://sentry.io/welcome/) & [For Flask](https://sentry.io/for/flask/)

- [GITHUB](https://github.com/getsentry/sentry)

- Getting started ---> [DOCS](https://docs.sentry.io/platforms/)

- For Flask Docs ---> [DOCS](https://docs.sentry.io/platforms/python/guides/flask/)

- [From Flask ---> DOCS](https://flask.palletsprojects.com/en/1.1.x/errorhandling/)

- [Black](https://black.readthedocs.io/en/stable/)

- [pre-commit](https://pre-commit.com/)

- [Coverage.py](https://coverage.readthedocs.io/en/coverage-5.3/)

> #### [Logging](https://docs.python.org/3/library/logging.html#module-logging)



# Jinja Setup
=======================

## Standard Context

- **Flask inserts a couple of global functions and helpers into the Jinja2 context, additionally to the values that are present by default.**

The following global variables are available within Jinja2 templates by default

- config

*The current configuration object (flask.config)*

- request

*The current request object (flask.request). This variable is unavailable if the template was rendered without an active request context.*

- session

*The current session object (flask.session). This variable is unavailable if the template was rendered without an active request context.*

- g

*The request-bound object for global variables (flask.g). This variable is unavailable if the template was rendered without an active request context.*

- url_for()

*The flask.url_for() function.*

- get_flashed_messages()

*The flask.get_flashed_messages() function.*

### The Jinja Context Behavior

**For Macros**

you explicitly pass the request to the macro as parameter, or the attribute of the request object you are interested in.

you import the macro “with context”.

Importing with context looks like this:

```{% from '_helpers.html' import my_macro with context %}```


-----------------------------------------------------------------------------------------------------

## Standard Filters

- tojson()

This function converts the given object into JSON representation. This is for example very helpful if you try to generate JavaScript on the fly


```

<script type=text/javascript>
    doSomethingWith({{ user.username|tojson }});
</script>


<button onclick='doSomethingWith({{ user.username|tojson }})'>
    Click me
</button>


```

-----------------------------------------------------------------------------------------------------

## Registering Filters

If you want to register your own filters in Jinja2 you have two ways to do that. You can either put them by hand into the jinja_env of the application or use the template_filter() decorator.

```

@app.template_filter('reverse')
def reverse_filter(s):
    return s[::-1]

def reverse_filter(s):
    return s[::-1]
app.jinja_env.filters['reverse'] = reverse_filter

```

-----------------------------------------------------------------------------------------------------

## Context Processors

**Injects new variables/functions automatically into the context of a template, context processors exist in Flask.**
```

@app.context_processor
def inject_user():
    return dict(user=g.user)


@app.context_processor
def utility_processor():
    def format_price(amount, currency=u'€'):
        return u'{0:.2f}{1}'.format(amount, currency)
    return dict(format_price=format_price)

{{ format_price(0.33) }}

```

-----------------------------------------------------------------------------------------------------

## Controlling Autoescaping 

- *[Cross-Site Scripting (XSS)](https://flask.palletsprojects.com/en/1.1.x/security/#xss)*

- In the Python code, wrap the HTML string in a Markup object before passing it to the template. This is in general the recommended way.

- Inside the template, use the |safe filter to explicitly mark a string as safe HTML ```({{ myvariable|safe }})```

- Temporarily disable the autoescape system altogether.

```

{% autoescape false %}
    <p>autoescaping is disabled here
    <p>{{ will_not_be_escaped }}
{% endautoescape %}

```

-----------------------------------------------------------------------------------------------------

## Custom Error Pages

- [DOCS](https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/)

-----------------------------------------------------------------------------------------------------

### Common Error Codes

- *404 Not Found*
The good old “chap, you made a mistake typing that URL” message. So common that even novices to the internet know that 404 means: damn, the thing I was looking for is not there. It’s a very good idea to make sure there is actually something useful on a 404 page, at least a link back to the index.

- *403 Forbidden*
If you have some kind of access control on your website, you will have to send a 403 code for disallowed resources. So make sure the user is not lost when they try to access a forbidden resource.

- *410 Gone*
Did you know that there the “404 Not Found” has a brother named “410 Gone”? Few people actually implement that, but the idea is that resources that previously existed and got deleted answer with 410 instead of 404. If you are not deleting documents permanently from the database but just mark them as deleted, do the user a favour and use the 410 code instead and display a message that what they were looking for was deleted for all eternity.

- *500 Internal Server Error*
Usually happens on programming errors or if the server is overloaded. A terribly good idea is to have a nice page there, because your application will fail sooner or later (see also: Application Errors).

----------------------------------

- [HTTPException](https://werkzeug.palletsprojects.com/en/1.0.x/exceptions/#werkzeug.exceptions.HTTPException)
- [errorhandler](https://flask.palletsprojects.com/en/1.1.x/api/#flask.Flask.errorhandler)
- [register_error_handler](https://flask.palletsprojects.com/en/1.1.x/api/#flask.Flask.register_error_handler)

-----------------------------------------------------------------------------------------------------

## Deployment Options

- [DOCS](https://flask.palletsprojects.com/en/1.1.x/deploying/)

-----------------------------------------------------------------------------------------------------

## Security Headers

- [Flask-Talisman](https://github.com/GoogleCloudPlatform/flask-talisman)

-----------------------------------------------------------------------------------------------------

## Set-Cookie 

- [DOCS](https://flask.palletsprojects.com/en/1.1.x/security/#set-cookie-options)

**Use itsdangerous.TimedSerializer to sign and validate other cookie values (or any values that need secure signatures).**

- *Secure:* limits cookies to HTTPS traffic only.

- *HttpOnly:* protects the contents of cookies from being read with JavaScript.

- *SameSite:* restricts how cookies are sent with requests from external sites. Can be set to 'Lax' (recommended) or 'Strict'. Lax prevents sending cookies with CSRF-prone requests from external sites, such as submitting a form. Strict prevents sending cookies with all external requests, including following regular links.

```

app.config.update(
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Lax',
)

response.set_cookie('username', 'flask', secure=True, httponly=True, samesite='Lax')


```

```
# cookie expires after 10 minutes
response.set_cookie('snakes', '3', max_age=600)
```

For the session cookie, if session.permanent is set, then PERMANENT_SESSION_LIFETIME is used to set the expiration. Flask’s default cookie implementation validates that the cryptographic signature is not older than this value. Lowering this value may help mitigate replay attacks, where intercepted cookies can be sent at a later time.

```
app.config.update(
    PERMANENT_SESSION_LIFETIME=600
)

@app.route('/login', methods=['POST'])
def login():
    ...
    session.clear()
    session['user_id'] = user.id
    session.permanent = True
    ...

```


-----------------------------------------------------------------------------------------------------


#### Notes
- [The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets (No Excuses!)](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/)

- [Discord](https://discord.gg/t6rrQZH)
- [How to create a Minimal, Reproducible Example](https://stackoverflow.com/help/minimal-reproducible-example)
-----------------------------------------------------------------------------------------------------