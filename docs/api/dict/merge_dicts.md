---
outline: deep
---

# merge_dicts
合并多个字典

```python
from usepy import merge_dicts
```

### 参数

- `*dicts`: 要合并的字典(可变参数)

### 例子

```python
>>> merge_dicts({'a': 1, 'b': 2}, {'c': 3}, {'d': 4})
{'a': 1, 'b': 2, 'c': 3, 'd': 4}
```
