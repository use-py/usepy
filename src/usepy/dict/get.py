from typing import TypeVar, Dict, Any, Optional, Union, List

K = TypeVar('K')
V = TypeVar('V')


def get(d: Dict[K, Any], path: Union[str, List[K]], default: Optional[V] = None) -> Optional[V]:
    """
    Safely gets a value from a nested dictionary using a path.

    Args:
        d (Dict[K, Any]): The source dictionary.
        path (Union[str, List[K]]): The path to the value. Can be a dot-separated string or a list of keys.
        default (Optional[V]): The value to return if path doesn't exist. Defaults to None.

    Returns:
        Optional[V]: The value at the path, or default if not found.

    Examples:
        >>> get({'a': {'b': {'c': 1}}}, 'a.b.c')
        1
        >>> get({'a': {'b': {'c': 1}}}, ['a', 'b', 'c'])
        1
        >>> get({'a': {'b': 1}}, 'a.x.y')
        None
        >>> get({'a': {'b': 1}}, 'a.x.y', default=0)
        0
    """
    if isinstance(path, str):
        keys = path.split('.')
    else:
        keys = path

    current = d
    for key in keys:
        if not isinstance(current, dict) or key not in current:
            return default
        current = current[key]

    return current