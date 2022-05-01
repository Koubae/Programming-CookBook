# using abort to signal errors for invalid API usage is to implement your own exception type and install an error handler for it that produces the errors in the format the user is expecting.



from flask import jsonify

class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv

# At that point views can raise that error, but it would immediately result in an internal server error. The reason for this is that there is no handler registered for this error class. That however is easy to add:



@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

# Here is how a view can use that functionality:

@app.route('/foo')
def get_foo():
    raise InvalidUsage('This view is gone', status_code=410)