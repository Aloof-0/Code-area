# 函数语句:
"""
 (定义)
 define f():                                              3-5都是函数定义
    print("ok")

f()                                                       7为函数调用
"""
# 函数也是一个变量它会指向一个内存地址    (如果调用一定要加括号)
def f():
    print("ok")
print(f)                                                   # >>><function f at 0x000002366B30C268>

# 形参与实参数量一定要一致
"""
def jjj(b,a,c):
    print(b,a,c)                                           # 报错
jjj(1,3)
"""

# 实参可以传递无数次
def x(n):
    print(n)
def y(n):                                                 # >>>1  这里的实参传递了两次 函数调用函数
    x(n)
y(1)

# 加法器
def adc(*num):
    print("总数:",num)
    sum = 0
    for i in num:
        sum += i                                          # >>>总数: (1, 2, 3, 4, 5, 6, 7)
    print(sum)                                            # >>>28
                                                          # >>>7
adc(1,2,3,4,5,6,7)

import 草稿本
草稿本.f(7)