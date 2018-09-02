#coding=utf-8


# ---------------------------
# 生成器 
# (x for x in range)  yield next() __next__() send
# --------------------------
# 列表生成式(这个不是生成器)
myListA = [x*2 for x in range(10)]
print(myListA) # [0,2,4,6,8,10,12,14,16,18]

# 在Python中，一边循环一边计算的机制，称为生成器：generator
# 只需把列表生成式的[] 换为()
myGen = (x*2 for x in range(10)) 
print(myGen) # <generator object <genexpr> at 0x....> 
# next(myGen) 生成下一个元素 或者myGen.__next__() 两者等价
print(next(myGen)) # 0
print(myGen.__next__()) # 2
next(myGen) # 4
myGen.__next__() # 6
# ...
next(myGen) # 18

# 斐波那契数列的前5个数
# 加了yield就成了生成器,返回yield后的变量
def fiBoNaQie():
	a,b=0,1
	for i in range(5):
		yield b
		a,b = b,a+b
print(fiBoNaQie()) # <generator object fiBoNaQie at 0x....>
# 如何用这个生成器,返回yield后的变量
fiBoGen = fiBoNaQie()
next(fiBoGen) # 1
next(fiBoGen) # 1
fiBoGen.__next__() # 2
next(fiBoGen) # 3
next(fiBoGen) # 5

# 如何输出生成器
for num in fiBoGen:
	print(num),
#1 1 2 3 5

# send ,如果yield 前有一个接收的变量,那么send可以传这个参数 
def fiBoNaQie2():
	a,b=0,1
	for i in range(5):
		temp = yield b
		print(temp)
		a,b = b,a+b
fiBoGen2 = fiBoNaQie2()
next(fiBoGen2) # None 1
fiBoGen2.__next__() # None 1
print(fiBoGen2.send("haha")) # haha 2

# 生成器的作用 
# 完成多任务 : 协程 (此外还有进程,线程)
def test1():
	while True:
		print("----1----")
		yield None

def test2():
	while True:
		print("----2----")
		yield None
# 生成器对象
# t1 = test1()
# t2 = test2()
# while True:
# 	next(t1)
# 	next(t2)


# ---------------------------
# 迭代器 
# 可以被next()函数调用并不断返回下一个值的对象
# --------------------------

# 什么对象是可迭代的?
# 1.可迭代对象Iterable : str,list,tuple,dict,set
# 2.迭代器Iterator : 生成器(生成器又包括列表生成器和函数生成器),iter()方法转成的迭代器

# 注:生成器一定是迭代器,但迭代器不一定是生成器

# 判断是否是一个可迭代对象
# 1.可以用for循环试一下(不推荐)
# 2.isinstance(obj,collections.Iterable)
from collections import Iterable 
isIterable = isinstance("abc",Iterable) 
print(isIterable) # True
# isinstance([],Iterable)  # True

# 如何判断是否是迭代器对象?
# 1.可以用next()函数试一下
# 2.isinstance(obj,collections.Iterator)
from collections import Iterator
isIterator = isinstance((x for x in range(10)),Iterator)
print(isIterator) # True
# isinstance([],Iterator) # False

# iter() 方法可以把一个可迭代对象转换成迭代器,
# 比如list原本占用内存较大,iter(list)后转成了迭代器对象(也可说是生成器),这时用多少占用多少内存
# isinstance(iter(a),Iterator) # True 




