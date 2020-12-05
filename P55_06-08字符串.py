#Staring 操作

#1.创建字符串：
var1 = 'Hello World!'
var2 = "Python RAlvin"

#2.重复输出字符串
print('hello'*2)         #>>>hellohello

#3.[] ,[:] 通过索引获取字符串中字符,这里和列表的切片操作是相同的,具体内容见列表
print('helloworld'[2:])   #切片,不用逗号     >>>lloworld

#4. in  成员运算符 - 如果字符串中包含给定的字符返回 True
print('el' in 'hello')   #判断是否包含       >>>True
print('AA' in 'hello')   #                  >>>False

#5. %   格式字符串
print('alex is a good teacher')
print('%s is a bad teacher'%'alex')
#6. +   字符串拼接
a='123'
b='abc'
c='789'
d1=a+b+c
print(d1)    # +效率低,该用join

d2 =''.join([a,b,c])           #join拼接
print(d2)

d3 = '==='.join([a,b,c])      #>>>      123===abc===789
print(d3)

