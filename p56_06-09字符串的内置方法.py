'''
string的内置方法
* 1. count       统计元素个数
  2. capitloize  首字母大写
  3. center      居中
  4. endswith    判断是否以某个内容结尾
  5. starswith   判断是否以某个内容开头
  6. expandtabs  增加空格   配合  /t   和  (tabsize = 20)
  7. find        查找第一个元素,并将索引值返回
  8. rfind       查找最后一个元素 并将索引值返回
  9. format      格式化输出的另一种方法 {}
 10. format_map  格式化输出的另一种方法 (字典)
 11. index       查找,与find一样,会报错
                 12.  isalnum      是否由字母与数字组成
                 13.  isdecimal    判断是否是十进制字符    字符串前面要加U
                 14.  isdigit      与isnumeric一样        判断是否为数字
判断             15.  isidentfier
                 16.  islower      判断是否为小写
                 17.  isupper      判断是否为大写
                 18.  isspace      判断是否只由空格组成
                 19.  istitle      是否首字母大写
20.  lower       替换全部为小写
21.  upper       替换全部为大写
'''


#1.      count()方法用于统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置.
str = "this is string example....wow!!!"
print(str.count("s"))                  #统计"s"在str出现的次数                                           >>>3

#2.     capitalize()将字符串的第一个字母变成大写,其他字母变小写.
str02 = "this is string example from runoob....wow!!!"
print("str02.capitalize() : ", str02.capitalize())    #将str02的首字母大写                              >>>str02.capitalize() :  This is string example from runoob....wow!!!

#3      center() 返回一个原字符串居中,并使用空格填充至长度 width 的新字符串。默认填充字符为空格.
str03 = 'oh my god'                        #str03.center(长度,元素B)
print(str03.center(50, '*'))               #将字符串居中,两边用元素B填充 元素B不能为空                    >>>********************oh my god*********************

#4.     endswith() 方法用于判断字符串是否以指定后缀结尾，如果以指定后缀结尾返回True，否则返回False。可选参数"start"与"end"为检索字符串的开始与结束位置.  （结束于)
#       startswith() 方法用于检查字符串是否是以指定子字符串开头，如果是则返回 True，否则返回 False。如果参数 beg 和 end 指定值，则在指定范围内检查       （开始于）
str04 = "this is string example....wow!!!"
suffix = "wow!!!"
print(str.endswith(suffix))
print(str.endswith(suffix, 20))      #20是指定位置 即str04的第20元素为止
suffix = "is"
print(str.endswith(suffix, 2, 4))
print(str.endswith(suffix, 2, 6))

#5.    expandtabs() 方法把字符串中的 tab 符号('\t')转为空格，tab 符号('\t')默认的空格数是 8.           （仅仅是加空格,没什么卵用）
str05 = "this is\tstring example....wow!!!";
print("Original string: " + str05)                     #默认是加8个                                  >>>Original string: this is	string example....wow!!!
print("Defualt exapanded tab: " +  str05.expandtabs()) #不做任何变化
print("Double exapanded tab: " +  str05.expandtabs(16))#仅仅是转换空格不能加其他元素                 >>>Double exapanded tab: this is         string example....wow!!!

#6.    find() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，如果包含子字符串返回开始的索引值，否则返回-1。
#      index()与find()方法一样，只不过如果str不在 string中会报一个异常。       fine返回-1     index报错
str06 = "happy"
print(str06.find("y"))                        # 注意find 只找第一个元素"a"                         >>>4
print(str06.find("z"))                        # 如果找不到,则返回-1                                >>>-1
print(str06.find("a",1))                      # "1"是指str06里面"a"的索引位置                      >>>1
print(str06.find("a",3))                      # 如果"a"在str06里面"3"不是str06的位置,则返回-1      >>>-1 注意str.find("y",位置) 如果它是 就返回1 如果不是则返回-1

#7. str.format()  ，它增强了字符串格式化的功能。基本语法是通过 {} 和 : 来代替以前的 % .    格式化的另一种方式
#   str.format_map()与format()一样 但一个是变量格式,一个是字典格式
str07 = "I am is {name}"                     # 大括号只是一个特殊的内容
print(str07.format(name="God"))              # >>>I am is God

stra7 = "I am is {name}"
print(stra7.format_map({'name':"God"}))     #  >>>I am is God

#8. isalnum() 方法检测字符串是否由字母和数字组成.                                                                          isXXX都是判断语句  ,它返回 True 和 Flash
str08 = "爱abc0222"                        # 中文也可以
print(str08.isalnum())                     # 如果是则返回一个True
stra8 = "$$$love"
print(stra8.isalnum())                     # 如果不是则返回一个Flash

#9. isdecimal() 方法检查字符串是否只包含十进制字符。这种方法只存在于unicode对象。      注意:定义一个十进制字符串，只需要在字符串前添加 'u' 前缀即可。
str09 = u"this2009"
print(str.isdecimal())                      # 不是则返回False
stra = u"23443434"
print(str.isdecimal())                      # 是则返回True

#10. isdigit()方法检测字符串是否只由数字组成。          如果字符串只包含数字则返回 True 否则返回 False。      浮点数也不行,必须是整形
str10 = "225313"
print(str10.isdigit())                      # 是数字则True
stra10 = "abc1000"
print(stra10.isdigit())                     # 非数字则False

#11.  isidentifier() 方法用于判断字符串是否是有效的 Python 标识符，可用来判断变量名是否合法。
print( "中国123a".isidentifier() )                             # >>>True
print( "".isidentifier() )                                     # >>>Flash
print( "_a".isidentifier() )                                   # >>>True

#12. islower() 方法检测字符串是否由小写字母组成。
#    isupper() 方法检测字符串是否由大写字母组成。
#    istitle() 方法检测字符串首字母是否大写.
str012 = "THIS is string example....wow!!!";
print(str012.islower())                                          # >>>False

#13.  swapcase() 方法用于对字符串的大小写字母进行转换。        大写变小写 小学变大写
str013 = "Abc"
print(str013.swapcase())                                         # >>>aBC

#14. join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
str014 = "-"
seq = ["a", "b", "c"]                                        # 字符串序列
print(str014.join(seq))                                      # >>>a-b-c

#15. ljust() 返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串。如果指定的长度小于字符串的长度则返回原字符串       字符在左
#    ljust() 返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串。如果指定的长度小于字符串的长度则返回原字符串        字符在右
str15 = "love"
print(str15.ljust(15,"#"))                                   # >>> love###########
print(str15.rjust(15,"#"))                                   # >>> ###########love

#16. strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。                        注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。换行符也可以去掉
#   lstrip() 去掉左边的空格和换行符
#   rstrip() 去掉右边的空格和换行符
str16 = "      l l     \n" # 换行符
print(str16.lstrip())                                         # >>> l l                              去掉空格和换行符

#17. replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次                替换    str.replace(old, new[, max])
str17 = "MY love"
print(str17.replace("love","bad"))                            #