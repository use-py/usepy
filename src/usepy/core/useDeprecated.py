import warnings
from functools import wraps


def useDeprecated(use_instead=None):
    """
    mark functions as deprecated
    """

    def deco(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            message = "Call to deprecated function %s." % func.__name__
            if use_instead:
                message += " Use %s instead." % use_instead
            warnings.warn(message, stacklevel=2)
            return func(*args, **kwargs)

        return wrapped

    if callable(use_instead):
        deco = deco(use_instead)
        use_instead = None
    return deco
