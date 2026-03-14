def starts_with(string: str, prefix: str) -> bool:
    """
    Checks if a string starts with a given prefix.

    Args:
        string (str): The string to check.
        prefix (str): The prefix to look for.

    Returns:
        bool: True if the string starts with the prefix, False otherwise.

    Examples:
        >>> starts_with('hello world', 'hello')
        True
        >>> starts_with('hello world', 'world')
        False
        >>> starts_with('hello', '')
        True
    """
    return string.startswith(prefix)


def ends_with(string: str, suffix: str) -> bool:
    """
    Checks if a string ends with a given suffix.

    Args:
        string (str): The string to check.
        suffix (str): The suffix to look for.

    Returns:
        bool: True if the string ends with the suffix, False otherwise.

    Examples:
        >>> ends_with('hello world', 'world')
        True
        >>> ends_with('hello world', 'hello')
        False
        >>> ends_with('hello', '')
        True
    """
    return string.endswith(suffix)