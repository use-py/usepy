---
outline: deep
---

# singleton
实现单例模式的装饰器

```python
from usepy import singleton
````


### 例子

```python
>>> @singleton
... class MyClass:
...     def __init__(self, value):
...         self.value = value
>>> 
>>> instance1 = MyClass(42)
>>> instance2 = MyClass(24)
>>> instance1.value
42
>>> instance1 is instance2
True
```
