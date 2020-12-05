# -*- coding: utf-8 -*-
# @Time    : 2019/12/4 10:55
# @Author   : 高冷
# @FileName  : P162_24-18面向对象的静态方法与普通方法.py

"""
普通方法:保存在类中,对象来调用,需要self这类参数

静态方法: 1.类的静态方法，不需要self这类参数，因为类的静态方法，不需要进行实例化，就可以进行调用
         2.可以通过类直接调用
         3.在类中的方法名称前加一个头标记@staticmethod。

类方法:  类的方法,由类直接调用,需要cls(类名)这类参数

#       方法总结:
                1.普通方法: 保存在类中,由对象来调用    self =>对象
                2.静态方法: 保存在类中,由类来调用
                3.  类方法: 保存在类中,由类调用        cls=>当前类i

                如果对象中需要保存一些值,执行某功能需要使用对象的值  -->普通方法
                不需要任何对象的值                                 -->静态方法
                不需要任何对象的值                                 -->  类方法
"""

# 普通方法

class FOOL:
    def simple(self, name):
        # 需要self这类参数
        print(name)

obj1 = FOOL()
# 保存在类中,对象来调用,
obj1.simple("Priate")


# 静态方法      @staticmethod

class FOOL_2:
    @staticmethod
    def static(name):
        # 不需要self这类参数，
        print(name)



#类方法             @classmethod

FOOL_2.static("man")
# 可以通过类直接调用

class FOOL_3:
    @classmethod
    def special(cls):
        # cls是类名 需要cls类名
        print(cls)

FOOL_3.special()