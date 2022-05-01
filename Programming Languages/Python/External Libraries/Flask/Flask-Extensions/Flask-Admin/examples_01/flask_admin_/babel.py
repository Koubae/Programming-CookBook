try:
    from flask_babelex import Domain
except ImportError:
    def gettest(string, **variables):
        return string % variables