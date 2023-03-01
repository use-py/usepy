---
outline: deep
---

::: info

    @Author: MicLon
    @Date: 2023/03/01
    @Description: url操作

:::


## useURL

```python
from usepy import useURL

url = useURL("https://www.google.com/search?q=usepy&ie=utf-8")
```


| url.scheme |   url.netloc   |    url.query     |       Coourl.query_dictl        | url.path |
| ---------- | :------------: | :--------------: | :-----------------------------: | -------: |
| https      | www.google.com | q=usepy&ie=utf-8 | `{'q': 'usepy', 'ie': 'utf-8'}` |  /search |
