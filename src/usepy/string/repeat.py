def repeat(string: str, n: int) -> str:
    """
    Repeats a string n times.

    Args:
        string (str): The string to repeat.
        n (int): The number of times to repeat.

    Returns:
        str: The repeated string.

    Examples:
        >>> repeat('abc', 3)
        'abcabcabc'
        >>> repeat('x', 0)
        ''
        >>> repeat('', 5)
        ''
    """
    return string * n