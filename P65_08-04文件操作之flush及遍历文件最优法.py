# 1.flush() 方法是用来刷新缓冲区的，即将缓冲区中的数据立刻写入文件，同时清空缓冲区，不需要是被动的等待输出缓冲区写入。
#        1.一般情况下，文件关闭后会自动刷新缓冲区，但有时你需要在关闭前刷新它，这时就可以使用 flush() 方法。
#        2.不用f.close()即可将内容写进文件中
#        3.flush参数主要是刷新， 默认flush = False，不刷新，如上面例子，print到f中的内容先存到内存中，当文件对象关闭时才把内容输出到 123.txt 中；而当flush = True时
#        4.它会立即把内容刷新存到 123.txt 中。

import time
print("Loading",end = "")
for i in range(30):
    print(".",end = '',flush = True)
    time.sleep(0.2)

# 2. truncate() 方法用于截断文件并返回截断的字节长度。
#   指定长度的话，就从文件的开头开始截断指定长度，其余内容删除；不指定长度的话，就从文件开头开始截断到当前位置，其余内容删除。

f = open("尼采01.txt","r+",encoding="utf-8")     # 这里的的模式如果是"w"   则全删除了 但是这个文件的光标还会到它参数的位置上
                                                 # w打开进行写入，首先截断文件 'w'       open for writing, truncating the file first
f.truncate(5)                                    # 注意 这里UTF-8的中文字符占3个字节
f.close()

# 可与seek()使用
f = open("尼采01.txt","r+",encoding="utf-8")
f.seek(10)                                       # 指针到指定位置
f.truncate()                                     # 再删除余下的
f.close()

# 3.with() 方法用于更加简介的打开文件
with open('尼采','r') as f:
    f.readline()
    f.read()             # 不用close
            #同时管理多个文件对象
with open('尼采','r') as f_03 , open('尼采','w') as f_3:
    f.readline()
    f.read()











'''
修改数据的方法

f_read  = open('尼采01.txt','r',encoding = 'utd-8')
f_write = open('尼采01.txt','a+',encoding = 'utd-8')

number = 0
for line in f_read:
    number += 1
    if number == 5:
        line = "hellow,world"
    f_write.write(line)
f_read.close()
f_write.close()


'''