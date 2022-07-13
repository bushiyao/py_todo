# coding=utf-8
# @Time : 2022/7/13 16:24 
# @Author : hh
# @File : thread_async.py 
# @Software: PyCharm

from threading import Thread
import time
import random

def asynca(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)
        thr.start()
    return wrapper

@asynca
def do_sth(n):
    time.sleep(random.randint(1, 5))
    print(n)

def do_list():
    for n in range(10):
        do_sth(n)
        print("end - {}" . format(str(n)))

if __name__ == "__main__":
    # async to do this
    do_list()
    '''
    end - 0
    end - 1
    end - 2
    end - 3
    end - 4
    end - 5
    end - 6
    end - 7
    end - 8
    end - 9
    1
    5
    7
    8
    0
    3
    2
    4
    6
    9
    '''



