# coding=utf-8
# @Time : 2022/7/21 15:57 
# @Author : hh
# @File : mergeSort.py 
# @Software: PyCharm

import math

def mergeSort(arr):
    if(len(arr) < 2):
        return arr

    middle = math.floor(len(arr) / 2)
    left, right = arr[0:middle], arr[middle:]
    # print('left: ', left)
    # print('right: ', right)
    return merge(mergeSort(left), mergeSort(right))

def merge(left, right):
    res = []
    while left and right:
        if left[0] <= right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))

    while left:
        res.append(left.pop(0))

    while right:
        res.append(right.pop(0))

    print(res)
    return res

print('end: ', mergeSort([1, 5, 2, 9, 6, 3, 8, 2]))