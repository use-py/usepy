---
outline: deep
---

# sort_by_key
根据字典的key排序

```python
from usepy import sort_by_key
```

### 参数

- `original_dict`: 要排序的字典
- `az`: 排序方式，默认为True，表示升序

### 例子

```python
>>> sort_by_key({'c': 1, 'b': 2, 'a': 3})
{'a': 3, 'b': 2, 'c': 1}
```
