

'''
When you want to use the werkzeug routing system for more flexibility you need to map the endpoint as defined in the Rule to a view function. This is possible with this decorator.
'''

from flask import Flask
from werkzeug.routing import Rule

app = Flask(__name__)
app.url_map.add(Rule('/', endpoint='index'))

@app.endpoint('index')
def my_index():
    return "Hello world"