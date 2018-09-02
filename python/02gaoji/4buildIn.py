#coding=utf-8

# 内建属性和内建方法
# build-In-Parameter and build-In-function 

# 1.查询某个类的内建属性和方法 
# 内置函数 dir() 用于按模块名搜索模块定义，它返回一个排好序的字符串类型的存储列表
# dir() 函数不带参数时，返回当前范围内的变量、方法和定义的类型列表；带参数时，返回参数的属性、方法列表。如果参数包含方法__dir__()，该方法将被调用。如果参数不包含__dir__()，该方法将最大限度地收集参数信息。

# 当定义的类没有额外的属性和方法时,dir(ClassName)返回的即是内建属性和方法(即object类的属性和方法,但额外增了几个方法)
class BuildInClassTest(object):
	pass

print(dir(BuildInClassTest))
'''
['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']

'''

a = 100
print(dir(a))
'''
['__abs__', '__add__', '__and__', '__class__', '__cmp__', '__coerce__', '__delattr__', '__div__', '__divmod__', '__doc__', '__float__', '__floordiv__', '__format__', '__getattribute__', '__getnewargs__', '__hash__', '__hex__', '__index__', '__init__', '__int__', '__invert__', '__long__', '__lshift__', '__mod__', '__mul__', '__neg__', '__new__', '__nonzero__', '__oct__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdiv__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'imag', 'numerator', 'real']
'''


'''
常用专有属性		说明	             	触发方式
__init__		构造初始化函数	     	创建实例后,赋值时使用,在__new__后
__new__	    	生成实例所需属性	 	创建实例时
__class__		实例所在的类	     	实例.__class__
__str__	    	实例字符串表示,可读性	print(类实例),如没实现，使用repr结果
__repr__		实例字符串表示,准确性	类实例 回车 或者 print(repr(类实例))
__del__	    	析构					del删除实例
__dict__		实例自定义属性			vars(实例.__dict__)
__doc__	    	类文档,子类不继承		help(类或实例)
__getattribute__属性访问拦截器			访问实例属性时
__bases__		类的所有父类构成元素	类名.__bases__
''' 

# 2. __getattribute__ 属性访问拦截器
# 访问一个类的属性之前可以进行一些操作,将此操作放在__getattribute__方法中
# 坑: 不能在__getattribute__方法中调用self.xxx属性,因为有可能陷入无限循环
class Itcast(object):
    def __init__(self,subject1):
        self.subject1 = subject1
        self.subject2 = 'cpp'

    #属性访问时拦截器，打log
    def __getattribute__(self,obj):
        if obj == 'subject1':
            print('log subject1')
            return 'redirect python'
        else:   #测试时注释掉这2行，将找不到subject2
        	temp = object.__getattribute__(self,obj)
        	print("===>2 : %s" % str(temp))
        	return temp

    def show(self):
        print('this is show function')

s = Itcast("python")
print(s.subject1)
print(s.subject2)
s.show()

'''
log subject1
redirect python
===>2 : cpp
cpp
===>2 : <bound method Itcast.show of <__main__.Itcast object at 0x0000000002A4A828>>
this is show function

'''

# 3.内建方法
# range() xrange()
# python2中用range()方法,此外还有xrange()方法,两种不同的实现,python3中保留了xrange用法,并改名为range()
# python3中的range()返回一个迭代值,如果想变成列表,用list(range(5))方法,此range()相当于python2中的xrange()

print(range(0,10)) # 生成0-9的列表
print(xrange(6)) #xrange(6)

# map()方法
# map(函数,可迭代对象),返回对应的可迭代对象
mapTest = map(lambda x: x*x,[1,2,3])
print("type(mapTest): %s" % type(mapTest))
print("mapTest: %s" % mapTest)
'''
type(mapTest): <type 'list'>
mapTest: [1, 4, 9]
'''

'''
lambda函数需要一个参数x
>>> map(lambda x:x*x,[1,2,3])
[1, 4, 9]
lambda函数需要两个参数x,y
>>> map(lambda x,y:x+y,[1,2,3],[4,5,6])
[5,7,9]
'''
# map用在for循环
for index in map(lambda x,y:x+y,[1,2,3],[4,5,6]):
    print(index)

# map其它用法 (直接传递函数)
def mapFunTest(x,y):
    return (x,y)
list1 = [1,2,3,4]
list2 = ['A','B','C','D']
mapResult = map(mapFunTest,list1,list2)
print(type(mapResult)) # <type 'list'>
print(mapResult) # [(1, 'A'), (2, 'B'), (3, 'C'), (4, 'D')]


# filter() : 对指定序列执行过滤操作
filterTest = filter(lambda x:x>3,[1,2,3,4,5])
print(type(filterTest)) # <type 'list'>
print(filterTest)   #[4,5]
# filter(None,...) 不执行滤操作

# reduce(function,sequence) :依次从sequence中取出一个元素,和上一次function的结果做参数再次调用function
reduceTest = reduce(lambda x,y:x+y,[1,2,3,4])
print(type(reduceTest)) # <type 'int'>
print(reduceTest) # 10   (1+2+3+4)

print(reduce(lambda x,y:x+y,["aa","bb","cc"],"dd"))  # ddaabbcc

# sort() 排序函数,无返回值
a = [32,38,12,8,1]
print(a.sort()) # None
print(a)    # [1,8,12,32,38]
a.sort(reverse=True) # 倒序
print(a)    # [38, 32, 12, 8, 1]

# sorted()函数
b = [33,22,12,3,44]
print(type(sorted(b))) #<type 'list'>
print(sorted(b))  #[3, 12, 22, 33, 44]
print(b)  #[33, 22, 12, 3, 44]

# 注:sort()函数会修改被调用者,还sorted返回新的对象,不会修改原调用者的值