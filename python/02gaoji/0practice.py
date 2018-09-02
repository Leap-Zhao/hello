#coding=utf-8

# 1.类装饰器 class decorator
# @ClassName __call__方法
class ClassDecoratorTest(object):
	"""docstring for ClassDecoratorTest"""
	def __init__(self, funcName):
		super(ClassDecoratorTest, self).__init__()
		self.funcName = funcName
	def __call__(self):
		print("这是一个类装饰器")
		self.funcName()

@ClassDecoratorTest
def decoratorFunction():
	print('这是被类装饰器装饰的方法')

decoratorFunction()

# 2.元类 MetaClass
# type() __class__ __metaclass__

# 2.1用type创建一个类
def setNum(self,num):
	self.num = num
def printNum(self):
	print(self.num)
MetaClassTest = type("MetaClassTest",(object,),{"setNum":setNum,"printNum":printNum})
metaClassTest = MetaClassTest()
metaClassTest.setNum(11)
metaClassTest.printNum()

# 2.2__class__属性
print(metaClassTest.__class__)
print(MetaClassTest.__class__)

# 2.3 __metaclass__方法
def upperFunc(class_name,class_parent,class_attr):
	newAttrDict = {}
	for name,value in class_attr.items():
		if not name.startswith("__"):
			newAttrDict[name.upper()] = value

	return type(class_name,class_parent,newAttrDict)
class MetaClassTest2(object):
	__metaclass__ = upperFunc
	# 定义属性
	para1 = "hello"
	def printPara(self):
		print("world")

'''
class MetaClassTest2(object,metaclass=upperFunc):
'''
print(hasattr(MetaClassTest2,'para1'))
print(hasattr(MetaClassTest2,'PARA1'))
print(hasattr(MetaClassTest2,'printPara'))
print(hasattr(MetaClassTest2,'PRINTPARA'))

# 3.垃圾回收机制 GarbgeCollection
# 3.1小整数对象池
# 3.2大整数对象池
# 3.3intern机制
# 3.4引用计数机制为主,隔代回收为辅的垃圾回收机制

# 4.内建方法与内建属性 BuildIn-Parameter BuildIn-Function
# 4.1 __getattribute__(self,attrName)内建方法
class GetAttributeTest(object):
	"""docstring for GetAttributeTest"""
	def __init__(self, arg1,arg2):
		super(GetAttributeTest, self).__init__()
		self.arg1 = arg1
		self.arg2 = arg2
    
    def __getattribute__(self,attrName):
		if attrName == 'arg1':
			print("这是arg1的属性拦截")
			return "改变了arg1的值"
		else:
			temp = object.__getattribute__(self,attrName)
			print("这是其它属性的拦截")
			return temp

	def getArg2(self):
		return self.arg2

getAttributeTest = GetAttributeTest("hello","world")
print(getAttributeTest.arg1)
print(getAttributeTest.arg2)
getAttributeTest.getArg2()

# 4.2 range()方法和xrange()方法
# 4.3 map(),reduce(),filter()
print(map(lambda x:x*x,[1,2,3]))
print(reduce(lambda x,y:x*y,range(1,5)))
print(filter(lambda x:x%2==0,range(10)))

def mapFun(x,y):
	return x-y
# 4.4 sort() sorted()
listA = [23,22,26,10]
listA.sort()
print(listA)
listA.sort(reverse=True)
print(listA)
listC = sorted(listA)
print(listC)

# 5.集合set
tupleA = (1,1,2,2,3,3,4)
setA = set(tupleA)
print(setA)
print(tuple(setA))
# 交集 setA&setB
# 并集 setA|setB
# 差集 setA-setB
# 对称差集 setA^setB

# 6.functools
import functools
# functools.partial(funcName,paraList) 偏函数
def partialFunTest(a):
	print("a = %d" % a)

partialFun = functools.partial(partialFunTest,5)
partialFun()

# functools.wraps() 用在装饰器中

# 7 hashlib模块
import hashlib
md5HashObj = hashlib.md5()
md5HashObj.update("123456")
print(md5HashObj.hexdigest())


# 原码,反码,补码
# 正数: 原=反=补
# 负数: 原 = 符号位1,其它位为正数原
# 进制转换
'''
十->二 bin(num)
十->八 oct(num)
十->十六 hex(num)
二->十 int('',2)
八->十 int('',8)
'''


# hashlib







