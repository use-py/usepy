---
outline: deep
---

# catch_error
捕获函数执行过程中的错误并返回指定值

```python
from usepy import catch_error
````


### 参数

- `return_val`: 发生异常时返回的值（可选）

### 例子

```python
>>> import logging
>>> logging.basicConfig(level=logging.DEBUG)
>>> 
>>> @catch_error(return_val=0)
... def divide(a, b):
...     return a / b
>>> 
>>> divide(10, 2)
5.0
>>> divide(10, 0)
0
```
