from typing import Optional




def left(original_str: str, end_str: str) -> Optional[str]:
    """
    Get the substring to the left of a given substring in a string.

    Args:
        original_str (str): The original string to search in.
        end_str (str): The substring to end the search at.

    Returns:
        Optional[str]: The substring to the left of the given end substring, or None if not found.

    Examples:
        >>> left('abc123def', 'def')
        'abc123'
    """
    from usepy.string._get_section import get_section

    result, *_ = get_section(original_str, end_str=end_str)
    return result
