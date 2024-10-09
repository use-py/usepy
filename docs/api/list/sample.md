---
outline: deep
---

# sample
从列表中随机选择指定数量的唯一元素。

```python
from usepy import sample
```

### 参数

- `lst`: 源列表
- `n`: 要选择的元素数量

### 例子

```python
>>> sample([1, 2, 3, 4, 5], 3)
[4, 1, 5]  # 结果可能会不同，因为是随机选择
```
