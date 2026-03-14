from typing import TypeVar, Dict, Iterable, Any

K = TypeVar('K')
V = TypeVar('V')


def pick(d: Dict[K, V], keys: Iterable[K]) -> Dict[K, V]:
    """
    Creates a new dictionary with only the specified keys.

    Args:
        d (Dict[K, V]): The source dictionary.
        keys (Iterable[K]): The keys to pick.

    Returns:
        Dict[K, V]: A new dictionary with only the picked keys.

    Examples:
        >>> pick({'a': 1, 'b': 2, 'c': 3}, ['a', 'c'])
        {'a': 1, 'c': 3}
        >>> pick({'a': 1, 'b': 2}, ['x', 'y'])
        {}
        >>> pick({}, ['a'])
        {}
    """
    return {k: d[k] for k in keys if k in d}