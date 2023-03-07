---
title: useLogger
outline: deep
---
# useParser

解析器，提供了一些常用的方法。

## curl <Badge type="warning" text="useCURL" />

用于解析CURL命令。
```python
from usepy import useParser, useCURL

test_curl_command = """
curl 'http://localhost:3333/api/parser.html' \
  -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' \
  -H 'Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6' \
  -H 'Cache-Control: no-cache' \
  -H 'Connection: keep-alive' \
  -H 'Cookie: Pycharm-fe1126fc=eb62da0d-7fad-4f5f-9396-37ee80df090c; csrftoken=SIf8rv13bnXYAarsi6aN6mpuHHZBjzKTBADTtouFI5U28Na8l9TFu9IFROY1auqH' \
  -H 'Pragma: no-cache' \
  -H 'Sec-Fetch-Dest: document' \
  -H 'Sec-Fetch-Mode: navigate' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'Sec-Fetch-User: ?1' \
  -H 'Upgrade-Insecure-Requests: 1' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76' \
  -H 'sec-ch-ua: "Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"' \
  --compressed
"""
# curl = useParser.curl(test_curl_command)
curl = useCURL(test_curl_command)
print(curl.url) # http://localhost:3333/api/parser.html
print(curl.method)  # GET
print(curl.data)  # None
print(curl.headers) # ...
print(curl.cookies) # ...
```


## useURL

用于解析URL。

```python
from usepy import useURL

url = useURL("https://www.google.com/search?q=usepy&ie=utf-8")
```


| url.scheme |   url.netloc   |    url.query     |       Coourl.query_dictl        | url.path |
| ---------- | :------------: | :--------------: | :-----------------------------: | -------: |
| https      | www.google.com | q=usepy&ie=utf-8 | `{'q': 'usepy', 'ie': 'utf-8'}` |  /search |
