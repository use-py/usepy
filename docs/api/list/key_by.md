---
outline: deep
---

# key_by
将列表转换为字典，使用指定的键函数生成键。

```python
from usepy import key_by
```

### 参数

- `lst`: 源列表
- `key_fn`: 用于生成键的函数

### 例子

```python
>>> key_by(['a', 'bb', 'ccc'], len)
{1: 'a', 2: 'bb', 3: 'ccc'}
```
