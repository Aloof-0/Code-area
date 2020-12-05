"""
def jjj():
        yeild 3212313
1.只要有yield的函数,就是一个生成器对象 即与return一样,遇到yeild就结束函数金,如果有多个yield,则进行一个退出一个

2.不是jjj是一个生成器对象,而是foo()是一个生成器对象

3.本质上能进行for循环的都是可迭代对象:生成器,迭代器(对象拥有iter方法)

next 和 send的区别
4. ///简单来说，next和send都是调用yield生成值的函数，next是直接调用，send是先覆盖上一个yield返回值后再调用下一个yield生成值。
即可以第一个就可以直接next(函数名),但send 不同,他需要覆盖上一个yeild,所以他需要函数名.send（None）
"""

# yield
def aaa():          # 3.转到函数
    print("ok1")            # 4.print("OK1")
    count = yield 123456            # 5.遇到第一个yield 退出函数 返回123456   #7.继续函数c.send("eee")给了count
    print(count)                        # 8.因为send=eee, print((count)==>eee
    yield 255555                        # 9.遇到第二个yield 退出函数

c = aaa()     # 1.aaa()赋予c 因为他是生成器所以不会执行函数
c.send(None)  # 2. 等同于next(c) 但是第一次send前如果没有next,只能传send(None)   假如print(c.send(None))得到的是123456
c.send("eee") # 6.把eee传给yield

'''
1.   #2.使用next(r) 和 r.send(None)输出的结果都是"ok1"
     为什么不send 多一个,yield 123456 send的是eee, yield 25555 还也可以send的啊?    假如 LLL = yield 25555
2.   因为函数遇到yield 就退出 
'''

