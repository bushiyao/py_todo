# coding=utf-8
# @Time : 2022/6/30 14:29 
# @Author : hh
# @File : escape_str.py 
# @Software: PyCharm

from pymysql.converters import escape_str

str = "halou ' do it"
st1 = 'halou do " it '

print(str)
print(escape_str(str))
# 'halou \' do it'
print(escape_str(st1))
# 'halou do \" it '
