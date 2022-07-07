# coding=utf-8
# @Time : 2022/7/7 14:38 
# @Author : hh
# @File : push_redis.py 
# @Software: PyCharm

#!/usr/bin/python3

import redis,time   # 导入redis模块，通过python操作redis 也可以直接在redis主机的服务端操作缓存数据库
import pickle
import json

# decode_responses 如果是 True 标识使用字符串格式
pool = redis.ConnectionPool(host='127.0.0.1', port=6379, password="", decode_responses=False)   # host是redis主机，需要redis服务端和客户端都起着 redis默认端口是6379
r = redis.Redis(connection_pool=pool)


tt = {"url":"http://baidu8.com", "dont_filter":True, "callback":"self.parse1"}
# tt1 = pickle.dumps(tt)
tt1 = json.dumps(tt)
res = r.lpush("test:start_urls", tt1)
print(res)
exit()