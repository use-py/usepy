---
outline: deep
---

# chunk
将列表分割成指定大小的子列表。

```python
from usepy import chunk
```

### 参数

- `lst`: 要分割的列表
- `size`: 每个子列表的大小

### 例子

```python
>>> chunk([1, 2, 3, 4, 5], 2)
[[1, 2], [3, 4], [5]]
```
