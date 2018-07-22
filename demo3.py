# -*- coding: utf-8 -*-
# @Time : 18-7-21 下午5:48
# @Author : weicheng.wang# @Site : 
# @File : demo3.py
# @Software: PyCharm


import threading
from threading import Lock,RLock


total = 0
lock = RLock()


def add():
    global total
    global lock
    for i in range(10000):
        lock.acquire()
        total += 1
        lock.release()

def desc():
    global total
    for i in range(10000):
        total -= 1


