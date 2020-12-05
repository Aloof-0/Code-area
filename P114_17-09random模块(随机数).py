# random随机数模块

import random

# 随机0-1得浮点数
print(random.random())

# 随机整形
print(random.randint(1,8))
print(random.randrange(1,8))   # 与randint一样 不过不包含8

#（3）随机返回
print(random.choice(['123','abc',52,[1,2]]))    # 随机返回参数列表中任意一个元素
'''结果：
abc
'''

print(random.sample(['123','abc',52,[1,2]],2))  # 随机返回参数列表中任意两个元素，参数二指定返回的数量
'''结果：
['123', 52]
'''


# 验证码函数
import random
def y():
    kkk = ""
    for i in range(5):
        if i == random.randint(0,2):
            C = str(random.randrange(1, 10))
        else:
            C = str(chr(random.randrange(65, 91)))
        kkk +=C
    print(kkk)
y()


# 验证码函数(最好)

def yb():
    ab = ""
    for i in range(5):
        add = random.choice([random.randrange(1, 10),chr(random.randrange(65, 91))])
        ab += str(add)
    print(ab)
yb()