# -*- coding: utf-8 -*-
# @Time : 18-7-21 下午4:58
# @Author : weicheng.wang# @Site : 
# @File : demo2.py
# @Software: PyCharm

import threading
import time
from queue import Queue



def get_detail_url(queue):
    print ("Get detail url start")
    for i in range(10):
        queue.put("id={}".format(i))

    time.sleep(2)
    print ("Get dettail url end")

def get_detail_html(queue):
    while True:
        url = queue.get()
        print ("Get detail {} start".format(url))
        time.sleep(2)
        print ("Get detail {} end".format(url))

if __name__ == "__main__":

    queue_list = Queue()
    thread_1 = threading.Thread(target=get_detail_html,args=(queue_list,))
    thread_2 = threading.Thread(target=get_detail_url,args=(queue_list,))
    thread_1.start()
    thread_2.start()




















