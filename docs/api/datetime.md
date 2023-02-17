---
outline: deep
---

:::tip
python中的日期时间的功能扩展
:::

## useDatetime


### timestamp

获取当前时间戳。

```python
def timestamp(dt: Optional[datetime] = None, digit: int = 10) -> int:
    """
    获取当前时间戳，默认10位
    :param dt: 时间，默认当前时间
    :param digit: 位数
    :return: 时间戳

    >>> UseDateTime.timestamp()
    1600000000
    >>> UseDateTime.timestamp(digit=13)
    1600000000000
    """
    ...
```


### format

格式化时间。

```python
def format(dt: datetime, fmt=None) -> str:
    """
    格式化时间
    :param dt:
    :param fmt: 时间格式
    :return: 时间
    """
    ...
```


### format_now

格式化当前时间。

```python
def format_now(fmt=None) -> str:
    """
    格式化当前时间
    :param fmt: 时间格式
    :return: 时间
    """
    ...
```

### format_before

格式化之前的时间。

```python
def format_before(nums, unit=None, fmt=None) -> str:
    """
    获取指定单位的时间
    :param nums: 数量
    :param unit: 单位，支持：days[默认], seconds, microseconds, milliseconds, minutes, hours, weeks
    :param fmt: 时间格式
    :return: 时间
    """
    ...
```

### format_after

格式化之后的时间。

```python
def format_after(nums, unit=None, fmt=None) -> str:
    """
    获取指定单位的时间
    :param nums: 数量
    :param unit: 单位，支持：days[默认], seconds, microseconds, milliseconds, minutes, hours, weeks
    :param fmt: 时间格式
    :return: 时间
    """
    ...
```

### parse

解析时间，将字符串转换为时间。

内置多种时间格式，可自定义时间格式。

```python
def parse(dt: str, fmt=None) -> datetime:
    """
    解析时间
    :param dt: 时间
    :param fmt: 时间格式
    :return: 时间
    """
    ...
```
