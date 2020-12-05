#循环:
 

 
#1.while死循环(while语句+条件 )

#当while后面的条件成立(True),才会执行它下面的代码

#while True:              #当真的时候,因为是默认为真,所以这是个死循环
#    print("acv")
    
#conter = 0
#while True:
#    counter+=1           #一样死循环

#1.'输入密码,登陆'

counter = 0
while counter  < 3:
    yonghuming = input("账号:")
    password = input ("密码:")
    if yonghuming =="leng" and password =="520":
        print("欢迎进入:")
        break
    else:
        print("输多一次:")
    counter += 1
    
    if counter == 3:
        jixu = input("还继续吗[y/n]")
        if jixu =="y":
            counter=0
else:
    print("输入太多次了.")