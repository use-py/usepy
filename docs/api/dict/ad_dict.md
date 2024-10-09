---
outline: deep
---

# ad_dict
创建一个允许使用点号访问的字典

```python
from usepy import ad_dict
```

### 参数

- `data`: 初始化字典数据(可选)

### 例子

```python
>>> d = ad_dict({'a': 1, 'b': {'c': 2}})
>>> d.a
1
>>> d.b.c
2
>>> d.d = 3
>>> d
{'a': 1, 'b': {'c': 2}, 'd': 3}
```
