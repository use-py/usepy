---
outline: deep
---

# compact
将列表压缩。

```python
from usepy import compact
```

### 参数

- `lst`: 列表

### 例子

```python
>>> compact([0, 1, False, 2, '', 3, None, 4, {}, 5])
[1, 2, 3, 4, 5]
```
