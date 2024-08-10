from typing import TypeVar, Sequence, Callable, Dict

T = TypeVar('T')


def count_by(arr: Sequence[T], mapper: Callable[[T], str]) -> Dict[str, int]:
    """
    Count the occurrences of each item in a sequence
    based on a transformation function.

    This function takes a sequence and a transformation function
    that converts each item in the sequence to a string. It then
    counts the occurrences of each transformed item and returns
    a dictionary with the transformed items as keys and the counts
    as values.

    Args:
        arr (Sequence[T]): The input sequence to count occurrences.
        mapper (Callable[[T], str]): The transformation function that maps each item to a string key.

    Returns:
        Dict[str, int]: A dictionary containing the transformed items as keys and the
        counts as values.
    """
    result: Dict[str, int] = {}

    for item in arr:
        key = mapper(item)
        result[key] = result.get(key, 0) + 1

    return result
