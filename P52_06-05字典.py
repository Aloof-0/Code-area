# 1.Dictionary字典
'''
字典是python中唯一的映射类型，采用键值对（key-value）的形式存储数据。python对key进行哈希函数运算，根据计算的结果决定value的存储地址，所以字典是无序存储的，且key必须是可哈希的。
可哈希表示key必须是不可变类型，如：数字、字符串、元组。字典(dictionary)是除列表意外python之中最灵活的内置数据结构类型。
列表是有序的对象结合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
'''
# ！！字典增查改 都一样 删除就用del
# 1.字典是中括号,且内容是无序性的,即无下表
dic1={'name':'alex','age':36,'sex':'male','dd':True}
      #name为键, alex为值,键是唯一的,非变量,只是一种映射关系,如拼音字典,搜索S则找到拼音以S为首的字一样    键指向值

#2.不可变类型:整形,字符串,元组    可变类型:列表,字典(值为可变类型,只是键为不可变类型)
dic2 = {'sex':'男','number':'10','ip':'5201314'}   #就是sex(键)是不可变的,但"男"(值)是可变的，可修改的
dic2['sex'] = "女"
print(dic2)         #{'sex': '女', 'number': '10', 'ip': '5201314'}

#3.反正就是dic = {"不可变类型"   :   "可变类型"}
#             整形,字符串,元组       列表,字典

#4.它是无序的
     #假设下标：1,2,3,4,5,6
dic3 = {'sex_1':'男','number_1':'10','ip_1':'5201314','love':'女人','home':'301','want':'rich','abc':'456','zoo':'dd'}
print(dic3)   #因为它是无序的,所以有可能

#5.字典可以内置字典
                #因为值是可变类型的,而字典也是,所以字典可以内置字典
dic4 = {'sex': '男', 'number': '10', 'ip':{'BY':'C'}}
print(dic4['ip'])

#创建字典
dic11=dict((('name','alex'),))      #创建字典的另一种方法
print(dic1)
print(dic2)

#增
dic3 = {}

dic3['name'] = 'alex'
dic3['age'] = 18
print(dic3)  # {'name': 'alex', 'age': 18}

a = dic3.setdefault('name', 'yuan')
b = dic3.setdefault('ages', 22)    #增加字典的另一种方法
print(a, b)
print(dic3)

#查
dic3 = {'name': 'alex', 'age': 18}
print(dic3.items())                      #items() 函数以列表返回可遍历的(键, 值) 元组数组。
print(dic3.keys())                       #keys() 函数以列表返回可遍历的键 元组数组。
print(dic3.values())                     #valuss() 函数以列表返回可遍历的值 元组数组。

print('name' in dic3)                    #判断 如果name在dic3 里则True 反之则False
print(list(dic3.values()))

#改
dic3 = {'name': 'alex', 'age': 18}
dic3['name'] = 'alvin'
dic4 = {'sex': 'male', 'hobby': 'girl', 'age': 36}
dic3.update(dic4)            #.update()     字典dict2的键/值对更新到dict里. 即把dic4加到dic3里 d3变,d4不变
print(dic3,dic4)             #          >>>{'name': 'alvin', 'age': 36, 'sex': 'male', 'hobby': 'girl'} {'sex': 'male', 'hobby': 'girl', 'age': 36}


#删
dic4 = {'name': 'alex','class': 1,'age': 18, }

del dic4['name']           #普通删除,无返回值     >>>{'class': 1, 'age': 18}
print(dic4)

b = dic4.pop('age')        #pop删除,有返回值     >>>18 {'class': 1}
print(b,dic4)

a = dic4.popitem()         #随机删除,有返回值    >>>('class', 1) {}
print(a, dic4)

dic4.clear()               #清空字典             >>>{}
print(dic4)

#其他操作以及涉及的方法

    #.fromkeys() 函数用于创建一个新字典,以序列 abc 中元素做字典的键,cde 为字典所有键对应的初始值.  dic041.fromkeys(['abc','abc'],cde)  !需要一个字典
seq = {}
dict = seq.fromkeys(['abc','abcd'],'love')
print(dict)                     #>>>{'abc': 'love', 'abcd': 'love'}

    #.copy() 函数返回一个字典的浅复制
dict44 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
dict22 = dict44.copy()
print("新复制的字典为 : ", dict22)      #>>>新复制的字典为 :  {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

     #sorted 对所有可迭代的对象进行排序操作      sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。有返回值 应用于所有对象
                                              #sort 方法返回的是对已经存在的列表进行操作，无返回值只应用于列表
dic0415 = {5:'555',2:'222',3:'333'}
print(sorted(dic0415))                        #默认是排列键 >>>[2, 3, 5]
print(sorted(dic0415.keys()))                 #排列键       >>>[2, 3, 5]
print(sorted(dic0415.items()))                #排列列表     >>>[(2, '222'), (3, '333'), (5, '555')]
print(sorted(dic0415.values()))               #排列值       >>>['222', '333', '555']

    #1字典的遍历
dic5={'name': 'alex', 'age': 18}

for i in dic5:
    print(i,dic5[i])              #最佳,快

for items in dic5.items():
    print(items)
for keys,values in dic5.items():
    print(keys,values)

    #列表的嵌套
av_catalog = {
    "欧美":{
        "www.youporn.com": ["很多免费的,世界最大的","质量一般"],
        "www.pornhub.com": ["很多免费的,也很大","质量比yourporn高点"],
        "letmedothistoyou.com": ["多是自拍,高质量图片很多","资源不多,更新慢"],
        "x-art.com":["质量很高,真的很高","全部收费,屌比请绕过"]
    },
    "日韩":{
        "tokyo-hot":["质量怎样不清楚,个人已经不喜欢日韩范了","听说是收费的"]
    },
    "大陆":{
        "1024":["全部免费,真好,好人一生平安","服务器在国外,慢"]
    }
}

av_catalog["大陆"]["1024"][1] += ",可以用爬虫爬下来"  #修改,或增加列表
print(av_catalog["大陆"]["1024"])
