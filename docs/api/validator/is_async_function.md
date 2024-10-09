---
outline: deep
---

# is_async_function
检查给定的函数是否为异步函数

```python
from usepy import is_async_function
```

### 参数

- `func`: 要检查的函数

### 例子

```python
>>> import asyncio
>>> async def async_func():
...     await asyncio.sleep(1)
>>> def sync_func():
...     pass
>>> is_async_function(async_func)
True
>>> is_async_function(sync_func)
False
>>> is_async_function(lambda x: x)
False
```
