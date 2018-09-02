#coding=utf-8

# GarbageCollection 垃圾回收机制

# 1.小整数对象池 [-5,256]已经提前创建好,同一个小整数用一个内存
'''
>>> a = 100
>>> id(a)
38824288L
>>> b = 100
>>> id(b)
38824288L
'''
smallNum1 = 100
smallNum2 = 100
smallNum3 = 100
# a,b,c用同一个内存地址
print("id(smallNum1): %s" % id(smallNum1))
print("id(smallNum2): %s" % id(smallNum2))
print("id(smallNum3): %s" % id(smallNum3))

# 2.大整数对象池 每一个大整数,在用时才去创建一个新的对象
'''
>>> a = 10000
>>> id(a)
44676160L
>>> b = 10000
>>> id(b)
44676136L
'''
bigNum1 = 10000
bigNum2 = 10000
bigNum3 = 10000
print("id(bigNum1): %s" % id(bigNum1))
print("id(bigNum2): %s" % id(bigNum2))
print("id(bigNum3): %s" % id(bigNum3))

# 3.intern机制 普通字母组成的字符串用一个内存
'''
>>> a = "helloworld"
>>> b = "helloworld"
>>> id(a)
44419280L
>>> id(b)
44419280L
'''

# =========垃圾回收 第二部分===========\
# 1.引用计数 : python用
# 有优点,有缺点
# 2.标记清除 Ruby用
# 3.隔代回收 : 处理python中循环引用的问题
# 总结: python的垃圾回收机制以引用计数为主,以隔代回收/分代回收为辅