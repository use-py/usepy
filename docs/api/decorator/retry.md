---
outline: deep
---

# retry
为函数添加重试机制,支持异步函数

```python
from usepy import retry
````


### 参数

- `max_attempts`: 最大重试次数
- `retry_interval`: 重试间隔时间（秒）
- `retry_exceptions`: 需要重试的异常类型（可选）

### 例子

```python
>>> @retry(max_attempts=3, retry_interval=1)
... def unstable_function():
...     import random
...     if random.random() < 0.7:
...         raise ValueError("随机错误")
...     return "成功"
>>> 
>>> unstable_function()
'成功'
```
