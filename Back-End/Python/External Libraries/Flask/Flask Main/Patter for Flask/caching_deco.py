


'''
The decorated function will work as follows

get the unique cache key for the current request based on the current path.

get the value for that key from the cache. If the cache returned something we will return that value.

otherwise the original function is called and the return value is stored in the cache for the timeout provided (by default 5 minutes).

'''

from functools import wraps
from flask import request


def cached(timeout=5 * 60, key='view/%s'):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):

            cache_key = key % request.path
            rv = cache.get(cache_key)
            if rv is not None:
                return rv
            rv = f(*args, **kwargs)
            cache.set(cache_key, timeout=timeout)
            return rv
        return decoreted_function
    return decorator