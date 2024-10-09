from typing import TypeVar

T = TypeVar('T', bound=str)


def capitalize(string: T) -> T:
    """
    Converts the first character of a string to uppercase and the remaining characters to lowercase.

    Args:
        string (T): The string to be capitalized.

    Returns:
        Capitalize[T]: The capitalized string.

    Examples:
        >>> capitalize('fred')
        'Fred'
        >>> capitalize('FRED')
        'Fred'
    """
    return string.title()
