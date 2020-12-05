# 1.深浅拷贝

     # 1.普通复制
s = [1,'alex','alvin']
s1 = [1,'alex','alvin']
s1[0] = 2
print(s)
print(s1)                                                                           # 可行,但是假如数据多的话 则不现实

     # 2.伪思路
a = [1,'alex','alvin']
a1 =a.copy()
print(a)             # [1, 'alex', 'alvin']
print(a1)            # [1, 'alex', 'alvin']
a1[0] = 2
print(a)            # [1, 'alex', 'alvin']
print(a1)           # [2, 'alex', 'alvin']                                         看起来好像a1怎么变 都不会与a2有关系

    # 3.真思路
b = [[1,2],3,4]
b1 = b.copy()
print(b)           # [[1, 2], 3, 4]
print(b1)          # [[1, 2], 3, 4]
b1[0][1] = 0
print(b)           # [[1, 0], 3, 4]
print(b1)          # [[1, 0], 3, 4]                                                但其实是有关系的 ,那为什么改 a1的【0】索引就没关系 改b1的[0][1]就有关系呢

"""
因为[[1, 2], 3, 4]里的 [1.2]是一个可变的内存地址 b,b1的索引都指向可变的内存地址   【1,2】变时 b,b1 都会变化
详情见 D:\python\LOVE\图片\深浅拷贝
"""

    # 4.深拷贝与浅拷贝
c = [[1,2],3,4]
c1 =c.copy()                                                                        # 浅复制
import copy
c2 = copy.deepcopy(c)                                                               # 深复制 要载入copy板块

    # 5.深复制与浅复制最大的区别
"""
    浅拷 = 只拷贝第一层
    深拷贝 = 克隆一份
"""

