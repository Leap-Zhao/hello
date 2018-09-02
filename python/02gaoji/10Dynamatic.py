#coding=utf-8


#==========================
#=== python语言的动态性
#==========================
# python是动态语言,可以在程序运行时对代码进行修改

class DynamicClassTest(object):
	CLASSNAME = "DCT"
	def __init__(self,param1,param2):
		self.param1	= param1
		self.param2 = param2

# 动态性表现:给已创建的对象实例添加一个属性
dct1 = DynamicClassTest(1,2)
print(dct1.param1)
print(dct1.param2)
# 给dct对象添加一个属性param3,别的实例对象并没有此属性
dct1.param3 = 3
print(dct1.param3)

# 动态性表现: 给类添加一个属性,类和实例都可以用此属性
DynamicClassTest.param4 = 4
dct2 = DynamicClassTest(11,22)
print(dct1.param4) 
print(dct2.param4)



def hello():
	print("hello")
def run(self):
	print("%s 正在运行" % self.param1)

@staticmethod
def staticFun():
	print("---static method---")

@classmethod
def printParam1(cls):
	print("classname : %s" % cls.CLASSNAME)

# 注:实例对象不可添加带self参数的方法,因为实例对象不会自动将其类与方法绑定
#    如果是一般的不带self的方法,是可以的
#	 假如要给实例对象绑定带self参数的方法,可以用types.MethodType(funName,instanceName)
dct1.hello = hello
dct1.hello()

'''
# 虽然dct1实例的run属性已经指向了run方法,但由于dct1实例并不会自动传给self形参,所以会报缺少参数的错
dct1.run = run
dct1.run()
# 可以用types模块的MethodType()方法
import types
dct1.run = types.MethodType(run,dct1)
dct1.run()
# 注:此只有dct1实例有run方法,其它实例对象没有此方法
'''

# 动态性表现: 给类添加一个类方法,类和实例都可调用
DynamicClassTest.printParam1 = printParam1
DynamicClassTest.printParam1()
dct1.printParam1() # DCT

# 动态性表现: 给类添加一个静态方法,类和实例都可调用
DynamicClassTest.staticFun = staticFun
DynamicClassTest.staticFun()
dct2.staticFun()

# 动态性的作用: 在不更新某个软件或系统的版本下,对软件或系统内部的一些元素进行动态修改
# 例如: 淘宝的app有时不更新版本,打开却是最新活动的样子

# ===========================
# ==== __slots__
# ===========================
# 如果不希望对类或实例对象动态添加属性或方法,用__slots__可以对此作出规定
class DynamicClassTestTwo(object):
	# 动态添加只能添加__slots__元组中的属性或方法
	__slots__ = ("paraName","funName")
	pass

dctt1 = DynamicClassTestTwo()
# 下面这句会报错
# dctt1.name = "hello"
dctt1.paraName = "hello"
print(dctt1.paraName)

