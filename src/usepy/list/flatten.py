from typing import TypeVar, List, Union, Optional

T = TypeVar("T")
D = TypeVar("D", int, float)


def flatten(lst: List[T], depth: D = 1) -> List[Union[T, List[T]]]:
    """
    Flattens an array up to the specified depth.

    Args:
        lst (List[T]): The array to flatten.
        depth (Optional[D], optional): The depth level specifying how deep a nested array structure should be flattened.
            If `float('inf')`, the array will be flattened completely. Defaults to 1.

    Returns:
        List[Union[T, List[T]]]: A new array that has been flattened.

    Examples:
        >>> flatten([1, [2, 3], [4, [5, 6]]],1)
        [1, 2, 3, 4, [5, 6]]

        >>> flatten([1, [2, 3], [4, [5, 6]]],2)
        [1, 2, 3, 4, 5, 6]

        >>> flatten([1, [2, [3, [4, [5]]]]], float('inf'))
        [1, 2, 3, 4, 5]
    """
    result: List[Union[T, List[T]]] = []
    floored_depth = depth

    def recursive(arr: List[T], current_depth: int) -> None:
        for item in arr:
            if isinstance(item, list) and current_depth < floored_depth:
                recursive(item, current_depth + 1)
            else:
                result.append(item)

    recursive(lst, 0)
    return result
