"""
reference
- https://github.com/LiuXingMing/Scrapy_Redis_Bloomfilter/blob/master/bloomfilterOnRedis.py
- https://github.com/MuggleK/CrawlersTools/blob/main/CrawlersTools/preprocess/bloom_filter.py
"""
from typing import Tuple

from .useTo import useToSHA1


class SimpleHash(object):

    def __init__(self, cap, seed):
        self.cap = cap
        self.seed = seed

    def hash(self, value):
        ret = 0
        for i in range(len(value)):
            ret += self.seed * ret + ord(value[i])
        return (self.cap - 1) & ret


class useBloomFilter(object):
    def __init__(self, client, key: str = "bloom_filter", block_num: int = 1):
        """
        :param client: Redis client
        :param key: Redis key
        :param block_num: 块数
        """
        self.client = client
        self.key = key
        self.bit_size = 1 << 31
        self.seeds = [5, 7, 11, 13, 31, 37, 61]
        self.block_num = block_num
        self.hash_func = []
        for seed in self.seeds:
            self.hash_func.append(SimpleHash(self.bit_size, seed))

    def exists(self, input_value: str) -> bool:
        """
        判断字符串是否存在
        :param input_value: 输入值
        :return: 是否存在
        """
        if not input_value:
            return False
        ret = True
        input_value = useToSHA1(input_value)
        name = f"{self.key}{int(input_value[0:2], 16) % self.block_num}"
        for f in self.hash_func:
            loc = f.hash(input_value)
            ret = ret & self.client.getbit(name, loc)
        return bool(ret)

    def _add(self, input_value: str):
        input_value = useToSHA1(input_value)
        name = f"{self.key}{str(int(input_value[0:2], 16) % self.block_num)}"
        for f in self.hash_func:
            loc = f.hash(input_value)
            self.client.setbit(name, loc, 1)

    def add(self, *input_value: Tuple[str]) -> None:
        """
        插入字符串
        :param input_value: 输入值
        :return:
        """
        for iv in input_value:
            self._add(iv)
