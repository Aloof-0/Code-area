# -*- coding: utf-8 -*-
# @Time    : 2019/11/6 17:41
# @Author   : 高冷
# @FileName  : P124_18-10re模块二.py

import re
# 1.search()方法  扫描整个字符串并返回第一个成功的匹配。               //返回的是一个对象不是值
"""
参数	描述
pattern	匹配的正则表达式
string	要匹配的字符串。
flags	标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。
匹配成功re.search方法返回一个匹配的对象，否则返回None。
"""
first = re.search('ak', 'ak47')
print("1.", first)

# 2.group()方法   用来提出分组截获的字符串,()用来分组对象转换为值      //即,把对象转换为值

first1 = re.search('lol', 'let me play the lol game')               # 方法一
print(first1.group())

frist2 = re.search('game', 'let me play the lol game').group()      # 方法二
print(frist2)
