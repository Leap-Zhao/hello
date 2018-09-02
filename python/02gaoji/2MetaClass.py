#coding=utf-8

# 元类 /类也是一个类对象 ;
# type
# __class__
# __metaclass__


# 动态创建类: type(类名, 由父类名称组成的元组（针对继承的情况，可以为空），包含属性的字典（名称和值）)

# 普通创建类
class Test1(object):
	pass
test1 = Test1();

# 用type创建Test2类
Test2 = type("Test2",(),{})
test2 = Test2()

# 用type创建带属性和方法的类,且继承于Test1类
def printNum(self):
	print("---num: %d--" % self.num)

Test3 = type("Test3",(Test1,),{"printNum":printNum,"num":100})
test3 = Test3()
test3.printNum()

# __class__ 检测是哪个类的实例
print("test1.__class__ : %s " % test1.__class__)
print("test2.__class__ : %s " % test2.__class__)
print("test3.__class__ : %s " % test3.__class__)
print("Test3.__class__ : %s " % Test3.__class__)


# __metaclass__  决定类创建的过程,如果写了,则根据metaclass来创建 (了解即可)
def upper_attr(future_class_name, future_class_parents, future_class_attr):
    
    #遍历属性字典，把不是__开头的属性名字变为大写
    newAttr = {}
    for name,value in future_class_attr.items():
        if not name.startswith("__"):
            newAttr[name.upper()] = value

    #调用type来创建一个类
    return type(future_class_name, future_class_parents, newAttr)

class Foo(object):
	# 以下为python2代码
    __metaclass__ = upper_attr #设置Foo类的元类为upper_attr
    bar = 'bip'

#以下为python3中元类用法: 设置Foo类的元类为upper_attr
'''
class Foo(object,metaclass=upper_attr):
    bar = 'bip'
'''

print("hasattr(Foo, 'bar'): %s" % hasattr(Foo, 'bar'))
print("hasattr(Foo, 'BAR'): %s" % hasattr(Foo, 'BAR'))

f = Foo()
print("f.BAR : %s" % f.BAR)



# -------------------------
# 进制与位运算 (了解即可)
# -------------------------
# 进制: 二进制,八进制,十进制,十六进制
'''
# 原码,反码,补码
# 正数: 原码 = 反码 = 补码
# 负数: 原码 = 符号位为1,其它位为正数的原码
#       反码 = 符号位不变,其它位取反
#       补码 = 反码 + 1
# 负数的补码转原码规则: 符号位不变,其它位取反,再+1

1 的原码: 0000 0000 0000 0001
-1的原码: 1000 0000 0000 0001
-1的反码: 1111 1111 1111 1110
-1的补码: 1111 1111 1111 1111

反码,补码用于解决加法
-1 + 1 = (-1的补码) + (1的补码)

十进制->二进制: bin(num)   bin(18) -> 0b10010
十进制->八进制: oct(num)   oct(18) -> 0o22
十进制->十六进制: hex(num) hex(18) -> 0x12

二进制->十进制: int('0b10010',2) -> 18
八进制->十进制: int('0o22',8) -> 18
十六进制->十进制: int('0x12',16) -> 18

位运算: &按位与,|按位或,^按位异或,~按位取反,<<按位左移,>>按位右移

按位与: 只要有一位是0,则就是0 (有0则0)
按位或: 只要有一位是1,则就是1 (有1则1)
按位异或: 只要两位不同就为1,相同为0 
按位取反: 1变0,0变1

'''

# -----------------------------
# attrName = property(getAttr,setAttr) 
# @peoperty @attrName.setter
# ----------------------------
# 原本私有属性要用getter与setter方法,但property可以直接让其访问私有属性
class ProTest(object):
    def __init__(self):
        self.__num = 100
        self.__money = 1000

    # 第一种property方式: 代表setter与getter
    def setNum(self,num):
        self.__num = num
    def getNum(self):
        return self.__num
    num = property(getNum,setNum)

    # 第二种property方式:用装饰器
    @property
    def money(self):
        return self.__money
    @money.setter
    def money(self,money):
        self.__money = money


proTest = ProTest()
print("num is %d" % proTest.num)
print("money is %d" % proTest.money)
proTest.num = 200
proTest.money = 2000
print("num is %d" % proTest.num)
print("money is %d" % proTest.money)


# ---------------------------
# 小面试题
# 交换两个变量的值(仅用这两个变量) 
# --------------------------
# python中的写法 : a,b = b,a
# 其它语言中的写法 : a = a+b ; b = a-b; a = a-b;