# 简单的伪生成器
'''
1.在Python中，一边循环一边计算的机制，称为生成器：generator。
  生成器仅仅保存了一套生成数值的算法，并且没有让这个算法现在就开始执行，而是我什么时候调它，它什么时候开始计算一个新的值，并给你返回。

2. 为什么要有生成器
列表所有数据都在内存中，如果有海量数据的话将会非常耗内存。
如：仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。
如果列表元素按照某种算法推算出来，那我们就可以在循环的过程中不断推算出后续的元素，这样就不必创建完整的list，从而节省大量的空间。
简单一句话：我又想要得到庞大的数据，又想让它占用空间少，那就用生成器！

3.工作原理
1）生成器(generator)能够迭代的关键是它有一个next()方法，
　　工作原理就是通过重复调用next()方法，直到捕获一个异常。

（2）带有 yield 的函数不再是一个普通函数，而是一个生成器generator。
　　可用next()调用生成器对象来取值。next 两种方式 t.__next__()  |  next(t)。
　　可用for 循环获取返回值（每执行一次，取生成器里面一个值）
　 （基本上不会用next()来获取下一个返回值，而是直接使用for循环来迭代）。

（3）yield相当于 return 返回一个值，并且记住这个返回的位置，下次迭代时，代码从yield的下一条语句开始执行。

（4）.send() 和next()一样，都能让生成器继续往下走一步（下次遇到yield停），但send()能传一个值，这个值作为yield表达式整体的结果
　　——换句话说，就是send可以强行修改上一个yield表达式值。比如函数中有一个yield赋值，a = yield 5，第一次迭代到这里会返回5，a还没有赋值。第二次迭代时，使用.send(10)，那么，就是强行修改yield 5表达式的值为10，本来是5的，那么a=10
'''

# 1.列表伪生成器                         //注意:这里是列表,的非生成器
    #  x操作 -----> 0-9
yy = [ x*x for x in range(10)]
print(yy)

#       2.也可以用函数去调用它
def AAA():
    yield 1                                 # 使用yield关键字得到一个生成器函数，调用这个函数得到一个生成器对象       retuen next.(AAA())

print(next(AAA()))                          # >>>1

#       3.普通生成器                                    ////第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
s = (p*p for p in range(10))                # 用元组而不是列表
print(s)                                    # >>> <generator object <genexpr> at 0x000001FF3F0D3ED0>
"""
注意:
1.根本就没有值
2.得到的只是一个对象
3.不使用永远不会生成
（1）只有在调用时才会生成相应的数据
（2）只记录当前位置
（3）在python3中只有一个__next__()方法，在python2.7中该方法为next（）方法

"""









