def pad_start(string: str, length: int, pad: str = ' ') -> str:
    """
    Pads a string on the left to a specified length.

    Args:
        string (str): The string to pad.
        length (int): The target length.
        pad (str): The padding string. Defaults to space.

    Returns:
        str: The padded string.

    Examples:
        >>> pad_start('abc', 5)
        '  abc'
        >>> pad_start('abc', 6, 'x')
        'xxxabc'
        >>> pad_start('abc', 2)
        'abc'
    """
    if len(string) >= length:
        return string

    padding_needed = length - len(string)
    if not pad:
        return string

    # Create padding by repeating the pad string
    padding = (pad * ((padding_needed // len(pad)) + 1))[:padding_needed]
    return padding + string


def pad_end(string: str, length: int, pad: str = ' ') -> str:
    """
    Pads a string on the right to a specified length.

    Args:
        string (str): The string to pad.
        length (int): The target length.
        pad (str): The padding string. Defaults to space.

    Returns:
        str: The padded string.

    Examples:
        >>> pad_end('abc', 5)
        'abc  '
        >>> pad_end('abc', 6, 'x')
        'abcxxx'
        >>> pad_end('abc', 2)
        'abc'
    """
    if len(string) >= length:
        return string

    padding_needed = length - len(string)
    if not pad:
        return string

    # Create padding by repeating the pad string
    padding = (pad * ((padding_needed // len(pad)) + 1))[:padding_needed]
    return string + padding