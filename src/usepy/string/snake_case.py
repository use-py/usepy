from typing import Union


def snake_case(string: Union[str, bytes]) -> str:
    """
    Converts a string to snake case.

    Snake case is the naming convention in which each word is written in lowercase
    and separated by an underscore (_) character.

    Args:
        string (Union[str, bytes]): The input string to be converted to snake case.

    Returns:
        str: The converted string in snake case.

    Examples:
        >>> snake_case('camelCase')
        'camel_case'
        >>> snake_case('some whitespace')
        'some_whitespace'
        >>> snake_case('hyphen-text')
        'hyphen_text'
        >>> snake_case('HTTPRequest')
        'http_request'
    """
    from usepy.string._get_words import get_words

    if isinstance(string, bytes):
        string = string.decode("utf-8")

    words = get_words(string)
    return "_".join(word.lower() for word in words)
