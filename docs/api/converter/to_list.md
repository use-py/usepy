---
outline: deep
---

# to_list
将值转换为列表

```python
from usepy import to_list
```

### 参数

- `value`: 要转换的值

### 返回值

- `list`: 转换后的列表

### 例子

```python
>>> to_list([1, 2, 3])
[1, 2, 3]
>>> to_list("abc")
['a', 'b', 'c']
>>> to_list(123)
[123]
>>> to_list((1, 2, 3))
[1, 2, 3]
