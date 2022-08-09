# coding=utf-8
# @Time : 2022/8/9 14:20 
# @Author : hh
# @File : binarySearch.py 
# @Software: PyCharm

def binary_search(data, item):
    count = len(data)
    if count > 0:
        middle = count // 2
        if data[middle] == item:
            return True
        elif data[middle] > item:
            return binary_search(data[:middle], item)
        else:
            return binary_search(data[middle+1:], item)

    return False

list = [1, 4, 10, 21, 33, 66, 100, 198, 234, 455, 555]
d = binary_search(list, 999)
e = binary_search(list, 234)
print(e)