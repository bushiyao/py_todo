# coding=utf-8
# @Time : 2022/6/23 10:54 
# @Author : hh
# @File : bloom.py 
# @Software: PyCharm

import redis
import math


from pybloom_live import BloomFilter,ScalableBloomFilter

from redis import StrictRedis

try:
    import reload
except ImportError:
    pass


import os


B = 8
KB = B << 10
MB = KB << 10
GB = MB << 10


class PyBloomFilter():
    #内置100个随机种子
    SEEDS = [543, 460, 171, 876, 796, 607, 650, 81, 837, 545, 591, 946, 846, 521, 913, 636, 878, 735, 414, 372,
             344, 324, 223, 180, 327, 891, 798, 933, 493, 293, 836, 10, 6, 544, 924, 849, 438, 41, 862, 648, 338,
             465, 562, 693, 979, 52, 763, 103, 387, 374, 349, 94, 384, 680, 574, 480, 307, 580, 71, 535, 300, 53,
             481, 519, 644, 219, 686, 236, 424, 326, 244, 212, 909, 202, 951, 56, 812, 901, 926, 250, 507, 739, 371,
             63, 584, 154, 7, 284, 617, 332, 472, 140, 605, 262, 355, 526, 647, 923, 199, 518]

    #capacity是预先估计要去重的数量
    #error_rate表示错误率
    #conn表示redis的连接客户端
    #key表示在redis中的键的名字前缀
    def __init__(self, capacity=MB, error_rate=0.00000001, conn=None, key='BloomFilter'):
        self.m = math.ceil(capacity*math.log2(math.e)*math.log2(1/error_rate))      #需要的总bit位数
        self.k = math.ceil(math.log1p(2)*self.m/capacity)                           #需要最少的hash次数
        self.mem = math.ceil(self.m/8/1024/1024)                                    #需要的多少M内存
        self.blocknum = math.ceil(self.mem/512)                                     #需要多少个512M的内存块,value的第一个字符必须是ascii码，所有最多有256个内存块
        self.seeds = self.SEEDS[0:self.k]
        self.b = BloomFilter(capacity=capacity)
        # self.b = ScalableBloomFilter(initial_capacity=100)
        self.key = key
        self.N = 2**31-1
        if conn is None or isinstance(conn, str):
            self.redis = StrictRedis.from_url(conn)
        elif isinstance(conn, redis.Redis):
            self.redis = conn
        else:
            assert isinstance(conn, redis.Redis)
        # print(self.mem)
        # print(self.k)

    def add(self, value):
        name = self.key + "_" + str(ord(value[0]) % self.blocknum)
        hashs = self.get_hashs(value)
        for hash in hashs:
            self.redis.setbit(name, hash, 1)

    def is_exist(self, value):
        # return False
        name = self.key + "_" + str(ord(value[0]) % self.blocknum)
        hashs = self.get_hashs(value)
        exist = True
        for hash in hashs:
            exist = exist & self.redis.getbit(name, hash)
        return exist

    def get_hashs(self, value):
        return list(self.b.make_hashes(value.encode("utf-8")))

    def clear(self):
        """Clear bloom mem"""
        for blocknum in range(0, self.blocknum):
            self.redis.delete(self.key + "_" + str(blocknum))


def main():
    # bf = PyBloomFilter(capacity=1000000,conn='redis://:123456@127.0.0.1:6379/15')           # 利用连接池连接Redis
    bf = PyBloomFilter(capacity=1000000,conn='redis://127.0.0.1:6379/15')               # 利用连接池连接Redis
    for i in range(0, 1000):
        if i % 2 == 0:
            bf.add(str(i))
    bf.add('www.zhihu.com')               # 向Redis默认的通道添加一个域名
    bf.add('www.luyin.org')                 # 向Redis默认的通道添加一个域名
    print(bf.is_exist('www.zhihu.com'))     # 打印此域名在通道里是否存在，存在返回1，不存在返回0
    print(bf.is_exist('www.luyin.org'))     # 打印此域名在通道里是否存在，存在返回1，不存在返回0
    for i in range(1, 1000, 2):
        print(i, bf.is_exist(str(i)))
    for i in range(0, 1000, 3):
        print(i, bf.is_exist(str(i)))

if __name__ == '__main__':
    main()
