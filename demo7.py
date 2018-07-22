# -*- coding: utf-8 -*-
# @Time : 18-7-22 下午7:53
# @Author : weicheng.wang# @Site : 
# @File : demo7.py
# @Software: PyCharm

from concurrent.futures import ProcessPoolExecutor,as_completed
import time

def fib(n):
    if n<=2:
        return 1
    return fib(n-1)+fib(n-2)


if __name__ == "__main__":
    with ProcessPoolExecutor(3) as executor:
        all_tasks = [executor.submit(fib,(num)) for num in range(25,35)]
        start_time = time.time()
        for future in as_completed(all_tasks):
            print (future.result())
        print (time.time()-start_time)
