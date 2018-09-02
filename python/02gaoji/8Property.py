#coding=utf-8

# -----------------------------
# attrName = property(getAttr,setAttr) 
# @peoperty @attrName.setter
# ----------------------------
# 原本私有属性要用getter与setter方法,但property可以直接让其访问私有属性
class PropertyTest(object):
	def __init__(self,num,money):
		self.__num = num
		self.__money = money

	# 第一种property方式: 代表setter与getter
	def getMoney(self):
		return self.__money
	def setMoney(self,money):
		self.__money = money
	money = property(getMoney,setMoney)

	# 第二种property方式:用装饰器
	@property
	def num(self):
		return self.__num
	@num.setter
	def num(self,num):
		self.__num = num

pt = PropertyTest(10,1000)
print(pt.money)
print(pt.num)
pt.money = 10000
pt.num = 100
print(pt.money)
print(pt.num)

