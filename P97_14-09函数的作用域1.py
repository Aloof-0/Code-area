# python中的作用域分4种情况：
"""
L：local，局部作用域，即函数中定义的变量；
E：enclosing，嵌套的父级函数的局部作用域，即包含此函数的上级函数的局部作用域，但不是全局的；
G：globa，全局变量，就是模块级别定义的变量；
B：built-in，系统固定模块里面的变量，比如int, bytearray等。 搜索变量的优先级顺序依次是：作用域局部>外层作用域>当前模块中的全局>python内置作用域，也就是LEGB。

（1）变量查找顺序：LEGB，作用域局部>外层作用域>当前模块中的全局>python内置作用域；

（2）只有模块、类、及函数才能引入新作用域；

（3）对于一个变量，内部作用域先声明就会覆盖外部变量，不声明直接使用，就会使用外部作用域的变量；

（4）内部作用域要修改外部作用域变量的值时，全局变量要使用global关键字，嵌套作用域变量要使用nonlocal关键字。nonlocal是python3新增的关键字，有了这个 关键字，就能完美的实现闭包了。
"""
# python中的作用域的分布情况
x =int(2.9)                # bulit_in  系统固定模块里面的变量
g_count = 0                # globa     模块级别的变量
def outer():
    o_cont =1              # enclosing 嵌套的父级函数的局部作用域
    def inner():
        i_count = 2        # local     局部作用域
        print(o_cont)
    inner()
outer()

# 局部作用域不能修改全局作用域的变量(需要globa) 顺序要一致
"""
count = 10                X
def f():
    print(count)         (1)     //这里print找到了count 但是顺序搞错了
    count = 5            (2)     //由内而外 先找里面的 在找外面的
f()             >>>报错
"""
# globa关键字
# 当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字了，当修改的变量是在全局作用域（global作用域）上的，就要使用global先声明一下，代码如下：
co = 10
ll = 20
def f():
    global co,ll                   #                     //globa是
    print(co)                      # >>>10
    co = 5
    print(co)                      # >>>5               // 证明co已经被修改
f()

# nonlocal关键字
# global关键字声明的变量必须在全局作用域上，不能嵌套作用域上，当要修改嵌套作用域（enclosing作用域，外层非全局作用域）中的变量怎么办呢，这时就需要nonlocal关键字了
def outer():
    count = 10
    def inner():
        nonlocal count
        count = 20                 # >>> 20 局部作用域能修改嵌套的父级函数的局部作用域
        print(count)
    inner()
    print(count)                   # >>> 20
outer()




