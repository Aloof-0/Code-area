#1.count(计数)
 #    count方法统计某个元素在列表中出现的次数:
>>>names = ['to','be','or','not','to','be']
>>>names.count('to')
2
>>>BBC = [[1,2],1,1,[2,1,[1,2]]]
>>>BBC.count(1)
2
>>>BBC.count([1,2])
1


#2.extend(延伸)
      #extend方法把另一个列表的元素放入另一个列表里:'可以在列表的末尾一次性追加另一个序列中的多个值.'
>>>a = [1,2,3]
>>>b = [4,5,6]
>>>a.extend(b) 
>>>print(a)
>>>print(b)
1,2,3,4,5,6
4,5,6
 # extend方法修改了被扩展的列表,而原始的连接操作（+）则不然,它会返回一个全新的列表.
>>> a = [1, 2, 3]
>>> b = [4, 5, 6]  
>>> a.extend(b)  
>>> print(a)  
[1, 2, 3, 4, 5, 6] 
 
>>> print(a + b)
[1, 2, 3, 4, 5, 6, 4, 5, 6]    
>>> print(a)
[1, 2, 3, 4, 5, 6]  


3.index(指数)
    index方法把某个元素指出在哪位置:'只知道名字,不知道位置'
             用于从列表中找出第一个匹配项的索引位置:
>>>names = ['apple','boy','cat','dog','egg']
>>>print(names.index('boy'))
>>>1

    '但是如果有两个相同的元素怎么办'#boy
>>>names = ['apple','boy','cat','egg','fuck','boy','girl']
>>>print(names.index(boy))
1                                     #无论怎么查都是找到第一个就退出

可以建一个大列表,两个列表:(切片)
names = 【  {'apple','boy'} ,('cat','egg','fuck','boy','girl') 】
第一小列表boy的位置 = names.index('boy')
#xiaoliebiao的值为1
'第二小列表' = names[第一小列表+1:]  #第二个小列表的第一个元素到最后一个元素

第二个小列表boy的位置 = '第二小列表'.index('boy')

大列表'2boy'= 第一小列表boy的位置 +第二个小列表boy的位置+1
5

4.reverse(颠倒) 
      reverse方法将列表中的元素反响存放          
>>>names = ['to','be','or','not','to','be']
>>>names.reverse()
>>>print(names)

5.sort(分类)
    sort方法用于在原位置对列表进行排序
>>>names = [4,5,2,1,7,9]
>>>names.sort()
>>>print(names)
[1,2,4,5,7,9]
"非数字时" :按26英文字母排序;











