#coding=utf-8



'''
装饰器知识
1.闭包
  |---1.1 简单闭包
  |---1.2 内层函数带参数,带返回值的闭包
2.函数装饰器(用函数写的装饰器)
  |----2.1 装饰简单函数
  |----2.2 多个装饰器的封装顺序和调用顺序
  |----2.3 装饰带参数,带返回值的函数
  |----2.4 通用装饰器
  |----2.5 装饰器本身带参数(三层嵌套)
3.类装饰器(用类写的装饰器)
  |----3.1 __call__ 与 @className
'''



# -----------------------------
# 闭包
# -----------------------------
# 函数里面定义了一个函数,并且这个函数用到了外边函数的变量,那么这个函数以及用到的一些变量称之为闭包

def test_out(number):
	print("----test-out-start----")

	def test_in():
		print("----test-in----")
		print(number+100)

	print("----test-out-end----")
	return test_in

result = test_out(100)
result()
# 输出
'''
----test-out-start----
----test-out-end----
----test-in----
200
'''

# 注:外层函数一定有返回值(返回内层函数),参数可以可无,但最好有,因为没有参数时闭包作用不大

# 接下来是内层函数带参数,带返回值的闭包

def test_out2(number1):
	print("-----test_out2_start----")
	def test_in2(number2):
		print("----test_in2_start----")
		print(number1+number2)
		return "---这是带返回值的函数---"
	print("-----test_out2_end----")
	return test_in2

test_in2 = test_out2(10)
print(test_in2(20))
# 输出
'''
-----test_out2_start----
-----test_out2_end----
----test_in2_start----
30
---这是带返回值的函数---
'''



# -------------------------------
# 函数装饰器
# --------------------------------

# 在不改变testFun函数名字的情况下给其函数增加功能
# 运用python中的装饰器模式

def wrapperFun(func):
	def wrapperIn():
		print("----这是增加的功能----")
		func()
	return wrapperIn

@wrapperFun
def test1Fun():
	print("----test1Fun----")

test1Fun()

'''
原理:
print("----装饰之前----")
test1Fun()
print("----装饰之后----")
test1Fun = wrapperFun(test1Fun)
test1Fun()
'''

# 当运行两个及以上的装饰器函数时,调用顺序
def wrapper2Fun(func):
	def wrapperIn():
		print("----这是第二个装饰器函数")
		func()
	return wrapperIn

# 只要python解释器执行到了这个代码,那么就会自动的进行装饰,而不是等到调用时才装饰
@wrapperFun
@wrapper2Fun
def test2Fun():
	print("----test2Fun----")

test2Fun()
'''
答:
先装饰了下面的wrapper2Fun,再装饰了上面的wrapperFun,
但先调用了上面那个wrapperFun,再调用了wrapper2Fun函灵敏

装饰器装饰是从下往上装,调用是从上往下调用的,递归调用
test2Fun中调用wrapperFun,wrapperFun中调用wrapper2Fun

装饰时是倒装的(从下住上),调用/执行时是正常调用/执行的(从上往下)

执行顺序类似:
test2Fun = wrapper2Fun(test2Fun)
test2Fun = wrapperFun(test2Fun)
test2Fun()

最后输出:
----这是增加的功能----
----这是第二个装饰器函数
----test1Fun----

'''
def wrapper3Fun(func):
	print("不调用也会执行装饰器wrapper3Fun")
	def wrapperIn():
		print("----这是第三个装饰器函数")
		func()
	return wrapperIn

def wrapper4Fun(func):
	print("不调用也会执行装饰器wrapper4Fun")
	def wrapperIn():
		print("----这是第四个装饰器函数")
		func()
	return wrapperIn

# 只要python解释器执行到了这个代码,那么就会自动的进行装饰,而不是等到调用时才装饰
@wrapper3Fun
@wrapper4Fun
def test3Fun():
	print("----test3Fun----")
# 没有调用test3Fun但仍会输出装饰的东西
'''
输出:
不调用也会执行装饰器wrapper4Fun
不调用也会执行装饰器wrapper3Fun

如果调用了test3Fun(),则输出:
不调用也会执行装饰器wrapper4Fun
不调用也会执行装饰器wrapper3Fun
----这是第三个装饰器函数
----这是第四个装饰器函数
----test3Fun----
'''
test3Fun()

print("")
print("------------------------------------------")
print("---调用含参数的函数和不定长参数的函数装饰器-----")
print("------------------------------------------")

# 调用含参数的函数和不定长参数的函数
def wrapper5Fun(func):
	def wrapperIn(*args,**kwargs):
		print("添加了装饰器")
		func(*args,**kwargs)
	return wrapperIn

@wrapper5Fun
def test4Fun(a,b,c):
	print("a=%d b=%d c=%d" % (a,b,c))

@wrapper5Fun
def test5Fun(a,b,c,d):
	print("a=%d b=%d c=%d d=%d" % (a,b,c,d))

test4Fun(11,22,33)
test5Fun(44,55,66,77)

print("")
print("------------------------------------------")
print("---调用含返回值的函数装饰器-----")
print("------------------------------------------")

# 调用含2个固定长参数的函数和返回值的函数
def wrapper6Fun(func):
	def wrapperIn(a,b):
		print("添加了装饰器")
		returnValue = func(a,b)
		return returnValue
	return wrapperIn

@wrapper6Fun
def test5Fun(a,b):
	print("a=%d b=%d " % (a,b))
	return '这是一个有返回值的函数'

result = test5Fun(44,55)
print(result)

print("")
print("------------------------------------------")
print("------通用的函数装饰器-----")
print("------------------------------------------")

# 定义一个通用的函数装饰器(不管被装饰的函数有没有参数和返回值,都可装饰)
def wrapper7Fun(func):
	def wrapperIn(*args,**kwargs):
		print("添加了装饰器")
		returnValue = func(*args,**kwargs)
		return returnValue
	return wrapperIn

@wrapper7Fun
def test6Fun(a,b):
	print("a=%d b=%d " % (a,b))
	return '这是一个有参数,有返回值的函数'

@wrapper7Fun
def test7Fun():
	print("这是一个参数,无返回值的函数")

result = test6Fun(44,55)
print(result)
test7Fun()


print("")
print("------------------------------------------")
print("------装饰器带参数的函数装饰器-----")
print("------------------------------------------")
# 当装饰器需要带参数(而不是被装饰的函数),这时需要在闭包外再进行封装,三层函数嵌套,两层闭包
# 带有装饰的装饰器,能够起到"在运行时有不同功能"的作用
def wrapperOut(arg):
	def wrapperIn_out(func):
		def wrapperIn(*args,**kwargs):
			print("添加了装饰器,此装饰器有个参数arg = %s" % arg)
			returnValue = func(*args,**kwargs)
			return returnValue
		return wrapperIn
	return wrapperIn_out

@wrapperOut('haha')
def test8Fun(a,b):
	print("a=%d b=%d " % (a,b))
	return '这是一个有参数,有返回值的函数'

result = test8Fun(12,13)
print(result)

print("")
print("")


# -------------------------------
# 类装饰器
# --------------------------------
# 知识点: @ClassName  __call__ 方法


class Test(object):
	def __init__(self,func):
		print("----Test Class Init----")
		print("the func name is %s" % func.__name__)
		self.__func = func

	def __call__(self):
		print("this is a class decorator")
		self.__func()

@Test
def test():
	print("this is test function")


print("---after execute test functon---")
test()



