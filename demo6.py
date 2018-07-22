# -*- coding: utf-8 -*-
# @Time : 18-7-22 下午4:13
# @Author : weicheng.wang# @Site : 
# @File : demo6.py
# @Software: PyCharm


from concurrent.futures import ThreadPoolExecutor,as_completed,wait
import time

def get(times):
    time.sleep(times)
    print("GEt URL")
    return "DDD"



if __name__ == "__main__":
    executor = ThreadPoolExecutor(max_workers=2)
    urls = [2,3,4]
    """
    all_tasks = [executor.submit(get(url)) for url in urls]
    for future in as_completed(all_tasks):
        data = future.result()
    """
    for future in executor.map(get,urls):
        print (future)









