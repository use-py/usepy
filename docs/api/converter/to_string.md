---
outline: deep
---

# to_string
将值转换为字符串

```python
from usepy import to_string
```

### 参数

- `value`: 要转换的值

### 返回值

- `str`: 转换后的字符串

### 例子

```python
>>> to_string(123)
'123'
>>> to_string([1, 2, 3])
'1, 2, 3'
>>> to_string({"a": 1, "b": 2})
'a: 1, b: 2'
>>> to_string(None)
''
```
