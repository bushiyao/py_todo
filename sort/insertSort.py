# coding=utf-8
# @Time : 2022/7/21 15:46 
# @Author : hh
# @File : insertSort.py 
# @Software: PyCharm


'''
steps:
1\ 将第一待排序序列第一个元素看做一个有序序列，把第二个元素到最后一个元素当成是未排序序列。
2\ 从头到尾依次扫描未排序序列，将扫描到的每个元素插入有序序列的适当位置.
'''

# insert sort
def insertSort(arr):
    for i in range(len(arr)):
        prevX = i - 1
        cur = arr[i]
        while prevX >= 0 and arr[prevX] > cur:
            arr[prevX + 1] = arr[prevX]
            prevX -= 1
        arr[prevX + 1] = cur
        print(arr)

    return arr

print('end: ', insertSort([1, 5, 2, 9, 6, 3, 8, 2]))
