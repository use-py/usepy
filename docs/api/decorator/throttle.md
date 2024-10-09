---
outline: deep
---

# throttle
限制函数调用频率的装饰器

```python
from usepy import throttle
````


### 参数

- `delay`: 允许再次调用的时间间隔（秒）

### 例子

```python
>>> import time
>>> 
>>> @throttle(delay=2)
... def print_message():
...     print("函数被调用")
>>> 
>>> print_message()
函数被调用
>>> print_message()  # 立即调用，不会执行
>>> time.sleep(2)
>>> print_message()
函数被调用
```

```

</rewritten_file>
