from typing import Optional, List


def middle_batch(
        original_str: str,
        start_str: Optional[str] = None,
        end_str: Optional[str] = None,
        max_count: Optional[int] = None,
) -> List[str]:
    """
    Get a list of substrings between two given substrings in a string.

    Args:
        original_str (str): The original string to search in.
        start_str (Optional[str], optional): The substring to start the search from.
            If not provided, the search starts from the beginning of the string.
        end_str (Optional[str], optional): The substring to end the search at.
            If not provided, the search ends at the end of the string.
        max_count (Optional[int], optional): The maximum number of substrings to return.
            If not provided or set to None, all substrings will be returned.

    Returns:
        List[str]: A list of substrings between the start and end substrings.

    Examples:
        >>> middle_batch('abc123def456abc789def', 'abc', 'def')
        ['123', '789']
        >>> middle_batch('abc123def456abc789def', 'abc', 'def', 1)
        ['123']
    """
    from usepy.string._get_section import get_section

    result = []
    original_str_copy = original_str

    while True:
        substring, start_index, end_index = get_section(original_str_copy, start_str, end_str)
        if substring is None:
            break

        result.append(substring)
        original_str_copy = original_str_copy[end_index + len(end_str or ""):]

    if max_count is not None:
        return result[:max_count]
    else:
        return result
