# Decorator

python中常用的装饰器。

## useSingleton

`@useSingleton`单例模式装饰器，同样适用于多线程环境下。

```python
@useDecorator.singleton
class A:
    pass

a = A()
b = A()
assert a is b  # pass
```

## useTimeIt

`@useTimeIt`装饰器，用于统计函数执行时间

```python
@useDecorator.timeit
def test():
    time.sleep(1)

test()  # test took 1.000 seconds
```

## useCatchError
  
  `@useCatchError`装饰器，用于捕获函数执行中的异常
  
  ```python
@useDecorator.catch_error()
def exception_demo():
    raise Exception('test')


@useDecorator.catch_error(return_val='test')
def exception_demo2():
    raise Exception('test')

exception_demo()  # None
exception_demo2()  # 'test'
print("run to here")

```


## useExceptDebug

`@useExceptDebug`装饰器，用于捕获函数执行中的异常，并进行debug

```python
@useDecorator.except_debug
def error():
    1 / 0

error()  # ZeroDivisionError: division by zero
```

## useRunInThread
  
  `@useRunInThread`装饰器，用于将函数放入线程中执行
  
  ```python
@useDecorator.run_in_thread
def run_in_thread():
    time.sleep(1)
    print('run_in_thread')

# 同时执行3个线程
for i in range(3):
    run_in_thread()
```

## useListify

`@useListify`将函数的返回值转换为列表。

```python
@useDecorator.listify()
def listify():
    yield 1


@useDecorator.listify(collection=set)
def listify2():
    yield 1
    yield 2
    yield 2


@useDecorator.listify(collection=dict)
def listify3():
    yield 1, 2
    yield 2, 3
    yield 2, 4


listify()  # [1]
listify2()  # {1, 2}
listify3()  # {1: 2, 2: 3}
```
