from typing import Optional


def trim(string: str, chars: Optional[str] = None) -> str:
    """
    Removes leading and trailing whitespace or specified characters.

    Args:
        string (str): The string to trim.
        chars (Optional[str]): Characters to remove. Defaults to whitespace.

    Returns:
        str: The trimmed string.

    Examples:
        >>> trim('  hello  ')
        'hello'
        >>> trim('xxhelloxx', 'x')
        'hello'
        >>> trim('\\n\\thello\\n', None)
        'hello'
    """
    return string.strip(chars)


def trim_start(string: str, chars: Optional[str] = None) -> str:
    """
    Removes leading whitespace or specified characters.

    Args:
        string (str): The string to trim.
        chars (Optional[str]): Characters to remove. Defaults to whitespace.

    Returns:
        str: The trimmed string.

    Examples:
        >>> trim_start('  hello  ')
        'hello  '
        >>> trim_start('xxhelloxx', 'x')
        'helloxx'
    """
    return string.lstrip(chars)


def trim_end(string: str, chars: Optional[str] = None) -> str:
    """
    Removes trailing whitespace or specified characters.

    Args:
        string (str): The string to trim.
        chars (Optional[str]): Characters to remove. Defaults to whitespace.

    Returns:
        str: The trimmed string.

    Examples:
        >>> trim_end('  hello  ')
        '  hello'
        >>> trim_end('xxhelloxx', 'x')
        'xxhello'
    """
    return string.rstrip(chars)