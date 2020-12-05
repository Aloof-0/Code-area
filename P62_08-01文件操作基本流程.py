"""文件操作基本流程

1.能调用方法的一定是对象           对象.方法

2.             li    =     [1,2,3]
               li    .     append(2)
             (对象)  .     (方法)

3.文件读和写不能并存

4."写"操作        会(1).清空原来的文本
                   (2).填上你写的内容
                   (3).即使你不写内容或写一个空值都会清空
                   (4).即使你没有这个文件,都会自动创建这个文件

5.模式    可做操作     若文件不存在    是否覆盖
r         只能读       报错            -
r+        可读可写     报错            是
w         只能写       创建            是
w+　      可读可写     创建            是
a　　     只能写       创建            否，追加写
a+        可读可写     创建            否，追加写

6.close()   就是把缓冲区的数据存到磁盘里 就算不close()python也会自动关上

7.最好的修改数据（f = open(xxxx)）

h
"""

# 1.open() 函数用于打开一个文件，创建一个 file 对象，相关的方法才可以调用它进行读写。
#         open(name[, mode[, buffering]])                              open("名字","模式","缓冲").方法
          #方法一
UAD = open("草稿本.txt",'r',encoding='utf8').read()
print(UAD)
         #方法二
UAD01 = open("草稿本.txt",'r',encoding='utf8')                      #打开
fa = UAD01.read()                                                   #操作
print(fa)
UAD01.close()

# 2.close() 方法用于关闭一个已打开的文件。关闭后的文件不能再进行读写操作， 否则会触发 ValueError 错误。 close() 方法允许调用多次。
#          当 file 对象，被引用到操作另外一个文件时，Python 会自动关闭之前的 file 对象。 使用 close() 方法关闭文件是一个好的习惯。
UAD02 = open("草稿本.txt",mode ='r',encoding='utf8')                      #打开
da = UAD02.close()                                                  #操作
print(da)                                                           #关闭   >>>None

# 3.read() 方法用于从文件读取指定的字节数，如果未给定或为负则读取所有。
#语法  对象.read(4)       >>>4代表着阅读4个字节 如果继续 print(UAD03.read(5)) 的话 则打印下5个字节
UAD03 = open("草稿本.txt",'r',encoding='utf8')
print(UAD03.read(5))              #打印到第五个字节
print(UAD03.read(5))              #第五个到第十个字节
UAD03.close()

# 4.write() 方法用于向文件中写入指定字符串。
#          在文件关闭前或缓冲区刷新前，字符串内容存储在缓冲区中，这时你在文件中是看不到写入的内容的。
#          如果文件打开模式带 b，那写入文件内容时，str (参数)要用 encode 方法转为 bytes 形式，否则报错：TypeError: a bytes-like object is required, not 'str'。
UAD04 = open("尼采.txt",mode = 'w',encoding='utf8')
UAD04.write('每一个不曾起舞的日子,都是对生命的辜负')
UAD04.close()

# 5.模式a() 模式用于增加内容。
#         "增加" 与 "写" 不同  , "写"是覆盖 "增加"是增加
UAD05 = open("尼采01.txt",mode = "a",encoding="utf8")
UAD05.write("智慧愿我们——勇敢、无忧、矜高、刚强，她是一个女人，永远只爱着战士。")
UAD05.close()

# 6.readline() 方法用于从文件读取整行，包括 "\n" 字符。如果指定了一个非负数的参数，则返回指定大小的字节数，包括 "\n" 字符。
       #方法1:按行取,默认第一行,如果继续 print(DAD06.readline()) 的话 则打印下一行
DAD06 = open("尼采01.txt",'r+',encoding='utf8')
print(DAD06.readline())                  #第一行
print(DAD06.readline())                  #第二行
DAD06.close()
       #方法2:如果添加参数,则为读取的字符串为X
DAD06_1 = open("尼采01.txt",'r+',encoding='utf8')
print(DAD06_1.readline(5))
DAD06_1.close()

# 7.readlines() 方法用于读取所有行(直到结束符 EOF)并返回列表，该列表可以由 Python 的 for... in ... 结构进行处理。如果碰到结束符 EOF 则返回空字符串。  一串字符串做成一个列表
DAD07 = open("尼采01.txt",'r+',encoding='utf8')
print(DAD07.readlines())            #默认返回全部列表
DAD07.close()
       #用for循环输出列表
DAD07_1 = open("尼采01.txt",'r+',encoding='utf8')
for abc in DAD07_1.readlines():
    print(abc)                     #如果加.strip()则唔空行
DAD07_1.close()

# 8.tell() 方法返回文件的当前位置，即文件"指针"当前位置。

DAD08_1 = open("尼采01.txt",'r+',encoding='utf8')
print(DAD06_1.tell())                 # >>>0
print(DAD06_1.read(10))
print(DAD06_1.tell())                 # >>>30  英文占1个 中文占3个
DAD08_1.close()
# 9.seek() 方法用于移动文件读取指针到指定位置。
DAD09_1 = open("尼采01.txt",'r+',encoding='utf8')
DAD09_1.seek(10)              # 指针到10开始操作, 也就是10字节开始
print(DAD09_1.readline())
DAD09_1.close()

"""
    （1）f.seek(p,0)  移动当文件第p个字节处，绝对位置
    （2）f.seek(p,1)  移动到相对于当前位置之后的p个字节
    （3）f.seek(p,2)  移动到相对文章尾之后的p个字节
"""