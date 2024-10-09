---
outline: deep
---

# get_function_name
获取当前函数的名称

```python
from usepy import get_function_name
```

### 返回值

- `str`: 当前函数的名称

### 例子

```python
>>> def outer():
...     def inner():
...         return get_function_name()
...     return inner()
>>> outer()
'inner'

>>> def example_function():
...     print(get_function_name())
>>> example_function()
example_function

>>> lambda_func = lambda: get_function_name()
>>> lambda_func()
'<lambda>'
