<div align=center>
<img src="logo-shadow.svg" width="100" alt="logo">

`usepy`是一个简单易用的Python工具库，包含了一些常用的工具函数。

<a href="https://github.com/mic1on/usepy/actions/workflows/test.yml?query=event%3Apush+branch%3Amain" target="_blank">
    <img src="https://github.com/mic1on/usepy/workflows/test%20suite/badge.svg?branch=main&event=push" alt="Test">
</a>
<a href="https://pepy.tech/badge/usepy">
<img src="https://pepy.tech/badge/usepy" alt="Downloads"></a>
<a href="https://pypi.org/project/usepy" target="_blank">
    <img src="https://img.shields.io/pypi/v/usepy.svg" alt="Package version">
</a>

<a href="https://pypi.org/project/usepy" target="_blank">
    <img src="https://img.shields.io/pypi/pyversions/usepy.svg" alt="Supported Python versions">
</a>
</div>

### 安装

```bash
pip install usepy -U
```

### 示例及文档

[官方文档](https://usepy.code05.com/)

### 演示

- useAdDict

```python
from usepy import useAdDict

d = useAdDict(
    {'a': 1, 'b': 2, 'c': {'d': 3, 'e': 4}}
)
assert d.a == 1
assert d.c.e == 4
```

- useBloomFilter

```python
from redis import Redis
from usepy import useBloomFilter

rds = Redis(host='localhost', port=6379, db=0)
bf = useBloomFilter(client=rds)
bf.add('hi', 'miclon')
assert bf.exists('hi') is True
assert bf.exists('miclon') is True
assert bf.exists('python') is False
```

### 还有一些集成工具

- useNotify(消息通知)

```python
from usepy.integrations.useNotify import useNotify, useChannels

notify = useNotify()
notify.add(
    useChannels.Bark({"token": "jtgTe6****yj6DaepQ"}),
)

notify.publish(content="usepy")
```

更多参阅[官方文档](https://usepy.code05.com/)

## 贡献

欢迎提交PR，一起完善这个工具库。
