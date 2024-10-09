---
outline: deep
---

# shuffle
随机打乱列表中的元素顺序。

```python
from usepy import shuffle
```

### 参数

- `lst`: 要打乱的列表

### 例子

```python
>>> lst = [1, 2, 3, 4, 5]
>>> shuffle(lst)
>>> lst
[3, 1, 4, 5, 2]  # 结果可能会不同，因为是随机打乱
```
