---
title: use-notify
outline: deep
---

# use-notify

::: code-group

```bash [pip]
pip install use-notify
```
```bash [poetry]
poetry add use-notify
```
:::

一个简单可扩展的消息通知库。

支持的消息通知渠道列表：

- Wechat
- Ding
- Bark
- Email
- Chanify
- Pushdeer
- Pushover

#### 使用

```python
from use_notify import useNotify, useNotifyChannels

notify = useNotify()
notify.add(
    # 添加多个通知渠道
    useNotifyChannels.Bark({"token": "xxxxxx"}),
    useNotifyChannels.Ding({
        "token": "xxxxx",
        "at_all": True
    })
)

notify.publish(title="消息标题", content="消息正文")

```


#### 自己开发消息通知

```python
from use_notify.useNotifyChannels import BaseChannel


class Custom(BaseChannel):
    """自定义消息通知"""

    def send(self, *args, **kwargs):
        ...
```
