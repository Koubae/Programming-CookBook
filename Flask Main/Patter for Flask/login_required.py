from functools import wraps
from flask import g, request, redirect, url_for



def login_required(f):

    @wraps(f)
    def decoreted_function(*args, **kwargs):
        if g.user is None:
            return redirect(url_for('login', next=request.url))
        return f(*args, *kwargs)
    return decoreted_function

@app.route('/secret_page')
@login_required
def secret_page():
    pass




'''

The next value will exist in request.args after a GET request for the login page. You’ll have to pass it along when sending the POST request from the login form. You can do this with a hidden input tag, then retrieve it from request.form when logging the user in.

'''


# <input type="hidden" value="{{ request.args.get('next', '') }}"/>





# Solution N 2 
next = request.args.get('next')
			if next == None or not next[0] == '/':
				next = url_for('core.index')
			return redirect(next)