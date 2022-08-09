# coding=utf-8
# @Time : 2022/7/22 10:14 
# @Author : hh
# @File : date.py
# @Software: PyCharm

import time
import datetime

# time ----------------------------------

str = '2022-07-22 12:13'

tt1 = time.strptime(str, '%Y-%m-%d %H:%M')
print('tt1: ', tt1)
# time.struct_time(tm_year=2022, tm_mon=7, tm_mday=22, tm_hour=12, tm_min=13, tm_sec=0, tm_wday=4, tm_yday=203, tm_isdst=-1)

tt2 = time.mktime(tt1)
print("tt2: ", tt2)
# 1658463180.0

tt3 = time.localtime(int(tt2))
print("tt3: ", tt3)
# time.struct_time(tm_year=2022, tm_mon=7, tm_mday=22, tm_hour=12, tm_min=13, tm_sec=0, tm_wday=4, tm_yday=203, tm_isdst=0)

last = time.strftime('%Y-%m-%d %H:%M:%S', tt3)
print("last: ", last)
# 2022-07-22 12:13:00


# datetime ----------------------------------------
print("\n\ndatetime-------------------- \n\n")

td1 = datetime.datetime.now()
print('td1: ', td1)

td2 = td1.strftime("%Y-%m-%d %H:%M:%S")
print("td2: ", td2)

td3 = td1 - datetime.timedelta(days=1)
print("td3: ", td3)

print('yesterday the daty is: ', td3.day)
'''
td1:  2022-07-22 11:00:57.909364
td2:  2022-07-22 11:00:57
td3:  2022-07-21 11:00:57.909364
yesterday the daty is  21
'''

