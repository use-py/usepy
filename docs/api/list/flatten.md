---
outline: deep
---

# flatten
将嵌套的列表展平一层。

```python
from usepy import flatten
```

### 参数

- `lst`: 要展平的嵌套列表

### 例子

```python
>>> flatten([1, [2, 3, [4, 5]], 6])
[1, 2, 3, [4, 5], 6]
```
