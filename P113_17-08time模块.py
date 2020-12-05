#Python 日期和时间
'''
时间戳         结构化时间                       格式化时间                   常用函数 datetime()
time.time（） time.localtime()        time.strftime()  time.strptime()      datetime.datetime.now()

Python 程序能用很多方式处理日期和时间，转换日期格式是一个常见的功能。
Python 提供了一个 time 和 calendar 模块可以用于格式化日期和时间。
时间间隔是以秒为单位的浮点小数。
每个时间戳都以自从1970年1月1日午夜（历元）经过了多长时间来表示。
Python 的 time 模块下有很多函数可以转换常见日期格式。如函数time.time()用于获取当前时间戳, 如下实例:
'''
# 2.时间元组？
'''
很多Python函数用一个元组装起来的9组数字处理时间:

序号	字段	    值
0	4位数年  	    2008
1	月	            1 到 12
2	日	            1到31
3	小时	        0到23
4	分钟	        0到59
5	秒	0到61       (60或61 是闰秒)
6	一周的第几日	    0到6 (0是周一)
7	一年的第几日	    1到366 (儒略历)
8	夏令时	-1, 0, 1, -1是决定是否为夏令时的旗帜
'''
# 3.上述也就是struct_time元组。这种结构具有如下属性：
'''
序号	属性	    值
0	tm_year	        2008
1	tm_mon	        1 到 12
2	tm_mday	        1 到 31
3	tm_hour	        0 到 23
4	tm_min	        0 到 59
5	tm_sec	        0 到 61 (60或61 是闰秒)
6	tm_wday	        0到6 (0是周一)
7	tm_yday	        1 到 366(儒略历)
8	tm_isdst	    -1, 0, 1, -1是决定是否为夏令时的旗帜
'''
import time


#     (1).获取当前时间  localtime()
localtime = time.localtime()
print( "本地时间为 :", localtime)

#      (2).获取格式化的时间  asctime()
print(time.asctime( time.localtime()))
print(time.ctime())
print(time.ctime(121534546))  # 把你的时间戳加上1234564564 再格式化时间


# 格式化日期

#      (1).格式化成2016-03-20 11:45:39形式        strftime(格式,本地时间)
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

#      (2).格式化成Sat Mar 28 22:24:24 2016形式   strftime()
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

#       还可以这样得到                             strptime(格式化时间,格式) 就可以任意取值   == strptime("2019-01--01 18:16:13",格式)
c = time.asctime( time.localtime())             #  >>> Mon Oct  7 23:20:14 2019
a = time.strptime(c,"%a %b %d %H:%M:%S %Y")

print(a.tm_min)
print(a.tm_hour)

# 常用  datetime
import datetime
print(datetime.datetime.now())