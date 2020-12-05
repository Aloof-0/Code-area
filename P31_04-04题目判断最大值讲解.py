# 输入3个数字,比大小 num1,num2,num3
'''
思路:
num1>num2>num3    num1最大
num1>num3>num2    num1最大
num2>num1>num3    num2最大
num2>num3>num1    num2最大
num3>num2>num1    num3最大
num3>num1>num2    num3最大

伪代码:
num1=int(input("num1:"))
num2=int(input("num2:"))
num3=int(input("num3:"))

if   num1<num2 or num1<num3:
    print("最大:num1",num1)
elif num2<num1 or num2<num3:
    print("最大:num2",num2)
else num3<num1 or num3<num2:
    print("最大:num3",num3)

正确代码1:         (复杂,新手)                        #不加入一个数
num1=int(input("num1:"))
num2=int(input("num2:"))
num3=int(input("num3:"))

if   num1>num3>num2:                                  #如果数1大于数3大于数2
    print("num1最大")                                 #输出最大值是数1                
elif num1>num2>num3:                                  #如果数1大于数2大于数3
    print("num1最大")                                 #输出最大值是数1
elif num2>num1>num3:                                  #如果数2大于数1大于数3
    print("num2最大")                                 #输出最大值是数2
elif num2>num3>num1:                                  #如果数2大于数2大于数3
    print("num2最大")                                 #输出最大值是数2
elif num3>num2>num1:                                  #如果数3大于数2大于数1
    print("num3最大")                                 #输出最大值是数3   
else:                                                 #否则(如果数3大于数1大于数2)
    print("num3最大")                                 #输出最大值是数3 

正确代码2:          (简洁,进阶)
num1=int(input("num1:"))
num2=int(input("num2:"))
num3=int(input("num3:"))
MAX_num=0                                             #参数...加入第4个数,主要用来做对比
if num1>num2:                                         #如果数1>数2
    MAX_num=num1                                            #则MAX=数1
    if MAX_num>num3:                                        #又如果MAX>数3
        print("MAX NUM IS",MAX_num)                         #输出最大值是MAX
    else:                                                   #否则的话
        print("MAX NUM IS",num3)                            #输出最大值是数3
else:                                                 #否则的话(数1<数2)
    MAX_num=num2                                            #MAX=数2
    if MAX_num>num3:                                        #又如果MAX大于数3
        print("MAX NUM IS",MAX_num)                         #输出最大值是MAX
    else:                                                   #否则的话
        print("MAX NUM IS",num3)                            #输出最大值是数3
'''

  
num1=int(input("num1:"))
num2=int(input("num2:"))
num3=int(input("num3:"))
MAX_num=0                                             #参数...加入第4个数,主要用来做对比
if num1>num2:                                         #如果数1>数2
    MAX_num=num1                                            #则MAX=数1
    if MAX_num>num3:                                        #又如果MAX>数3
        print("MAX NUM IS",MAX_num)                         #输出最大值是MAX
    else:                                                   #否则的话
        print("MAX NUM IS",num3)                            #输出最大值是数3
else:                                                 #否则的话(数1<数2)
    MAX_num=num2                                            #MAX=数2
    if MAX_num>num3:                                        #又如果MAX大于数3
        print("MAX NUM IS",MAX_num)                         #输出最大值是MAX
    else:                                                   #否则的话
        print("MAX NUM IS",num3)                            #输出最大值是数3
















