---
outline: deep
---

# flatten_deep
将嵌套的列表完全展平。

```python
from usepy import flatten_deep
```

### 参数

- `lst`: 要完全展平的嵌套列表

### 例子

```python
>>> flatten_deep([1, [2, 3, [4, 5]], 6])
[1, 2, 3, 4, 5, 6]
```
