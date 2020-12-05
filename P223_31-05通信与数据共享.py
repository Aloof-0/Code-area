# -*- coding: utf-8 -*-
# @Time    : 2020/2/7, 17:21 
# @Author   : 高冷
# @FileName: P223_31-05通信与数据共享.py

from multiprocessing import Process, Queue

def f(q,n):
    q.put([42, n, 'hello'])

if __name__ == '__main__':
    q = Queue()

    for i in range(3):
        p = Process(target=f, args=(q,i))
        p.run()
    print(q.get())
    print(q.get())
    print(q.get())

