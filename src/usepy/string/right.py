from typing import Optional


def right(original_str: str, start_str: str) -> Optional[str]:
    """
    Get the substring to the right of a given substring in a string.

    Args:
        original_str (str): The original string to search in.
        start_str (str): The substring to start the search from.

    Returns:
        Optional[str]: The substring to the right of the given start substring, or None if not found.

    Examples:
        >>> right('abc123def', 'abc')
        '123def'
    """
    from usepy.string._get_section import get_section

    result, *_ = get_section(original_str, start_str=start_str)
    return result
