# coding=utf-8

'''
========================================
=========语法基础重点==============
========================================
'''

# python变量和类型

# 1.python是弱类型语言,可以在定义变量时不指定其类型

# 数字类型 Numbers:int(有符号整型),long(长整型),float(浮点型),complex(复数型)
# 布尔类型 Boolean:True,False
# 其它类型 String(字符串),List(列表),Tuple(元组),Dictionary(字典)
# 查看变量类型的方法: type(变量)

# 怎么查看所有关键字
print("=======查看所有关键字===========");
import keyword	
print(keyword.kwlist)

# 输入函数:raw_input("input your age");返回的都是字符串
age = raw_input("input your age:");
print("your age is %s ,and type is %s" % (age,type(age)));
# input your age:18
# your age is 18 ,and type is <type 'str'>

# //(取整除) 与 /(除法) 的区别
# 除法/中:只要有一个浮点数,结果就是浮点数,两个整数相除结果是整数
# 取整除//中:返回商的整数部分 9//2 输出结果 4 , 9.0//2.0 输出结果 4.0, 9.0//2 返回4.0

# 逻辑运算符: and(与),or(或),not(非),例子; x and y,x or y, not x

# 循环嵌套
'''输出:
*
* *
* * *
* * * * 
* * * * *
'''
print("while实现")
i=1;
while i<=5:
	j=1
	while j<=i:
		print("* "),
		j+=1
	print("")
	i+=1
print("for实现")
for i in range(1,6):
	for j in range(0,i):
		print("*"),
	print("")

print("第二种方式:");
i=1
while i<=5:
	print("* "*i)
	i+=1

# break 和 continue
# break/continue只能用在循环中，除此以外不能单独使用
# break/continue在嵌套循环中，只对最近的一层循环起作用

# 时间函数
import time
# time.time()返回从1970至今的秒数,返回类型为<type 'float'>
timeFrom1970 = time.time()
# localtime():返回<type 'time.struct_time'>类型,结构化时间类型
timeStructure = time.localtime(timeFrom1970)
# asctime(): 返回<type 'str'> 
timeStr = time.asctime(timeStructure)

print(timeFrom1970)  
# 1523580786.016
print(timeStructure) 
# time.struct_time(tm_year=2018, tm_mon=4, tm_mday=13, tm_hour=8, tm_min=53, tm_sec=58, tm_wday=4, tm_yday=103, tm_isdst=0)
print(timeStr) 
# 'Fri Apr 13 08:53:58 2018'



'''
========================================
=========语法进阶重点==============
========================================
'''

# 1.字符串str
# 1.1 raw_input() 与 input()函数的区别:
# input()中输入数字,则返回值是数字类型,而raw_input返回的总是字符串类型,在input的输入中不能输入字符串(会报错),只能输入数字

'''
input your age: 50
>>> type(age)
<type 'int'>
>>> hello = input("input your name:")
input your name:feiyue
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<string>", line 1, in <module>
NameError: name 'feiyue' is not defined
>>> hello = raw_input("input your name:")
input your name:feiyue
>>> hello
'feiyue'
'''

# 1.2 将一个字符串反序遍历,比如"abcde" 输出 "edcba"
myStr = "abcde"
# 用while实现
k  = len(myStr)-1
while k>=0:
	print(myStr[k]),
	k -= 1
print("")
# 用for实现
for i in range(len(myStr)-1,-1,-1):
	print(myStr[i]),
print("")
# 最简单的方法
print(myStr)
print(myStr[::-1])


# 2.列表,元组,字典
# 列表(有序,可修改,可重复)
# 元组(有序,不可修改,可重复)


# 3.函数
# 3.1 不定长参数(传列表或者元组)
# 3.2 缺省参数/默认参数(参数有一个默认值)
# 3.3 局部变量和全局变量(global)
# 3.4 递归函数(完成阶乘函数和FiBoNaqie函数)
# 3.5 匿名函数(lambda表达式) -> 用lambda表达式写两个数的乘积
# 3.6 常用的类型转换的函数


def test(*args,num=1):
	for i in range(0,num):
		for ele in args:
			print(ele)


qiuhe = lambda a,b: a*b

def jiecheng(n):
	if n > 1:
		return n * jiecheng(n-1)
	else:
		return 1

def feibonaqie(n):
	num1 = 1
	num2 = 1
	if n < 2:
		retuen 1
	else:
		return feibonaqie(n-1) + feibonaqie(n-2)
'''
fibo(5) = fibo(4) + fibo(3)
	    = [ feibo(3) + fibo(2) ]+ [ fibo(2) + fibo(1) ]
	    = [ fibo(2) + fibo(1) ]+ fibo(2) + fibo(2) + fibo(1)
'''


