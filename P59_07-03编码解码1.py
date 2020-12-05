"""
二进制:

---->ASCII:只能存英文和拉丁字符.一个字符占一个字节,8位
------->gb2312:只能6700多个中文，1980
---------->hbk1.0: 存了2万多字符,1995
--------------->GB18030:2000,27000中文

---------------->unicode：utf-32： 一个字符占4个字节
---------------->unicode：utf-16： 一个字符占2个字节或2个以上 ,65535，




import  sys
print(sys.getfilesystemencoding())

b = bytes = 字节类型[0-255] 纯数字的数据类型
encode 在编码的同时,会把数据转成byte类型

                         unicode

      uncode↓ ↑decode              uncode↓ ↑decode

       utf-8                              GBK

 GBK转换UTF-8
 1.GBK     通过编码decode 转换 unicode
 2.unicode 通过解码encode 转换utf-8



"""