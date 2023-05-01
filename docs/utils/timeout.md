---
outline: deep
---

## useTimeoutFn

超时将会执行回调函数

```python
def callback():
    print("timeout")

timeout = useTimeoutFn(1, callback)
timeout.start()
# do something need 2 seconds
timeout.stop()

```


```python
def callback():
    print("timeout")

# 无需`start`立即生效
timeout = useTimeoutFn(1, callback, immediate = True)
# timeout.start()
# do something need 2 seconds

```

## useTimeout

超时

```python

timeout = useTimeout(0.1)
```
