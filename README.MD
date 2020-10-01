# Flask Recipes CooBook
=======================


### Features


> #### [Sentry](https://sentry.io/welcome/) & [For Flask](https://sentry.io/for/flask/)

- [GITHUB](https://github.com/getsentry/sentry)

- Getting started ---> [DOCS](https://docs.sentry.io/platforms/)

- For Flask Docs ---> [DOCS](https://docs.sentry.io/platforms/python/guides/flask/)

- [From Flask ---> DOCS](https://flask.palletsprojects.com/en/1.1.x/errorhandling/)

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