#coding=utf-8

# 文件相关
# 打开文件 文件对象 = open(文件名,访问模式)
# 关闭文件 文件对象.close()

# 读数据 str = 文件对象.read(num)  
# num表示要从文件中读取的数据的长度（单位是字节），如果没有传入num，那么就表示读取文件中所有的数据
# 按行读取数据 list = 文件对象.readlines()
# str = 文件对象.readline()  读取一行数据
# 就像read没有参数时一样，readlines可以按照行的方式把整个文件中的内容进行一次性读取，并且返回的是一个列表，其中每一行的数据为一个元素
# 写数据 文件对象.write(内容)

# tell() :在读写文件的过程中，如果想知道当前的位置，可以使用tell()来获取
# seek(offset, from) : 定位到某个位置.offset:偏移量 from:方向(0:表示文件开头,1:表示当前位置2:表示文件末尾)
# 例子: 把位置设置为：从文件开头,偏移5个字节seek(5,0) 离文件末尾,3字节处seek(-3,2)

# 访问模式如下:
# r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
# w	打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
# r+ 打开一个文件用于读写。文件指针将会放在文件的开头。
# w+ 打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# a+ 打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。

# rb 以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。
# wb 以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# ab 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
# rb+ 以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
# wb+ 以二进制格式打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# ab+ 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。

file = open("test.txt","a+")
# win下文件中的换行是\r\n ,linux下是\n
file.write("\r\nhello world again")
file.close();

file = open("test.txt","r+")
content = file.read(5)
print("-"*30)
print("5char : %s " % content)
# 注意:read一次之后指针会停在read后的位置,下一次read时从指针位置读取
content2 = file.readline()
print("-"*30)
print("line : %s" % content2)
content3list = file.readlines()
print("-"*30)
print("readlines length : %d" % len(content3list))
file.seek(0,0)
content1 = file.read()
print("-"*30)
print("all: %s " % content1)
file.close()

# 文件的其它相关操作 os模块 
# import os
# 文件重命名 os.rename(需要修改的文件名, 新的文件名) 
# os.rename("毕业论文.txt", "毕业论文-最终版.txt")
# 创建文件 open("text.txt","w")
# 删除文件 os.remove(待删除的文件名)
# os.remove("毕业论文.txt")

# 文件夹的相关操作 os模块
# 创建单层文件夹 os.mkdir("文件夹名") 
# 创建多层文件夹 os.makedirs(".\\data\\mydirs")
# 注意:mkdir只能创建单层的文件夹,不能创建多层
# 删除文件夹 os.rmdir("文件夹名")
# 获取当前目录 os.getcwd()
# 改变默认目录 os.chdir("../")
# 获取目录列表 os.listdir("./")


# 捕获异常 try except finally
'''
try:
    num = 100
    print(num)
except (IOError,NameError):
	print("error")
else:
	print('没有捕获到异常，真高兴')
finally:
	print('我一定会执行的哦')
'''

# 在接收错误类型的后面定义一个变量(例如:errorMsg)用于接收具体错误信息,然后将接收的错误信息打印即可
try:
    print(num)
except NameError, errorMsg:
    print("error message: %s" % errorMsg); 
else:
	print("no error")

# 引发异常:raise语句 异常/错误对象必须有一个名字,且它们应是Error或Exception类的子类
# 自己定义一个异常
class ShortInputException(Exception):
	def __init__(self,length,atleast):
		Exception.__init__(self)
		self.length =length
		self.atleast = atleast

try:
	s = raw_input("请输入一个n位数字,位数小于3时抛异常")
	if len(s)<3:
		raise ShortInputException(len(s),3)
except EOFError:
	print('/n你输入了一个结束标记EOF')
except ShortInputException,x : #x这个变量被绑定到了错误的实例
	print('ShortInputException: 输入的长度为 %d,长度至少应是 %d' % x.length, x.atleast)
else:
	print("no error or exception")
# 模块
# 在Python中用关键字import来引入某个模块 import module1,mudule2...
# Python的from语句让你从模块中导入一个指定的部分到当前命名空间中 from modname import name1[, name2[, ... nameN]]
import math,os
# 导入模块fib的fibonacci函数 
from fib import fibonacci
# from modname import * 把一个模块的所有内容全都导入到当前的命名空间

# 当你导入一个模块，Python解析器对模块位置的搜索顺序是：
# 当前目录
# 如果不在当前目录，Python则搜索在shell变量PYTHONPATH下的每个目录。
# 如果都找不到，Python会察看默认路径。UNIX下，默认路径一般为/usr/local/lib/python/
# 模块搜索路径存储在system模块的sys.path变量中。变量里包含当前目录，PYTHONPATH和由安装过程决定的默认目录。

# 自定义模块test.py
# 可发现test.py中的测试代码，应该是单独执行test.py文件时，才应该执行的，不应该是其他的文件中引用而执行
# 为了解决这个问题，python在执行一个文件时有个变量__name__



