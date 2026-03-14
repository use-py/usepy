from typing import TypeVar, Dict, Callable

K = TypeVar('K')
V = TypeVar('V')
V2 = TypeVar('V2')


def map_values(d: Dict[K, V], mapper: Callable[[V], V2]) -> Dict[K, V2]:
    """
    Creates a new dictionary with values transformed by a function.

    Args:
        d (Dict[K, V]): The source dictionary.
        mapper (Callable[[V], V2]): A function that transforms each value.

    Returns:
        Dict[K, V2]: A new dictionary with transformed values.

    Examples:
        >>> map_values({'a': 1, 'b': 2}, lambda x: x * 2)
        {'a': 2, 'b': 4}
        >>> map_values({'a': 'x', 'b': 'y'}, str.upper)
        {'a': 'X', 'b': 'Y'}
    """
    return {k: mapper(v) for k, v in d.items()}