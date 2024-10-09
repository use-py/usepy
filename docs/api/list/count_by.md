---
outline: deep
---

# count_by
根据指定的函数对列表元素进行计数。

```python
from usepy import count_by
```

### 参数

- `lst`: 要计数的列表
- `fn`: 用于分类的函数

### 例子

```python
>>> count_by([1.2, 2.3, 3.4, 4.5], math.floor)
{1: 1, 2: 1, 3: 1, 4: 1}
```
