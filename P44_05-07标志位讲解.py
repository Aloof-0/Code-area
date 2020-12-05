#在10里面,输出5-10的数
for i in range(11):
    if i<5:
        continue #作用:结束本次循环,继续下次循环
    print (i)
    

for i in range(10):
    if i < 5:
        continue
    
    print(i)
    for j in range(10):
        print(j,end="")
        if j==6:
            break
"""

break:跳出当前循环
continue: 结束本次循环,继续下次循环 

数据类型:
         列表,元组


name0 = "a"
name1 = "b"
name2 = "c"                                                  如果需要存储一个列表,用多个变量可以,但是没有联系.
name3 = "d"
name4 = "e"

names = ['a','B','C','D','E'] 
print("F" in names)
>>>Flash
     
         
names = ['a','B','C','D','E']                                用单个变量就可以存储,既有联系,而且简洁
   位置:  0   1   2   3   4                                  可以用来增删改查
   索引:print(names[3])            >>>D                      用索引来"查位置"
         [起点:   终点-1]
        print(names[1:3])          >>>B C
        print(names[1:])           >>>B C D E                冒号后面什么都不加;自动查到最后一个,"取到最后"
        print(names[1:-1])         >>>B C D                  冒号后面加一个-1;"取到倒数第二个"             
        print(names[1:-1:1])       >>>B C D                  从左到右一个一个去取;长为正数 则方向为("从左到右")
        print(names[1::2])         >>>B D                    从左到右隔一个去取;长为2 则"隔一个数"
        print(names[1::-2])        >>>D B                    从右到左隔一个去取;长为负数且为2 则方向为"从右到左隔一个数"

    1."求顺序 D B:" 
               print(names[3::-2])                           print(names[-1:1:-2])
        
        
    2."从之前的列表里取出一段赋予一个新列表"
       names = ['a','B','C','D','E']          
       print(print(names[1::-2]))                  "D B"
       name_pop = names[1::-2]                     "D B"赋予新变量;即 name_pop = ['D','B']    
       print = name_pop                         >>>"D B"   
 
 
2.'增加新列表'(append[追加];insert[插入])

names = ['a','B','C','D','E']  
     
      
          a.append('F')                                 names.insert(1,'Z')
                          '里面放的是你添加内容的值';          
          append()                    相同              insert()    
    
          append('F')                 不同              insert(1,'Z')
    '默认插到最后一个位置'                          '将数据插入到任意一个位置'
>>>'a','B','C','D','E','F'                           >>>'a','Z','B','C','D','E'


3.'修改列表'

单个修改
names = ['a','B','C','D','E']
 a[1] = 'Z'                            直接替换
print(names)
>>>'a','Z','C','D','E'

多个修改
names = ['a','B','C','D','E']
names[1:3]  =['A','O']                     把['B','C']替换成['A','O']
print (a)           
>>>'a','A','O','D','E'

4.'删除列表'(remove[去除],pop,del)

names=['Apple','Baby','Cat','Dog','Egg']

#你不知道要从列表中删除的值所处的位置;                            你可以使用pop()来删除列表中任何位置的元素,
#如果你只知道要删除的元素的值 可使用remove                        只需要在括号中指定要删除的元素的索引即可                                        
                                                                   
names.remove('Baby')   '单纯只是删除'                              names.pop('Apply')   '可以返回删除的值'
print(names)           '删谁(内容)就把他放到remove里面'            print(names)          
                       '不可以直接删下标'                          
names.remove(names[1]) '也可以'                                     names.pop(0)         '可以直接删下标'            
>>>'Apple','Cat','Dog','Egg'                                        >>>'Baby','Cat','Dog','Egg'


#如果知道要删除的元素在列表中的位置,可使用del语句.
del names[0]                                                       比如:
print(names)                                                        names=['Apple','Baby','Cat','Dog','Egg']
>>>'Baby','Cat','Dog','Egg'                                         abc=names.pop(0)        #看它有没有值
                                                                    print(names)
del names               '可以直接删变量'                            print(abc)
print(names)
>>错误                  '已经没有了'                                >>>'Baby','Cat','Dog','Egg'
                                                                    >>>'Apple'
                                                                    可以直接调用删除的值





列表,元组
         "查"
             索引(下标),都是从0开始
             切片
             .count 查某个元素的出现次数
             .index 根据内容找其对应的位置
             "XXX" in names
          "增加"
              a.append()追加"最后一个"
              a.insert(位置,内容)
          "删除"
              a.remove("只能内容")
              a.pop("内容"或"下标")   可以返回删除的值
              a.clear("清空所有内容")          
          "排序"
              a.sort("分类")
              a.reverse("倒序")              
      


"""




