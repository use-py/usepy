---
outline: deep
---

::: info

    @Author: MicLon
    @Date: 2023/02/19
    @Description: 用于转换数据类型的工具函数

:::



## string
将任意数据转换为字符串
```python
def string(data):
    """
    将任意数据转换为字符串
	:param data: data
	:return: string
    """
    ...
    
```


## md5
将字符数据转换为md5
```python
def md5(data: AnyStr) -> str:
    """
    将字符数据转换为md5
    :param data: data
    :return: md5
    """
    ...
```


## sha1
将字符数据转换为sha1
```python
def sha1(data: AnyStr) -> str:
    """
    将字符数据转换为sha1
    :param data: data
    :return: sha1
    """
    ...
```

## camel
将字符串转换为驼峰命名
```python
def camel(data: str, char: str = '-') -> str:
    """
    将字符数据转换为驼峰命名
    :param data: data
    :param char: 特征字符，如：-、_
    :return:
    >>> camel("test")
    'test'
    >>> camel("test-case")
    'testCase'
    >>> camel("test_case", char="_")
    'testCase'
    """
    ...
```

## snake
将字符串转换为下划线命名
```python
def snake(data: str, char: str = '_') -> str:
    """
    将字符数据转换为下划线命名
    :param data: data
    :param char: 特征字符，如：-、_
    :return:
    >>> snake("test")
    'test'
    >>> snake("testCase")
    'test_case'
    >>> snake("testCase", char="-")
    'test-case'
    """
    ...
```