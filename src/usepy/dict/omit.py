from typing import TypeVar, Dict, Iterable

K = TypeVar('K')
V = TypeVar('V')


def omit(d: Dict[K, V], keys: Iterable[K]) -> Dict[K, V]:
    """
    Creates a new dictionary without the specified keys.

    Args:
        d (Dict[K, V]): The source dictionary.
        keys (Iterable[K]): The keys to omit.

    Returns:
        Dict[K, V]: A new dictionary without the omitted keys.

    Examples:
        >>> omit({'a': 1, 'b': 2, 'c': 3}, ['b'])
        {'a': 1, 'c': 3}
        >>> omit({'a': 1, 'b': 2}, ['x', 'y'])
        {'a': 1, 'b': 2}
        >>> omit({}, ['a'])
        {}
    """
    keys_set = set(keys)
    return {k: v for k, v in d.items() if k not in keys_set}