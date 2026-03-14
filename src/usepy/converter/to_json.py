import json
from typing import Any, Optional


def to_json(obj: Any, indent: Optional[int] = None, ensure_ascii: bool = False) -> str:
    """
    Converts an object to a JSON string.

    Args:
        obj (Any): The object to convert.
        indent (Optional[int]): The number of spaces for indentation. Defaults to None (compact).
        ensure_ascii (bool): Whether to escape non-ASCII characters. Defaults to False.

    Returns:
        str: The JSON string.

    Examples:
        >>> to_json({'a': 1, 'b': 2})
        '{"a": 1, "b": 2}'
        >>> to_json({'name': '张三'}, ensure_ascii=False)
        '{"name": "张三"}'
        >>> to_json([1, 2, 3], indent=2)
        '[\\n  1,\\n  2,\\n  3\\n]'
    """
    return json.dumps(obj, indent=indent, ensure_ascii=ensure_ascii)


def from_json(json_string: str, default: Any = None) -> Any:
    """
    Parses a JSON string into a Python object.

    Args:
        json_string (str): The JSON string to parse.
        default (Any): The default value to return if parsing fails. Defaults to None.

    Returns:
        Any: The parsed Python object, or default if parsing fails.

    Examples:
        >>> from_json('{"a": 1, "b": 2}')
        {'a': 1, 'b': 2}
        >>> from_json('[1, 2, 3]')
        [1, 2, 3]
        >>> from_json('invalid json', default={})
        {}
    """
    try:
        return json.loads(json_string)
    except (json.JSONDecodeError, TypeError):
        return default