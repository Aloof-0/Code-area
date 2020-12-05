age_of_princal = 56#校长的年龄

guess_age = int(input("校长的年龄:"))
'''
伪代码(思路)
if guess_age == age_of_princal then 
print("yes")


else if   guess_age > age_of_princal:
print("你应该往小里试")

elif
print("NO")
'''
if   guess_age == age_of_princal:       #如果        ##输入年龄==实际年龄
    print("yes,你明白了.")              
elif guess_age > age_of_princal:        #否则        ##输入年龄>实际年龄
    print("大了")
else:                                   #不然的话    ##输入年龄<实际年龄
    print("小了")

score = int(input("成绩:"))

if score>=90:                          #如果你的成绩大于等于90的话
    print("A")                         #则为"A"
elif score>=80:                        #如果你的成绩大于等于80的话
    print("B")                         #则为"B"
elif score>=70:                        #如果你的成绩大于等于70的话
    print("C")                         #则为"C"
elif score>=60:                        #如果你的成绩大于等于60的话
    print("D")                         #则为"D"
else:                                  #不然的话
    print("滚")                        #你可以滚滚了







'''
注意:
1.elif可以无限增长,可以把他看成一个个等级
2.elif会从上往下判断条件,从上到下只执行一个结果

'''