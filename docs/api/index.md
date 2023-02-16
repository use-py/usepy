---
outline: deep
---

# Data

python中的数据结构的功能扩展


## useAdDict

用于解决字典取值繁琐的问题。

```python
from usepy.data import useAdDict

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


## useList

扩展列表，提供了一些常用的方法。

### split

将列表按照指定长度分割。

```python
def split(origin_list: List, n: int) -> Generator[List, None, None]:
    """
    按指定数量平均分割列表
    :param origin_list: 原始列表
    :param n: 指定数量
    :return: 分割后的列表

    >>> list(UseList.split([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """
    for i in range(0, len(origin_list), n):
        yield origin_list[i:i + n]
```

### objs_to_obj

将对象列表转换为字典。

```python
def objs_to_obj(arr: List[Dict], key: str) -> Dict:
    """
    将对象列表转换为指定key名的对象
    :param arr: 对象列表
    :param key: 指定key名
    :return: 指定key名的对象

    >>> UseList.objs_to_obj([{'id': 1, 'name': 'miclon'}, {'id': 2, 'name': 'miclon2'}], 'id')
    {1: {'id': 1, 'name': 'miclon'}, 2: {'id': 2, 'name': 'miclon2'}}
    """
    return {b[key]: b for b in arr}
```


### dedupe

列表去重，保持顺序

```python
def dedupe(items: List, key: Optional[Callable] = None):
    """
    列表去重，保持顺序
    >>> list(UseList.dedupe([1, 5, 2, 1, 9, 1, 5, 10]))
    [1, 5, 2, 9, 10]
    >>> list(UseList.dedupe([{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}], key=lambda d: (d['x'], d['y'])))
    [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 2, 'y': 4}]
    """
    seen = set()
    for item in items:
        value = item if key is None else key(item)
        if value not in seen:
            yield item
            seen.add(value)
```

### sort_bubble

冒泡排序。

```python
def sort_bubble(collection: List) -> List:
    """
    冒泡排序
    :param collection: 待排序数组
    :return: 排序后数组
    """
    for i in range(len(collection) - 1):
        for j in range(len(collection) - 1 - i):
            if collection[j] > collection[j + 1]:
                collection[j], collection[j + 1] = collection[j + 1], collection[j]
    return collection
```

### sort_quick

快速排序。

```python
def sort_quick(collection: List) -> List:
    """
    快速排序
    :param collection: 待排序数组
    :return: 排序后数组

    >>> UseList.sort_quick([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> UseList.sort_quick([])
    []
    >>> UseList.sort_quick([-2, 5, 0, -45])
    [-45, -2, 0, 5]
    """
    if len(collection) < 2:
        return collection
    pivot = collection.pop()
    greater: List[int] = []
    lesser: List[int] = []
    for element in collection:
        (greater if element > pivot else lesser).append(element)
    return UseList.sort_quick(lesser) + [pivot] + UseList.sort_quick(greater)
```

### sort

排序。

```python
def sort(collection: List, algorithm='bubble') -> List:
    """
    排序
    :param collection: 待排序数组
    :param algorithm: 排序算法, 默认冒泡排序
    :return: 排序后数组
    """
    name = f'sort_{algorithm}'
    if hasattr(UseList, name):
        return getattr(UseList, name)(collection)
    else:
        raise Exception('algorithm not found')
```

### sort_by_list

按指定列表排序，前者列表 按 后者列表排序

```python
def sort_by_list(collection: List, sort_list: List) -> List:
    """
    按指定列表排序，前者列表 按 后者列表排序
    :param collection: 待排序数组
    :param sort_list: 指定排序列表
    :return: 排序后数组

    >>> UseList.sort_by_list([1, 2, 3, 4, 5], [5, 4, 3, 2, 1])
    [5, 4, 3, 2, 1]
    >>> UseList.sort_by_list(['blue', 'green', 'orange', 'purple', 'yellow'], [3, 2, 5, 4, 1])
    ['yellow', 'green', 'blue', 'purple', 'orange']
    """
    return [val for (_, val) in sorted(zip(sort_list, collection), key=lambda x: x[0])]
```

## useString

扩展字符串，提供了一些常用的方法。

### to_str

将对象转换为字符串。

```python
def to_str(s, encoding=None, errors='strict'):
    """
    将 bytes 或者 bytearray 转换为 str
    :param s: bytes 或者 bytearray
    :param encoding: 编码
    :param errors: 错误处理
    :return: str
    """
    if isinstance(s, str):
        return s
    if not isinstance(s, (bytes, bytearray)):
        return str(s)
    return s.decode(encoding or 'utf-8', errors)
```


### to_bytes

将对象转换为bytes。

```python
def to_bytes(s, encoding=None, errors='strict'):
    """
    将 str 转换为 bytes
    :param s: str
    :param encoding: 编码 
    :param errors: 错误处理
    :return: bytes
    """
    if isinstance(s, bytes):
        return s
    if not isinstance(s, str):
        return bytes(s)
    return s.encode(encoding or 'utf-8', errors)
```


### random

生成随机字符串。

```python
def random(min_len=3, max_len=20, characters=None):
    """
    生成随机字符串
    :param min_len: 最小长度
    :param max_len: 最大长度
    :param characters: 字符集
    :return: 随机字符串
    """
    characters = characters or _characters
    _len = randint(min_len, max_len) if max_len > min_len else min_len
    return ''.join((choice(characters) for _ in range(_len)))
```


### get_middle

获取字符串中间的内容。

```python
def get_middle(
        original_str: str,
        start_str: str,
        end_str: str
) -> Optional[str]:
    """
    获取字符串中间内容
    :param original_str: 原始字符串
    :param start_str: 开始字符串
    :param end_str: 结束字符串
    :return: 中间内容
    >>> UseString.get_middle('abc123def', 'abc', 'def')
    '123'
    """
    find_str, _, _ = UseString._get_section(original_str, start_str, end_str)
    return find_str
```


### get_middle_batch

批量获取字符串中间的内容，返回列表。

```python
def get_middle_batch(
        original_str: str,
        start_str: str,
        end_str: str
) -> list:
    """
    获取字符串中间内容
    :param original_str: 原始字符串
    :param start_str: 开始字符串
    :param end_str: 结束字符串
    :return: 中间内容
    >>> UseString.get_middle_batch('abc123def456abc789def', 'abc', 'def')
    ['123', '789']
    """
    result = []
    while True:
        find_str, start_, end_ = UseString._get_section(original_str, start_str, end_str)
        if find_str is None:
            break
        result.append(find_str)
        original_str = original_str[end_:]
    return result
```


### get_left

获取字符串左边的内容。

```python
def get_left(
        original_str: str,
        end_str: str
) -> Optional[str]:
    """
    获取字符串左边内容
    :param original_str: 原始字符串
    :param end_str: 结束字符串
    :return: 左边内容
    >>> UseString.get_left('abc123def', 'def')
    'abc123'
    """
    find_str, _, _ = UseString._get_section(original_str, end_str=end_str)
    return find_str
```


### get_right

获取字符串右边的内容。

```python
def get_right(
        original_str: str,
        start_str: str
) -> Optional[str]:
    """
    获取字符串右边内容
    :param original_str: 原始字符串
    :param start_str: 开始字符串
    :return: 右边内容
    >>> UseString.get_right('abc123def', 'abc')
    '123def'
    """
    find_str, _, _ = UseString._get_section(original_str, start_str=start_str)
    return find_str
```


### uuid

生成uuid。

```python
@staticmethod
def uuid():
    return f"{uuid4().hex}"
```


### reverse

反转字符串。

```python
def reverse(original_str: str) -> str:
    """
    反转字符串
    :param original_str: 原始字符串
    :return: 反转后字符串
    >>> UseString.reverse('abc')
    'cba'
    """
    return original_str[::-1]
```


### encode

自定义秘密加密字符串。

```python
def encode(original_str: str, key: str) -> str:
    """
    加密字符串
    :param original_str: 原始字符串
    :param key: 密钥
    :return: 加密后字符串
    """
    encoded_chars = []
    for i in range(len(original_str)):
        key_c = key[i % len(key)]
        encoded_c = chr(ord(original_str[i]) + ord(key_c) % 256)
        encoded_chars.append(encoded_c)
    encoded_string = "".join(encoded_chars)
    return base64.urlsafe_b64encode(encoded_string.encode('utf-8')).decode('utf-8')
```


### decode

自定义密码解密字符串。

```python
def decode(original_str: str, key: str) -> str:
    """
    解密字符串
    :param original_str: 原始字符串
    :param key: 密钥
    :return: 解密后字符串
    """
    decoded_chars = []
    original_str = base64.urlsafe_b64decode(original_str).decode('utf-8')
    for i in range(len(original_str)):
        key_c = key[i % len(key)]
        decoded_c = chr((ord(original_str[i]) - ord(key_c) + 256) % 256)
        decoded_chars.append(decoded_c)
    decoded_string = "".join(decoded_chars)
    return decoded_string
```
