---
outline: deep
---

:::tip
python中的字典数据结构的功能扩展
:::

## useAdDict

用于解决字典取值繁琐的问题。

```python
from usepy import useAdDict

d = useAdDict({'a': 1, 'b': 2, 'c': {'d': 3, 'e': 4}})
assert d.a == 1
assert d.c.e == 4
```
## useDict

扩展字典，提供了一些常用的方法。

### find_keys

查找字典中所有的key，返回一个列表。
```python
def find_keys(original_dict: dict, val: any) -> list:
    """
    查找字典中指定值的所有键
    :param original_dict: 原始字典
    :param val: 指定值
    :return: 键列表
    >>> UseDict.find_keys({'a': 1, 'b': 2, 'c': 3}, 2)
    ['b']
    """
    return list(key for key, value in original_dict.items() if value == val)
```
### reverse

反转字典，key和value互换。

```python
def reverse(original_dict: dict) -> dict:
    """
    反转字典
    :param original_dict: 原始字典
    :return: 反转后的字典
    >>> UseDict.reverse({'a': 1, 'b': 2, 'c': 3})
    {1: 'a', 2: 'b', 3: 'c'}
    """
    return {v: k for k, v in original_dict.items()}
```


### sort_by_key

按照key排序。

```python
def sort_by_key(original_dict: dict, az: bool = False) -> dict:
    """
    按键排序
    :param original_dict: 原始字典
    :param az: 是否升序 True: 升序 False: 降序
    :return: 排序后的字典
    >>> UseDict.sort_by_key({'c': 1, 'b': 2, 'a': 3})
    {'a': 3, 'b': 2, 'c': 1}
    """
    return dict(sorted(original_dict.items(), reverse=az))
```


### sort_by_value

按照value排序。

```python
def sort_by_value(original_dict: dict, az: bool = False) -> dict:
    """
    按值排序
    :param original_dict: 原始字典
    :param az: 是否升序 True: 升序 False: 降序
    :return: 排序后的字典
    >>> UseDict.sort_by_value({'c': 1, 'b': 2, 'a': 3})
    {'c': 1, 'b': 2, 'a': 3}
    """
    return dict(sorted(original_dict.items(), key=lambda x: x[1], reverse=az))
```

### arrays_to_dict

将数组转换为字典。

```python
def arrays_to_dict(keys: List, values: List) -> Dict:
    """
    将两个数组转换为字典
    :param keys: 键列表
    :param values: 值列表
    :return: 字典
    >>> UseDict.arrays_to_dict(['a', 'b', 'c'], [1, 2, 3])
    {'a': 1, 'b': 2, 'c': 3}
    """
    return dict(zip(keys, values))
```

### merge

合并字典。

```python
def merge(*dicts: Dict) -> Dict:
    """
    合并字典
    :param dicts: 字典列表
    :return: 合并后的字典
    >>> UseDict.merge({'a': 1}, {'b': 2}, {'c': 3})
    {'a': 1, 'b': 2, 'c': 3}
    """
    return {k: v for d in dicts for k, v in d.items()}
```

### merge_values

合并字典的值。

```python
def merge_values(*dicts: Dict) -> Dict:
    """
    合并字典，相同的key合并为数组
    :param dicts: 字典列表
    :return: 合并后的字典
    >>> UseDict.merge_values({'a': 1, 'b': 'foo', 'c': 400}, {'a': 3, 'b': 200, 'd': 400})
    {'a': [1, 3], 'b': ['foo', 200], 'c': [400], 'd': [400]}
    """
    res = defaultdict(list)
    for d in dicts:
        for key in d:
            res[key].append(d[key])
    return dict(res)
```
