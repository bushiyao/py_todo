# coding=utf-8
# @Time : 2022/8/3 18:49 
# @Author : hh
# @File : d2281.py 
# @Software: PyCharm


class Solution(object):
    def totalStrength(self, strength):
        """
        :type strength: List[int]
        :rtype: int
        """

        sum = 0
        count = len(strength)
        for t in range(count + 1):
            ns = strength[t:]
            n = len(ns)
            while n > 0:
                data = ns[0:n]
                dsum = 0
                for d in data:
                    dsum += d
                sum = sum + (min(data) * dsum)
                n -= 1
            print('sum: ', sum)
        return sum


if __name__ == "__main__":
    s = [1,3,1,2]
    do = Solution().totalStrength(s)
    print(do)