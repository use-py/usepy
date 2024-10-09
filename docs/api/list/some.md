---
outline: deep
---

# some
检查列表中是否存在至少一个元素满足指定条件。

```python
from usepy import some
```

### 参数

- `lst`: 要检查的列表
- `fn`: 用于检查的函数

### 例子

```python
>>> some([1, 2, 3, 4], lambda x: x > 3)
True
```
