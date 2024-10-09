---
outline: deep
---

# middle_batch
获取字符串中两个指定子串之间的多个部分

```python
from usepy import middle_batch
```

### 参数

- `original_str`: 原始字符串
- `start_str`: 开始子串（可选）
- `end_str`: 结束子串（可选）
- `max_count`: 最大返回数量（可选）

### 例子

```python
>>> middle_batch('abc123def456abc789def', 'abc', 'def')
['123', '789']
>>> middle_batch('abc123def456abc789def', 'abc', 'def', 1)
['123']
```
