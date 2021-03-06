#3.九九乘法表    

"""
  #伪九九乘法表(倒三角)

hang=9
while hang > 0:
    lie=1
    while lie<=hang:
        print(str(hang)+"*"+str(lie)+"=",hang*lie," ",end="")
        lie += 1
    print()
    hang -= 1
    


结果:
9*1= 9  9*2= 18  9*3= 27  9*4= 36  9*5= 45  9*6= 54  9*7= 63  9*8= 72  9*9= 81
8*1= 8  8*2= 16  8*3= 24  8*4= 32  8*5= 40  8*6= 48  8*7= 56  8*8= 64
7*1= 7  7*2= 14  7*3= 21  7*4= 28  7*5= 35  7*6= 42  7*7= 49
6*1= 6  6*2= 12  6*3= 18  6*4= 24  6*5= 30  6*6= 36
5*1= 5  5*2= 10  5*3= 15  5*4= 20  5*5= 25
4*1= 4  4*2= 8  4*3= 12  4*4= 16
3*1= 3  3*2= 6  3*3= 9
2*1= 2  2*2= 4
1*1= 1



步骤:
hang = 9                           #第一步:赋值                                  #第七步:赋值

while hang > 0:                    #第二步:hang=9                                #第八步:hang=8
    lie=1                          #第三步:lie=1(列是固定的)                     #第九步:lie=1
    while lie<=hang:               
        print(....)                #第四步:输出hang*lie (9*1=9,9*2=18...9*9=81)  #第十步:输出hang*lie (8*1=8,8*2=16...8*8=64)   
        lie += 1                   #第五步:lie=lie+1     {1,2,3,4,5,6,7,8,9}     #第十一步:lie=lie+1   {1,2,3,4,5,6,7,8}
    print()                         (直到大于9,结束循环,执行下一步)              (直到大于8,结束循环,执行下一步)                                 
    hang -= 1                      #第六步:hang=8                                #第十二步:hang=7
"""


   #真九九乘法表(长方型)
hang = 9                     
while hang>0:                
    lie = 9                  
    while lie >0:            
        print(...)           
        lie -= 1             
                             
    print()
    hang-=1
'''    
结果:
9*9= 81  9*8= 72  9*7= 63  9*6= 54  9*5= 45  9*4= 36  9*3= 27  9*2= 18  9*1= 9
8*9= 72  8*8= 64  8*7= 56  8*6= 48  8*5= 40  8*4= 32  8*3= 24  8*2= 16  8*1= 8
7*9= 63  7*8= 56  7*7= 49  7*6= 42  7*5= 35  7*4= 28  7*3= 21  7*2= 14  7*1= 7
6*9= 54  6*8= 48  6*7= 42  6*6= 36  6*5= 30  6*4= 24  6*3= 18  6*2= 12  6*1= 6
5*9= 45  5*8= 40  5*7= 35  5*6= 30  5*5= 25  5*4= 20  5*3= 15  5*2= 10  5*1= 5
4*9= 36  4*8= 32  4*7= 28  4*6= 24  4*5= 20  4*4= 16  4*3= 12  4*2= 8   4*1= 4
3*9= 27  3*8= 24  3*7= 21  3*6= 18  3*5= 15  3*4= 12  3*3= 9   3*2= 6   3*1= 3
2*9= 18  2*8= 16  2*7= 14  2*6= 12  2*5= 10  2*4= 8   2*3= 6   2*2= 4   2*1= 2
1*9= 9   1*8= 8   1*7= 7   1*6= 6   1*5= 5   1*4= 4   1*3= 3   1*2= 2   1*1= 1
步骤:
hang = 9                     #第一步:赋值,hang=9
while hang>0:                
    lie = 9                  #第三步:赋值,lie=9
    while lie >0:            
        print(...)           #第四步:输出hang*lie(9*9=81,9*8=72..9*1=9)
        lie -= 1             #第五步:lie=lie-1 (9,8,7,6,5,4,3,2,1)
                             
    print()
    hang-=1
'''
hang=9
while hang>0:
    lie=9
    while lie>0:
        print(str(hang)+"*"+str(lie)+"=",hang*lie," ",end="")
        lie-=1
    
    
    print(hang)
    hang-=1




