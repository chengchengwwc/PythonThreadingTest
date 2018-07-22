# -*- coding: utf-8 -*-
# @Time : 18-7-22 下午3:54
# @Author : weicheng.wang# @Site : 
# @File : demo5.py
# @Software: PyCharm


#Semaphore 控制进入数量的所

import threading
from threading import Semaphore
import time


class HtmlSpider(threading.Thread):

    def __init__(self,url,sem):
        super().__init__()
        self.url = url
        self.sem = sem

    def run(self):
        time.sleep(2)
        print ("GET URL")
        self.sem.release()


class UrlProducer(threading.Thread):
    def __init__(self,sem):
        super().__init__()
        self.sem = sem

    def run(self):
        for i in range(20):
            self.sem.acquire()
            html_thread = HtmlSpider(url=i,sem=self.sem)
            html_thread.start()


if __name__ == "__main__":
    sem = Semaphore(3)
    thread_1 = UrlProducer(sem=sem)
    thread_1.start()














