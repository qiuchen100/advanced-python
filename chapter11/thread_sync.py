# -*- coding: utf-8 -*-

import dis
import threading
from threading import Lock, RLock

total = 0
lock = Lock()
rlock = RLock()

"""
RLock 可重入都锁
在同一个线程里面，可以连续调用多次acquire，一定要
注意acquire的次数要和release次数相等
"""


def add():
    global total
    global rlock
    for i in range(1000000):
        rlock.acquire()
        rlock.acquire()
        total += 1
        rlock.release()
        rlock.release()


def desc():
    global total
    global rlock
    for i in range(1000000):
        rlock.acquire()
        total -= 1
        rlock.release()


def add1(a):
    a += 1


def desc1(a):
    a -= 1


'''
add函数
1. load a
2. load 1
3. + 1
4. 赋值给a a=1
'''

'''
desc函数
1. load a
2. load 1
3. - 1
4. 赋值给a a=-1
'''

# 解决线程同步问题：锁
# 用锁会影响性能，获取锁 释放锁都需要时间
# 锁会引起死锁



thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)
thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(total)

print(dis.dis(add1))
print(dis.dis(desc1))
