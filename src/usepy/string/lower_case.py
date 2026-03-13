from typing import Union


def lower_case(string: Union[str, bytes]) -> str:
    """
    Converts a string to lower case.

    Lower case is the naming convention in which each word is written in lowercase
    and separated by a space ( ) character.

    Args:
        string (Union[str, bytes]): The input string to be converted to lower case.

    Returns:
        str: The converted string in lower case.

    Examples:
        >>> lower_case('camelCase')
        'camel case'
        >>> lower_case('some whitespace')
        'some whitespace'
        >>> lower_case('hyphen-text')
        'hyphen text'
        >>> lower_case('HTTPRequest')
        'http request'
    """
    from usepy.string._get_words import get_words

    if isinstance(string, bytes):
        string = string.decode('utf-8')

    words = get_words(string)
    return ' '.join(word.lower() for word in words)
