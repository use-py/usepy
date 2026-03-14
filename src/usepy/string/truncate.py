from typing import Optional


def truncate(string: str, length: int = 30, omission: str = '...') -> str:
    """
    Truncates a string to a specified length and adds an omission string.

    Args:
        string (str): The string to truncate.
        length (int): The maximum length of the result. Defaults to 30.
        omission (str): The string to add at the end. Defaults to '...'.

    Returns:
        str: The truncated string.

    Examples:
        >>> truncate('hello world this is a long string', 15)
        'hello world...'
        >>> truncate('short', 10)
        'short'
        >>> truncate('hello world', 8, omission='~')
        'hello w~'
    """
    if len(string) <= length:
        return string

    # Calculate how much of the original string to keep
    keep_length = length - len(omission)
    if keep_length <= 0:
        return omission[:length]

    return string[:keep_length] + omission