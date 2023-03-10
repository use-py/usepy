# 插件

大部分基础较为常用的功能内置于`usepy`中，但是有一些功能并不是所有人都需要，所以我们将这些功能放在了插件中，这样可以保证`usepy`更加轻量化。



## 官方插件

### usepy-plugin-notify

`usepy-plugin-notify`是一个用于发送通知的插件，支持多种渠道的消息通知，并允许扩展新的消息通知渠道。


### 安装：

::: code-group

```bash [pip]
pip install "usepy[notify]"
``` 
```bash [poetry]
poetry add usepy --extras notify
``` 
:::


#### 支持的消息通知渠道列表

- Wechat
- Ding
- Bark
- Email
- Chanify
- Pushdeer
- Pushover


#### 使用方法

```python
from usepy import useNotify, useNotifyChannels

notify = useNotify()
notify.add(
    # Bark消息通知
    useNotifyChannels.Bark({"token": "xxxxxx"}),
    ...
)

notify.publish(title="usepy", content="usepy发布啦～")
```
