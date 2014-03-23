from bottle import Bottle

bottle = Bottle()

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@bottle.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'


# Define an handler for 404 errors.
@bottle.error(404)
def error_404(error):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.'
