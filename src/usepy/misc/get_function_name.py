import inspect


def get_function_name():
    """
    get the name of the current function

    >>> def a():
    ...     def b():
    ...         return get_function_name()
    ...     return b
    ...
    >>> a()()
    'b'
    """
    return inspect.currentframe().f_back.f_code.co_name
