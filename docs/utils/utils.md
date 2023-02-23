---
outline: deep
---

::: info

    @Author: MicLon
    @Date: 2023/02/19
    @Description: 一些其他工具集合

:::



## cookie_to_dict
将字符串cookie转换为字典
```python
def cookie_to_dict(cookies):
    """
    将字符串cookie转换为字典
	:param cookies: cookie字符串
	:return: dict
    """
    ...
    
```
## data_to_dict
将字符串data转换为字典
```python
def data_to_dict(data):
    """
    将字符串data转换为字典
	:param data: data字符串。格式为`key1=value1&key2=value2`
	:return: dict
    """
    ...
    
```
## gen_unique_id
生成唯一id
```python
def gen_unique_id():
    """
    生成唯一id
	:return:
    """
    ...
    
```
## headers_to_dict
将字符串headers转换为字典
```python
def headers_to_dict(headers):
    """
    将字符串headers转换为字典
	:param headers: headers字符串
	:return: dict
    """
    ...
    
```
## uuid4
Generate a random UUID.
```python
def uuid4():
    """
    Generate a random UUID.
    """
    ...
    
```

## clean_html <Badge type="tip" text="useCleanHtml" />

```python
def clean_html(html: str, white_tags=None) -> str:
    """
    清除HTML标签
    >>> clean_html('<p>This is a paragraph.</p><br><strong>This is bold text.</strong>')
    'This is a paragraph.This is bold text.'
    """
    ...
```
