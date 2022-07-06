# coding=utf-8
# @Time : 2022/7/6 16:09
# @Author : hh
# @File : redis.py
# @Software: PyCharm


#!/usr/bin/python3

import redis,time   # 导入redis模块，通过python操作redis 也可以直接在redis主机的服务端操作缓存数据库
import pickle

# decode_responses 如果是 True 标识使用字符串格式
pool = redis.ConnectionPool(host='127.0.0.1', port=6379, password="", decode_responses=False)   # host是redis主机，需要redis服务端和客户端都起着 redis默认端口是6379
r = redis.Redis(connection_pool=pool)

js = {"name":'Tom',"age":22}
print(js, type(js))
print(pickle.dumps(js), type(pickle.dumps(js)))
print(pickle.loads(pickle.dumps(js)))
'''
{'name': 'Tom', 'age': 22} <class 'dict'>
b'\x80\x04\x95\x1a\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x04name\x94\x8c\x03Tom\x94\x8c\x03age\x94K\x16u.' <class 'bytes'>
{'name': 'Tom', 'age': 22}
'''
print("\n\n")

data = r.zrange('ant_hrw_org_1:requests', 0, -1)
for d in data:
    print(d)
    print(pickle.loads(d))
    exit()
print(data)
'''
b'\x80\x05\x95K\x01\x00\x00\x00\x00\x00\x00}\x94(\x8c\x03url\x94\x8c,http://****/people\x94\x8c\x08callback\x94\x8c\x06parser\x94\x8c\x07errback\x94N\x8c\x06method\x94\x8c\x03GET\x94\x8c\x07headers\x94}\x94C\x07Referer\x94]\x94C http://****/people\x94as\x8c\x04body\x94C\x00\x94\x8c\x07cookies\x94}\x94\x8c\x04meta\x94}\x94(\x8c\x05title\x94\x8c\x0bJohn Fisher\x94\x8c\x08position\x94\x8c\x0fGeneva Director\x94\x8c\x05depth\x94K\x01u\x8c\t_encoding\x94\x8c\x05utf-8\x94\x8c\x08priority\x94K\x00\x8c\x0bdont_filter\x94\x89\x8c\x05flags\x94]\x94\x8c\tcb_kwargs\x94}\x94u.'

{
	'url': 'http://****/people',
	'callback': 'parser',
	'errback': None,
	'method': 'GET',
	'headers': {
		b 'Referer': [b 'http://****/people']
	},
	'body': b '',
	'cookies': {},
	'meta': {
		'title': 'John Fisher',
		'position': 'Geneva Director',
		'depth': 1
	},
	'_encoding': 'utf-8',
	'priority': 0,
	'dont_filter': False,
	'flags': [],
	'cb_kwargs': {}
}
'''

# r.set('name', 'phyger-from-python-redis')
# print(r['name'])
# print(r.get('name'))  # 取出键name对应的值
# print(type(r.get('name')))



