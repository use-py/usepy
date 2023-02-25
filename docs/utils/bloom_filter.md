---
outline: deep
---

::: info

    @Author: MicLon
    @Date: 2023/02/25
    @Description: 布隆过滤器

:::


## 介绍

布隆过滤器是一种空间效率很高的随机数据结构，它可以用来告诉你，一个元素是否在一个集合中。它的优点是空间效率和查询时间都远远超过一般的算法，缺点是有一定的误识别率和删除困难。

参考：[布隆过滤器](https://www.cnblogs.com/cpselvis/p/6265825.html)

## 使用

```python{2}
from redis import Redis
from usepy import useBloomFilter


rds = Redis(host='localhost', port=6379, db=0)
bf = useBloomFilter(
    client=rds
)
bf.add('hello')
bf.add('world')
print(bf.exists('hello')) # True
print(bf.exists('world')) # True
print(bf.exists('python')) # False
print(bf.exists('')) # False
