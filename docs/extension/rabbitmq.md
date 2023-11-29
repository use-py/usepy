---
title: use-rabbitmq
outline: deep
---

# use-rabbitmq

::: code-group

```bash [pip]
pip install use-rabbitmq
```
```bash [poetry]
poetry add use-rabbitmq
```
:::

一个永不断线的RabbitMQ连接管理


### example

```python
from use_rabbitmq import useRabbitMQ

rmq = useRabbitMQ()


@rmq.listener(queue_name="test")
def test_listener(message):
    print(message.body)
    message.ack()  # ack message
```

if you use it with [usepy](https://github.com/use-py/usepy), you can use it like this:

```python
from usepy.plugin import useRabbitMQ

rmq = useRabbitMQ()
```
