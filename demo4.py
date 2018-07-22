# -*- coding: utf-8 -*-
# @Time : 18-7-22 下午3:17
# @Author : weicheng.wang# @Site : 
# @File : demo4.py
# @Software: PyCharm

from threading import Condition
import threading


class TianMao(threading.Thread):

    def __init__(self,name,cond):
        super().__init__(name=name)
        self.cond = cond

    def run(self):
        with self.cond:
            print("{}:Hi".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print ("{}:我们来对故事把".format(self.name))
            self.cond.notify()




class XiaoAi(threading.Thread):

    def __init__(self,name,cond):
        super().__init__(name=name)
        self.connd = cond


    def run(self):
        with self.connd:
            self.connd.wait()
            print("{}:在".format(self.name))
            self.connd.notify()

            self.connd.wait()
            print ("{}:hao".format(self.name))



if __name__ == "__main__":
    """
    启动顺序很重要
    在调用with cond之后才能调用wait或者notify的方法
    condition有两层锁，一把底层锁会在wait后进行释放
    
    
    
    """






    connd = Condition()
    thread_1 = TianMao(name="TianMao",cond=connd)
    thread_2 = XiaoAi(name="XiaoAi",cond=connd)
    thread_2.start()
    thread_1.start()










