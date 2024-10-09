---
outline: deep
---

# without
返回一个新列表，排除指定的值。

```python
from usepy import without
```

### 参数

- `lst`: 源列表
- `*values`: 要排除的值

### 例子

```python
>>> without([1, 2, 3, 4, 5], 2, 4)
[1, 3, 5]
```
