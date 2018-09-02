#coding=utf-8

# 字符串str
print("============str=============")
# 数字类型输出
num3 = 3.14
print("num3 = %d" % num3); # num3 = 3
print("num3 = %f" % num3); # num3 = 3.140000  (%f浮点数默认6位小数)
print("num3 = %.2f" % num3); # num3 = 3.14  (%.2f修改小数点为2位)
# 字符串输入
# 1.raw_input()
# 2.input()  
# input()中输入数字,则返回值是数字类型,而raw_input是字符串类型
# 字符串索引与遍历
strIndexText = "abcdefg";
strIndexTextLength = len(strIndexText)

# 注意:python中的for循环只有for.in.. 没有for(;;)这种
for i in range(0,strIndexTextLength):
	print("%s"%strIndexText[i]),
print("")
# while正序遍历
k = 0
while k<strIndexTextLength:
	print(strIndexText[k]),
	k+=1 
print("")
# 反序遍历
k = strIndexTextLength-1
while k>=0:
	print(strIndexText[k]),
	k-=1
print("")


# strIndexText[0:3] 为选下标0(第1个)到下标3(第4个,但不包括)的子字符串,取的个数为3-0=3个
# strIndexText[2:] 为选下标2(第3个)到最后的子字符串,
# strIndexText[-3:] 为选从下标为-3(倒数第3个)字符到最后的子符串
# strIndexText[2:-1] 为选从下标2(第3个)到下标-1(倒数第1个,不包括此)字符的子符串

# 字符串常用函数
# str.find(subStr); //找到返回索引值,未找到返回-1
# str.find(subStr,n,m) //从索引值为n到m的子串中查找指定字符串
# mystr.rfind(str, start=0,end=len(mystr) ) 类似于 find()函数，不过是从右边开始查找.
# str.index(subStr); //和find有点类似,找到返回索引值,未找到直接抛出异常
# mystr.rindex( str, start=0,end=len(mystr)) 类似于 index()，不过是从右边开始.
# str.count(subStr) 输出str中存在多少个subStr,数字类型
# len(str)  输出str的长度值,数字类型
# str.replace(str1,str2,count)  将str1替换为str2,count为最多替换的次数,可以不写,返回的是替换后的字符串
# str.split(subStr,maxsplit)  //按subStr将str分切为一个列表[],maxsplit表示最多切的次数(可以不写),返回列表类型
# "hello\nworld".splitlines() 按照行分隔，返回一个包含各行作为元素的列表
# mystr.partition(str) 把mystr以str分割成三部分,str前，str和str后,返回元组类型
# mystr.rpartition(str) 类似于 partition()函数,不过是从右边开始.返回元组类型
# str.join(mystr) 以 str 作为分隔符，将 mystr 中所有的元素(若是字符串则为一个个字符,若是列表则是一个个元素)合并为一个新的字符串

# mystr.capitalize()  将mystr的首字母大写,返回字符串
# mystr.lower()  把mystr中所有的大写字母全部变为小写的,返回新的字符串
# mystr.upper()  把mystr中所有的小写字母全部变为大写的,返回新的字符串
# mystr.ljust(width)  返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串 
# mystr.rjust(width)  返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串 
# mystr.center(width) 返回一个原字符串居中对齐,并使用空格填充至长度 width 的新字符串
# mystr.lstrip() 删除 mystr 左边的空格,返回新的字符串
# mystr.rstrip() 删除 mystr 字符串末尾的空格

# mystr.startwith(str2); 判断mystr是否以str2开头,返回True或False 
# mystr.endwith(str2);   判断mystr是否以str2结尾,返回Ture或False
# mystr.isalnum() 如果 mystr 所有字符都是字母或数字则返回 True,否则返回 False
# mystr.isalpha() 如果 mystr 所有字符都是字母 则返回 True,否则返回 False
# mystr.isdigit() 如果 mystr 只包含数字则返回 True 否则返回 False.
# mystr.isspace() 如果 mystr 中只包含空格，则返回 True，否则返回 False.
# mystr.isupper() 如果 mystr 所有字符都是大写，则返回 True，否则返回 False

# 面试题: 反转一个字符串  str[::-1]
strTest = "abcdefg"
print(strTest[::-1])  # "gfedcba"

# 列表(可以存放不同类型的数据集合,里面的元素有序且可修改,可重复)
# 元组(可以存放不同类型的数据集合,里面的元素有序不可修改,可重复)
# 字典(键值对,键无序且不可修改不可重复,值可修改可重复)
print("===========列表list=======");
myList = ["xiaowang",100,3.14,100];

# 列表的遍历
# 第一种遍历方法
i=0;
while i<len(myList):
	print(myList[i]),
	i+=1;
print("")
# 第二种遍历方法
for i in range(0,len(myList)):
	print(myList[i]),
print("")
# 第三种遍历方法 (最简洁)
for ele in myList:
	print(ele),
print("")

# 列表的常用操作
# 增加元素 myList.append(element);
myList.append("newElement")
for ele in myList:
	print(ele),
print("")

# 删除元素 del(根据下标进行删除),pop(删除最后一个元素),remove(根据元素的值进行删除)
del myList[0]
for ele in myList:
	print(ele),
print("")

myList.pop()
for ele in myList:
	print(ele),
print("")

myList.remove(100)
for ele in myList:
	print(ele),
print("")

# 修改元素 myList[0] = "changeElement"
myList[0] = "changeElement"
for ele in myList:
	print(ele),
print("")

# 查找元素 in(存在),not in(不存在)
if 100 in myList:
	print("exit")
else:
	print("not exit in list")


# 字典
# 定义:没有排列顺序,是键值对,键不可重复,值可重复,值可通过键来修改
print("========字典dictionay==========")
myDict = {"name":"zhangsan","age":20,"addr":"beijing"};
print("name: %s, age: %d " % (myDict['name'],myDict['age']));

# 字典操作:添加字典元素
myDict["bir"] = "11-08"
# 字典操作:删除某一个字典元素用del,
# 字典操作:清空一个字典用clear()
del myDict['addr']
# myDict.clear();  //myDict的值变为{}
# 字典操作:修改元素 myDict['age'] = 30
myDict['name'] = "zhaosi"
myDict['age'] = 30
print("name: %s, age: %d " % (myDict['name'],myDict['age']));

# 字典操作: 查找元素
# keys() : 返回一个包含字典所有KEY的列表
if "name" in myDict.keys():
	print("has this key")
# has_key(key) : dict.has_key(key)如果key在字典中,返回True,否则返回False
if myDict.has_key("name"):
	print("method1: has the key of name")	
# values() : 返回一个包含字典所有value的列表
if "zhaosi" in myDict.values():
	print("has this value")
# items() : 返回一个包含所有（键,值）元祖的列表
if ("age",30) in myDict.items():
	print("has this item")

# 字典其它操作
# len() : 测量字典中键值对的个数
myDictLength = len(myDict);

# 字典的遍历
# 键的遍历 : 返回的键每一个都是字符串类型,
# 值的遍历 : 返回的值是对应的值类型(字符串,整数,等等)
# 键值对的遍历 : 返回的是一个元组类型 (键,值)
print("=====key:")
for keyName in myDict.keys():
	print(keyName)
print("=====value:")
for value in myDict.values():
	print(value)
print("=====item:")
for item in myDict.items():
	print(item)
for key,value in myDict.items():
	print(key)
	print(value)
for k,v in myDict.iteritems():
	print k,v

# items() 与iteritems()方法的区别
# 字典items()方法和iteritems()方法，是python字典的内建函数，
# items()方法返回元组类型组成的Python列表<type 'list'>,而iteritems()方法返回迭代器<type 'dictionary-itemiterator'>,迭代器每次迭代返回的也是元组
# iteritems()方法在需要迭代结果的时候使用最适合，而且它的工作效率非常的高


# 元组
# 元组(可以存放不同类型的数据集合,里面的元素有序不可修改,可重复)
myTuple = ('zhao',77,99.9)
# 访问元组 myTuple[0]
# 元组不可赋值修改
# 两个元组合并成一个 tup3 = tup1+tup2
# 元组中的单个元素值是不允许删除的,但我们可以使用del语句来删除整个元组
# del myTuple
# 元组索引
myTuple[2]  # 99.9  读取第三个元素
myTuple[-2] # 77 倒数第二个元素
myTuple[1:] # (77,99.9) 从第二个元素截取到最后一个,组成一个新的元组

# 元组内置函数
# cmp(tuple1, tuple2)   比较两个元组元素
# len(tuple)  计算元组元素个数
# max(tuple)  返回元组中元素最大值
# min(tuple)  返回元组中元素最小值
# tuple(list)  将列表转换为元组

# 序列 : 字符串,列表,字典,元组
# 序列操作: len() 返回序列中元素的个数
# 序列操作: for ele in 序列:
# 其中,字符串,列表,字典有切片操作,元组没有


# 函数
# 可以有返回值,也可以没有,可以有形参,也可以没有
def add():
	a = 1
	b = 2
	c = a+b
	print("%d = %d + %d" % (c,a,b))

def add2(a,b):
	c = a+b
	print("%d = %d + %d " % (c,a,b))

def add3(a,b):
	c = a+b
	return c 

# 函数调用 函数名()
add()
add2(2,4)
result = add3(4,6)
print(result)

# 计算1-num累积和的函数
def calculateSum(num):
	sum = 0
	i = 1
	while i<=num:
		sum+=i
		i+=1
	return sum

calculateResult = calculateSum(100)
print(calculateResult)

# 函数高级
# 1.不定长参数(一般用来传列表,元组,)
# 下面这个可以传0-n个参数
def test(*args):
	for ele in args:
		print(ele)

# 2.必须有的参数
# 下面这个函数可以传1->n个参数,第1个永远对应num1
def test2(num1,*args):
	print(num1)
	for ele in args:
		print(ele)

# 3.缺省参数 : 给参数加上一个默认值,让其可传可不传
# 下面这个函数可以传1个或2个参数
def test3(name,age=18):
	pass

# 函数调用可以指定参数名
test3(age=16,name="xiaoming")

# 函数中，可以有多个return语句，但是只要执行到一个return语句，那么就意味着这个函数的调用完成

# 函数应用
# 编写一个函数: 求n个数的和
def sumByN(n=1):
	sum1 = 0
	i=0
	while i<n:
		num = int(raw_input("请输入第%d个数 : " % (i+1)))
		sum1 += num
	return sum1
# 编写一个函数,求n个数的平均值
def aveByN(n=1):
	sum1 = sumByN(n)
	print("sum = %d " % sum1)
	average = sum1/float(n)
	print("average = %f" % average)

# 局部变量和全局变量
g_a = 100
def globalTest():
	# 怎么能在方法里改变一个全局变量的值呢
	# g_a = 200 这还是个局部变量,并不能改变全局变量,应该用global
	global g_a
	g_a = 200
	print("g_a = %d" % g_a)  #变为200

print("g_a = %d" % g_a)   # 变为200

# python中局部变量与其它语言的不同,但不推荐这么写
def localTest():
	local_a = 10
	if local_a > 9:
		local_b = 11
	# 在其它的语言里,下面这一句会报错,但python不会
	print("local_b=%d" % local_b) 
	if local_a < 4:
		local_c = 10
	# 下面这一句会报错,因为local_c并没有生成
	print("local_c=%d" % local_c)


# 函数递归
# 用递归的方式完成累加
def sumByRecursion(n):
	if n>1:
		result = n + sumByRecursion(n-1)
	else:
		result = 1
	return result
# 用递归的方式完成阶乘
def factorialByRecursion(n):
	if n>1:
		result = n*factorialByRecursion(n-1)
	else:
		result = 1
	return result 

# 匿名函数 lambda表达式(没有return,直接返回式子计算后的值)
sumByLam = lambda a,b:a+b
# 调用lambda表达式
# 调用方式1:先定义后调用
result = sumByLam(1,2)
print("sumByLam(1,2) = %d" % result)
print("sumByLam(3,4) = %d" % sumByLam(3,4))
# 调用方式2:直接定义且调用
print("mulByLam(3,4) = %d" % (lambda a,b:a*b)(3,4))

# 类型转换
# int(x [,base ])	将x转换为一个整数
# long(x [,base ])	将x转换为一个长整数
# float(x )	将x转换到一个浮点数
# complex(real [,imag ])	创建一个复数
# str(x )	将对象 x 转换为字符串
# repr(x )	将对象 x 转换为表达式字符串
# eval(str )	用来计算在字符串中的有效Python表达式,并返回一个对象
# tuple(s )	将序列 s 转换为一个元组
# list(s )	将序列 s 转换为一个列表
# chr(x )	将一个整数转换为一个字符
# unichr(x )	将一个整数转换为Unicode字符
# ord(x )	将一个字符转换为它的整数值
# hex(x )	将一个整数转换为一个十六进制字符串
# oct(x )	将一个整数转换为一个八进制字符串

# 进制书写方式
# 八进制(Octal) 0o377
# 十六进制(Hex) 0xFF
# 二进制(Binary) 0b11111111# 

# 位运算 
# & 按位与 ,| 按位或, ^ 按位异或, ~ 按位取反,<< 按位左移,>> 按位右移