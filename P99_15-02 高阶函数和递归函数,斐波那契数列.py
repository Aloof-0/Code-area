# 高阶函数
"""
高阶函数：一个函数可以作为参数传给另外一个函数，或者一个函数的返回值为另外一个函数（若返回值为该函数本身，则为递归），满足其一则为高阶函数。

# 1.函数名可以进行赋值          foo = f  (f为函数名)
# 2.函数名可以作为函数参数      bar(1,2,f)
# 3.还可以作为函数的返回值      return f                       # 递归函数 return f(n-1)+f(n-2)             //斐波那契数列
"""
# 函数名可以作为函数参数  (高阶函数)
def fdf(n):
    return n * n
def ggg(a,b,fun):
    return fdf(a)+fdf(b)                    # fun =fdf = n * n 即把fdf函数带入到fun变量里
print(ggg(1,2,fdf))

# 递归函数
"""
定义：在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。

关于递归函数的特性
# 1.调用自身的函数 
# 3.但凡是递归可以写的循环都可以解决
# 4.递归的效率有时候会很低
"""

# 实例1(阶乘) 普通循环  f(7)  7*6*5*4*3*2*1 =sum 求sum
def hhh(n):
    r = n
    for i in range(1,n):
        r *= i
    return r
print(hhh(4))

# **********递归*********
def fac(n):
    if n == 1:
        return 1                  # 不让它无限循环下去 ,它终点为1
    return n * fac(n - 1)
print(fac(3))

# 实例2(斐波那契数列) f(7)           s a b
#                                 0 1 1 2 3 5 8 13 21 34 55   即 s + a = b  求b
# 索引                              0 1 2 3 4 5  6  7  8  9
def fibo(n):
    star = 0
    after = 1
    for i in range(n - 1):
        ret = star + after            # 即后面的数边前面的树 即 b = a + b, s = a ,a =b
        star = after
        after = ret
    return ret
print(fibo(7))

# **************递归*********************
def fibo_new(n):  # n可以为零，数列有［0］  f(7)=f(6)+f(5)
    if n <= 1:
        return n
    return (fibo_new(n - 1) + fibo_new(n - 2))
print(fibo_new(3))
#递归特性:
'''
1. 必须有一个明确的结束条件

2. 每次进入更深一层递归时，问题规模相比上次递归都应有所减少
'''


