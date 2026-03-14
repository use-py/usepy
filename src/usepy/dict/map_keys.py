from typing import TypeVar, Dict, Callable

K = TypeVar('K')
V = TypeVar('V')
K2 = TypeVar('K2')


def map_keys(d: Dict[K, V], mapper: Callable[[K], K2]) -> Dict[K2, V]:
    """
    Creates a new dictionary with keys transformed by a function.

    Args:
        d (Dict[K, V]): The source dictionary.
        mapper (Callable[[K], K2]): A function that transforms each key.

    Returns:
        Dict[K2, V]: A new dictionary with transformed keys.

    Examples:
        >>> map_keys({'a': 1, 'b': 2}, str.upper)
        {'A': 1, 'B': 2}
        >>> map_keys({1: 'a', 2: 'b'}, lambda x: x * 2)
        {2: 'a', 4: 'b'}
    """
    return {mapper(k): v for k, v in d.items()}