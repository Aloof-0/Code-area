
"""
如何输出一个如下的直角三角形,用户指定输出行数:(如果上下反转,又如何实现)

*
**
***
****
*****
******
*******
********
"""
#1.如何输出一个如下的直角三角形,用户指定输出行数:(如果上下反转,又如何实现){即倒三角型}
                                              
                                              #输入6
                                                           # 结果:                    原本结果非*:
hang =int(input(""))                                       #      ******                           654321
while hang>0:                                              #      *****                            54321
    temp = hang                                            #      ****                             4321
    while temp>0:                                          #      ***                              321 
        print("*",end="")                                  #      **                               21
        temp -=1                                           #      *                                1
    print()
    hang -= 1
   

#2.使用"#"号输出一个长为6长方形,用户可以指定宽,如果宽为4,长为6,则输出一个横着有6个"#",竖着有4个"#"的长方形(为了方便对比)   
                                              #输入6
                                                           # 结果:                    原本结果非$:
num2=int(input(""))                                        #      $$$$$$                           654321
while num2>0:                                              #      $$$$$$                           654321
    num=6                                                  #      $$$$$$                           654321
    while num>0:                                           #      $$$$$$                           654321
        print("$",end="")                                  #      $$$$$$                           654321 
        num -=1                                            #      $$$$$$                           654321
    print()                                      
    num2 -=1                            

#区别:多了一个temp/num
#"temp"会随着"hang"的变化而变化;但"num"不会变化.即双方行数都是不变的情况下,"num"的列是固定输出的,"temp"的列是不断减少的,
#这就形成了倒三角形




'''
解析:(假设输入5)

hang =int(input(""))        #第一步:赋值                    
while hang>0:               #第二步:hang=5                    #第八步:hang=4                     #第十三步:hang=3            
    temp = hang             #第三步:temp=hang=5               #第九步:temp=hang=4                #第十四步:temp=hang=3       
    while temp>0:                                          
        print("*",end="")   #第四步:输出5个"*"                #第十步:输出4个"*"                 #第十五步:输出3个"*"        
        temp -=1            #第六步:temp=temp-1 {54321}       #第十一步:temp=temp-1 {4321}       #第十六步:temp=temp-1 {321}     
        print()                   (直到小于0,结束循环)                (直到小于0,结束循环)                (直到小于0,结束循环)
    hang -= 1               #第七步:hang=4=hang-1             #第十二步:hang=3=hang-1             #第十七步:hang=2=hang-1      
                                                            
'''
i = 5
while i >= 0:
    temp = i
    while temp > 0:
        print("*", end="")
        temp -= 1
    print("*")
    i -= 1




print("\t")

i_2 = 0
while i_2 <= 5:
    wemp_1 = i_2

    while wemp_1 >= 0:

        wemp_1 -= 1
        print("*",end="")
    print()
    i_2 += 1