---
outline: deep
---

::: info

    @Author: MicLon
    @Date: 2023/02/27
    @Description: 用于捕获函数执行中的异常，并进行debug

:::

## 使用

`@useExceptDebug`装饰器，用于捕获函数执行中的异常，并进行debug

```python
@useDecorator.except_debug
def error():
    1 / 0

error()  # ZeroDivisionError: division by zero
```
