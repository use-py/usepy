---
title: use-redis
outline: deep
---

# use-redis

::: code-group

```bash [pip]
pip install use-redis
```
```bash [poetry]
poetry add use-redis
```
:::

一个永不断线的Redis连接管理


### example

```python
from use_redis import useRedis

rds = useRedis()
```

if you use it with [usepy](https://github.com/use-py/usepy), you can use it like this:

```python
from usepy.plugin import useRedis

rds = useRedis()
```
