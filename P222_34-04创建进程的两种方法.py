# -*- coding: utf-8 -*-
# @Time    : 2020/2/3, 0:19 
# @Author   : 高冷
# @FileName  : P222_34-04创建进程的两种方法
"""
程序的执行实例称为进程。
1. 每个进程都提供执行程序所需的资源。
2. 进程具有虚拟地址空间、可执行代码、对系统对象的打开句柄、安全上下文、唯一进程标识符、环境变量、优先级类、最小和最大工作集大小以及至少一个执行线程。每个进程都由一个线程（通常称为主线程）启动，但可以从其任何线程创建其他线程。
3. 进程应该避免数据共享, 如果非要的话,应该优先考虑pipe和queue
"""
# 创建进程的方法一
from multiprocessing import Process
import time

def times(name):
    time.sleep(1)
    print("hellow", name, time.ctime())
if __name__ == '__main__':
    p_list = []
    for i in range(3):
        p = Process(target=times, args=("china",))
        p_list.append(p)
        p.start()
    for p in p_list:
        p.join()
    print("end")
# 类方法

class MyProcess(Process):
    def __init__(self):
        super(MyProcess,self).__init__()

    def run(self, name):
        time.sleep(1)
        print("hellow", name, time.ctime())

A = MyProcess()
A.run("me")




