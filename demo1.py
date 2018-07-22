# -*- coding: utf-8 -*-
# @Time : 18-7-21 下午3:36
# @Author : weicheng.wang# @Site : 
# @File : demo1.py
# @Software: PyCharm

import threading
import time


class GetDetailHtml(threading.Thread):

    def __init__(self,name):
        super().__init__(name=name)


    def run(self):
        print ("get detail html start")
        time.sleep(2)
        print ("get detail html end")


