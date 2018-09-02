# 1.print的区别
# python2: print("")或print('')或print '';
# python3: print("")或print('');不再支持print ''

# 2.print不换行输出的区别
# python2: print "", 或 print(""),
# python3: print("",end="") 或 print(str,end="") ; end=""可使输出不换行

# 3.输入函数的区别
# python2 : raw_input("input your name") 返回 str类型,而input("input your age:")返回int数字类型,且只能输入数字,输入字符串报错
# python3 : 没有raw_input()方法了,input("input your name") 返回str类型,

# 4.range()方法的区别
# python2中range()方法返回一个列表,此外,还有一个xrange(),节省内存空间
# python3中的range()方法返回一个迭代对象range,如果想让其变成列表,则用list(range(..))方法

# 4.在生成器Generator 中运用next() 函数问题 
# python2 中只能用next(myGen)方法
# python3 中next(myGen)方法或myGen.__next__()方法

# 5.元类metaclass的用法不同
'''
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

class Foo(object,metaclass=upper_attr):
    bar = 'bip'
'''

# 6.reduce()方法
# 在python2中,reduce在__bulidin__模块中,自动导入
# 在python3中,reducey方法被放置在functools模块里,使用时要先导入from functools import reduce
# reduce(lambda x,y:x+y,[1,2,3,4])  #  1+2+3+4 = 10

# 7.*args的用法
# python2中:
'''
>>> grades = [1,2,3,4,5,6,7,8,9]
>>> first,*middle,last = grades
  File "<stdin>", line 1
    first,*middle,last = grades
          ^
SyntaxError: invalid syntax
'''

'''
>>> grades = [x for x in range(1,10)]
>>> grades
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> first, *middle, last = grades
>>> middle
[2, 3, 4, 5, 6, 7, 8]
'''

# 8.队列Queue类的导入
# python2的Queue在Queue模块中: from Queue import Queue
# python3的Queue在queue模块中: from queue import Queue

# 9.urllib2模块 在 python3.x 中被改为urllib.request

# 10. 除法/与整数除//的区别
# 不管是py2还是py3,整数除//都是一样的,返回的都是整数,不过,如果除数与被除数都是int,则返回的是int,如果其中有一个float,则返回的整数是float类型
# 例如, 9//2 = 4 , 9.0//2 = 4.0, 9.0//2.0 = 4.0
# 除法/在py2与py3是不一样的,在py2中,若除数与被除数都是int,则返回的也是int类型(结果只取整),若其中有一个是float,则返回的是float(结果正确),而在py3中,不管有没有float,结果都是float(正确的结果)
# 例如, 在py2中,9/2= 4 ,8/2=4,而在py3中 9/2= 4.5,8/2=4.0不管是py2还是py3,9.0/2=4.5,8.0/2=4.0