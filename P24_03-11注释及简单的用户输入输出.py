msg = "我爱北京天安门？"
print(msg)   #井号在后面-代码注释
#print(msg)   #井号在前面-单行注释
'''print(msg) #三点包括在里面-多行注释(只要是三点都可以:""",'')
print(msg)
'''


# 注释：
   # 单行注释 用#
   # 多行注释用三个单引号或三个双引号'''被注释的内容'''


# input("你的名字:")         #input输入



#print INPUT 需要用到变量；   死亡日期：
death_age = 100             #默认活100岁
name = input("你的名字:")
age  = input("你的年龄:")  #input 接受的所有数字都是字符串,即使你输入的是数字,依然会被当成字符串来处理
print(type(age))           #显示age的类型

print("你的名字是:", name)
print("你的年龄是:", age)
print("你还可以活:", death_age - int(age), "年")


#int integer=整数 把字符串转成证整数(INT)  用int(被转的数据)
#str string =字符串 把数据转成字符串(INT)  用str(被转的数据)
