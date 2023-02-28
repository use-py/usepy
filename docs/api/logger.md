---
title: useLogger
outline: deep
---
# useLogger

`loguru`是一个十分优秀的日志库，但是大部分第三方库都是使用`logging`模块来进行日志记录的，当项目中同时使用了`loguru`和`logging`时，会导致日志记录混乱。

`useLogger`就是为了解决这个问题而生的，它可以将`logging`模块的日志记录转换为`loguru`的日志记录。并且能够统一格式输出。

当你在**项目入口处**使用`useLogger`后，你可以在任何地方使用`logging`/`loguru`模块来进行日志记录，它们统统会被无感转换为`loguru`的日志记录。


## 使用

```python
from usepy.logger import useLogger

useLogger() # 使用默认配置
```

如果你自身项目正在使用`loguru`，这一切似乎感觉毫无变化。因为默认的配置只是修改了一点输出样式。

如果想要感受它带来的“魔法”，需要稍微配置一下。

```python
from usepy.logger import useLogger

useLogger(packages=["scrapy", "django", "usepy"])
```
如果你在使用如`scrapy`/`django`等第三方库时，你会发现它们的日志记录也被统一了。

晚一些时候，这里会提供演示。

## Logstash/Filebeat

日志的更重要能力是将日志记录发送到`Logstash`/`Filebeat`，这样就可以将日志记录存储到`Elasticsearch`中，方便进行日志分析。所以统一日志的最终输出格式是非常重要的。

`useLogger`内置一个`logstash_handler`统一化输出格式。

```python{6}
from usepy import useTimeIt
from usepy.logger import useLogger, logstash_handler

useLogger(
    handlers=[
        logstash_handler(level="DEBUG", extra={"app_name": "spider"})
    ],
    packages=["usepy"],  # hook拦截 usepy 的日志
    extra={"project_name": "usepy"}
)

logger.warning("test warning")
logger.info("test info")
logger.debug("test debug")
# 这里测试调用函数的耗时，这是一个在usepy包中的函数
useTimeIt(lambda: logger.debug("start run test function"))()
```

运行结果：

![](https://miclon-job.oss-cn-hangzhou.aliyuncs.com/img/20230228222300.png)

有了以上输出，如果你使用过类似`filebeat`的工具，你就可以通过它自动收集docker的日志产物，发往`elasticsearch`中，方便进行日志分析。


## 另类模块

### uvicorn

`uvicorn`是一个非常优秀的`ASGI`服务器。它是`fastapi`的最佳拍档。它的日志拦截稍微特殊，我们将它单独拿出来。

```python
# app.py
from fastapi import FastAPI
from usepy.logger import useLoggerInterceptUvicorn

useLoggerInterceptUvicorn()  # 在 app 实例化前调用即可

app = FastAPI()

@app.get("/")
def home():
    return {"message": "hello"}
```

```python
# main.py
import uvicorn

uvicorn.run(app="app:app", host="127.0.0.1")
```

![](https://miclon-job.oss-cn-hangzhou.aliyuncs.com/img/20230228223646.png)

## 兼容性

`useLogger`兼容`loguru`和`logging`模块，你可以在任何地方使用它们来进行日志记录。

当你需要其他handler时，可以使用`loguru`的`add`方法来添加。

```python
from loguru import logger
from usepy.logger import useLogger

useLogger()

logger.add(
    "file_{time}.log",
    rotation="00:00",
    retention="10 days",
    enqueue=True,
    encoding="utf-8",
    level="DEBUG",
)
```

```text
# file_2023-02-28_22-26-56_570490.log
2023-02-28 22:26:56.590 | WARNING  | __main__:<module>:50 - test warning
2023-02-28 22:26:56.593 | INFO     | __main__:<module>:51 - test info
2023-02-28 22:26:56.593 | DEBUG    | __main__:<module>:52 - test debug
2023-02-28 22:26:56.593 | DEBUG    | __main__:<lambda>:53 - start run test function
2023-02-28 22:26:56.594 | DEBUG    | usepy.decorator.timeit:_timer:18 - <lambda> took 0 seconds
```
