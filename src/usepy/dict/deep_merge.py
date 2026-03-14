from typing import Dict, Any
import copy


def deep_merge(*dicts: Dict[str, Any]) -> Dict[str, Any]:
    """
    Deeply merges multiple dictionaries.

    Nested dictionaries are merged recursively. Other values are overwritten.

    Args:
        *dicts (Dict[str, Any]): The dictionaries to merge.

    Returns:
        Dict[str, Any]: A new deeply merged dictionary.

    Examples:
        >>> deep_merge({'a': {'b': 1}}, {'a': {'c': 2}})
        {'a': {'b': 1, 'c': 2}}
        >>> deep_merge({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
        {'a': 1, 'b': 3, 'c': 4}
        >>> deep_merge({'a': [1, 2]}, {'a': [3, 4]})
        {'a': [3, 4]}
    """
    if not dicts:
        return {}

    result = copy.deepcopy(dicts[0])

    for d in dicts[1:]:
        for key, value in d.items():
            if (
                key in result
                and isinstance(result[key], dict)
                and isinstance(value, dict)
            ):
                result[key] = deep_merge(result[key], value)
            else:
                result[key] = copy.deepcopy(value)

    return result