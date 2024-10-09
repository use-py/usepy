---
outline: deep
---

# to_set
将值转换为集合

```python
from usepy import to_set
```

### 参数

- `value`: 要转换的值

### 返回值

- `set`: 转换后的集合

### 例子

```python
>>> to_set([1, 2, 2, 3])
{1, 2, 3}
>>> to_set("abcabc")
{'a', 'b', 'c'}
>>> to_set((1, 2, 3))
{1, 2, 3}
