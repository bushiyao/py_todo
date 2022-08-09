# coding=utf-8
# @Time : 2022/8/9 14:29 
# @Author : hh
# @File : json.py 
# @Software: PyCharm

import json

data = {
    'name': 'Jack',
    'age': 32,
    'vip': True,
    'address': {'province':'bj', 'city':'hd'}
}
print(data, data['age'], data['vip'], type(data))

dataJson = json.dumps(data)
print(dataJson, type(dataJson))

dataDict = json.loads(dataJson)
print(dataDict, type(dataDict))

'''
{'name': 'Jack', 'age': 32, 'vip': True, 'address': {'province': 'bj', 'city': 'hd'}} 32 True <class 'dict'>
{"name": "Jack", "age": 32, "vip": true, "address": {"province": "bj", "city": "hd"}} <class 'str'>
{'name': 'Jack', 'age': 32, 'vip': True, 'address': {'province': 'bj', 'city': 'hd'}} <class 'dict'>
'''
