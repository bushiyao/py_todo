# coding=utf-8
# @Time : 2022/7/21 15:40 
# @Author : hh
# @File : selectSort.py 
# @Software: PyCharm

'''
steps:
1\ 首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置
2\ 再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
3\ 重复第二步，直到所有元素均排序完毕。
'''

# select sort
def selectSort(arr):

    for i in range(len(arr) - 1):
        mx = i
        for j in range(i + 1, len(arr)):
            if arr[mx] > arr[j]:
                mx = j
        arr[i], arr[mx] = arr[mx], arr[i]
        print(arr)

    return arr

print('end: ', selectSort([1, 5, 2, 9, 6, 3, 8, 2]))

'''
[1, 5, 2, 9, 6, 3, 8, 2]
[1, 2, 5, 9, 6, 3, 8, 2]
[1, 2, 2, 9, 6, 3, 8, 5]
[1, 2, 2, 3, 6, 9, 8, 5]
[1, 2, 2, 3, 5, 9, 8, 6]
[1, 2, 2, 3, 5, 6, 8, 9]
[1, 2, 2, 3, 5, 6, 8, 9]
end:  [1, 2, 2, 3, 5, 6, 8, 9]
'''
