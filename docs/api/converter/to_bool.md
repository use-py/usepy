---
outline: deep
---

# to_bool
将值转换为布尔类型

```python
from usepy import to_bool
```

### 参数

- `value`: 要转换的值

### 返回值

- `bool`: 转换后的布尔值

### 例子

```python
>>> to_bool(True)
True
>>> to_bool("True")
True
>>> to_bool("true")
True
>>> to_bool("t")
True
>>> to_bool(0)
False
>>> to_bool("false")
False
```
