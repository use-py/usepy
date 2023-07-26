---
outline: deep
---

::: info

    @Author: MicLon
    @Date: 2023/02/27
    @Description: 捕获函数执行中的异常

:::

## 使用

`@useCatchError`装饰器，用于捕获函数执行中的异常
  
```python
from usepy import useCatchError


@useCatchError()
def exception_demo():
    raise Exception('test')


@useCatchError(return_val='test')
def exception_demo2():
    raise Exception('test')


print(exception_demo())  # None
print(exception_demo2())  # 'test'
print("run to here")
```
