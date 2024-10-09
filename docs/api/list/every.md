---
outline: deep
---

# every
检查列表中的所有元素是否都满足指定条件。

```python
from usepy import every
```

### 参数

- `lst`: 要检查的列表
- `fn`: 用于检查的函数

### 例子

```python
>>> every([2, 4, 6, 8], lambda x: x % 2 == 0)
True
```
