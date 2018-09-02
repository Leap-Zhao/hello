#coding=utf-8

# 面向对象 

# 类
'''
class 类名:
	属性
	方法
'''

print("-"*30)
print("----面向对象基础----")
print("-"*30)

class Dog:
	# 属性
	# 前面加__(两个下划线)时表示此属性私有

	# 公共属性, 类属性
	color="white"
	# 私有属性sex
	__sex = "gong"
	# 私有属性age : 只能在本类中用,不能在子类中用
	__info = "haha"

	# 构造方法 /对象创建时做的事情
	def __init__(self,age):
		# 实例属性, 
		self.__age = age;

	# 析构方法(析构函数) :对象销毁时做的事情 
	# del 可以销毁一个对象
	def __del__(self):
		print("object %s is over...." % self.name)

	#公共方法,也是实例方法
	def setName(self,name):
		# self.属性 相当于添加一个新属性
		self.name = name
	def getName(self):
		return self.name

	def getAge(self):
		return self.__age
	def setAge(self,age):
		self.__age = age

	def eat(self):
		print("%s is eating" % self.name)
	def run(self):
		print("%s is running" % self.name)

	# 私有方法(只能在类中用)
	def __getInfo(self):
		return self.__info
	def showInfo(self):
		print("info : %s" % self.__getInfo())

	# 用方法访问私有属性
	def showSex(self):
		print("sex is %s" % self.__sex)

	#类方法,必须要有@classmethod,且必须都有cls形参
	@classmethod
	def setColor(cls,color):
		cls.color = color

	#类方法:创建多个实例
	@classmethod
	def createManyDog(cls):	
		tempList = []
		# 多创建了两个实例
		tempList.append(Dog())
		tempList.append(Dog())
		return tempList

	#静态方法,必须要有@staticmethod,但可以没有参数
	@staticmethod
	def testStaticMethod():
		print("this is a static method")



# 创建对象
jinMao = Dog(16)
hashiqi = Dog(18)

jinMao.setName("jinMao")
hashiqi.setName("hashiqi")

# 调用方法
jinMao.eat()   # jinMao is eating
hashiqi.run() # hashiqi is running 

# 销毁对象,访问析构函数
del hashiqi  # object hashiqi is over...

# 公共属性可以直接调用,也可以修改属性
print(jinMao.color) #white
print(jinMao.name) # jinMao
 
# 如果通过对象去修改类属性,那么python会自动给这个对象创建一个和类属性相同名字的实例属性
jinMao.color ="black"
print(jinMao.color) # black 这个是实例属性,并不是类属性
print(jinMao.getName()) #jinMao

# 私有的属性不可以直接调用和修改
# print(jinMao.sex) 第
jinMao.showSex()

# 通过公共方法访问私有方法
jinMao.showInfo()

# 访问构造方法传的参数
print("age is %d" % jinMao.getAge())

# 类属性,实例属性
# 如果通过对象去修改类属性,那么python会自动给这个对象创建一个和类属性相同名字的实例属性
# 要想修改类属性, 需用 类名.类属性 = 新的值  , Dog.color = "pink"

'''
# 类方法,实例方法,静态方法的区别
# 定义上的区别:
	实例方法:定义上必须用self代表实例本身,可以通过 self.实例属性 调用实例属性,本质上不可以调用类属性,因为 self.类属性 会在该实例中生成一个同名的实例属性,不改变类属性的值.
	类方法: 定义上必须用cls代表类本身,可以通过 cls.类属性 访问类属性.本质上不可以调用实例属性,因为 cls.实例属性 会在该类中生成一个同名的类属性,不改变之前实例属性的值
	静态方法: 定义上不用写self或cls,不可以访问类属性,也不可以访问实例属性
	总结: 在实际开发中,我们应做到,在实例方法只访问实例属性,在类方法中只访问类属性,在静态方法不要访问实例属性和类属性

# 调用上的区别:
	实例对象肯定可以调用实例方法,但是却也可以调用类方法和静态方法
	类对象肯定可以调用类方法,经实验,它也可以调用静态方法,但不能调用实例方法
	总结: 在实际开发中,我们应做到,实例对象调用实例方法,类对象调用类方法,而静态方法呢,实例与类对象都可以调用,但一般由类对象调用

# 对象和类都可以调用类方法,但最好用类调用
# 对象和类都可以调用静态方法,但最好用类调用
# 实例方法只能用对象/实例调用,不能用类调用

# 静态方法的作用:
https://www.cnblogs.com/pinking/p/7944376.html
'''

Dog.setColor("pink")  #jinMao.setColor("pink") 也可以
print("Dog color is %s" % Dog.color)


print("-"*30)
print("----面向对象进阶----")
print("-"*30)

# 父类,基类 : 猫类 Cat
class Cat:

	def __init__(self,newName,newAge):
		self.__name = newName
		self.__age = newAge	
		print(" this is the constructor method of Cat class")

	def miaomao(self):
		print("cat is calling")

	def catch(self): 
		print("cat is catching mouse")

# 子类: 波斯猫 BosiCat
class BosiCat(Cat):

	# 重写:重写父类中的方法
	def __init__(self,weight):
		# 如何在子类重写方法中调用父类的同名的方法
		Cat.__init__(self,newName,neaAge)
		self.__weight  = weight
		print("this is the constructor method of BosiCat class")

	# 定义子类中独特的方法
	def naoyangyang(self):
		print("Bosi cat is naoyangyang")

	def getWeight(self):
		return self.__weight

# 多继承 class C(A,B): 如果类A与类B中有同名的方法(子类C中没有),类C调用方法时用写在前面那个类的方法

bosiCat = BosiCat("bosicat",100,6)



