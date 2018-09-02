#coding=utf-8

# 单例模式Singleton
# 单例模式，是一种常用的软件设计模式。在它的核心结构中只包含一个被称为单例的特殊类。通过单例模式可以保证系统中，应用该模式的类一个类只有一个实例。即一个类只有一个对象实例

class Singleton(object):
	# 在创建类实例的时候调用__new__
	# 创建类实例的时候,如果没有实例,则创建一个实例,并赋值给instance类属性
	# 创建类实例的时候,如果有实例,则直接返回instance类属性对应的那个实例 
	def __new__(cls):
		if not hasattr(cls, "instance"):
			cls.instance = super(Singleton, cls).__new__(cls)
		return  cls.instance

if __name__ == "__main__":
	obj1 = Singleton()
	obj2 = Singleton()

	print(id(obj1))
	print(id(obj2))
	obj1.attr1 = "value1"
	print(obj1.attr1,obj2.attr1)
	print obj1 is obj2