from typing import Dict


def merge_dicts(*dicts: Dict) -> Dict:
    """merge dicts

    Args:
        dicts (Dict): The dicts to merge.

    Returns:
        Dict: The merged dict.

    Examples:
        >>> merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
        {'a': 1, 'b': 3, 'c': 4}
    """
    result = {}
    for d in dicts:
        result.update(d)
    return result
