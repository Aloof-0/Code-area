#猜数字
age_of_princal = 56#校长的年龄
print("校长的年龄:")
guess_age = int(input(">>:"))
'''
伪代码(思路)
if guess_age == age_of_princal then 
print("yes")
elif
print("NO")
'''
if guess_age == age_of_princal:   #!!!这很重要:::
    print("yes,你明白了.")
else:
    print("NO,这是不对的.")


'''                        #为什么要缩进：
if,else的格式:              意思是
if  XXX:                    如果IF成立
 (缩进)AAA                  执行AAA
else:                       如果else不成立
 (缩进)BBB                  执行BBB
#注意:
1.缩进级别必须保持一致
2.官方规定只能4个空格
3.可以按tab键直接跳进,但tab键!=4个空格
'''