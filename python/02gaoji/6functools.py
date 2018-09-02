#coding=utf-8

# functools
import functools

# 查看functools模块中的方法和属性
print(dir(functools))
'''
['WRAPPER_ASSIGNMENTS', 'WRAPPER_UPDATES', '__builtins__', '__doc__', '__file__', '__name__', '__package__', 'cmp_to_key', 'partial', 'reduce', 'total_ordering', 'update_wrapper', 'wraps']
'''

# funtools模块中的partial方法 偏函数
def showarg(*args,**kw):
	print(args)
	print(kw)

fun1 = functools.partial(showarg,1,2,3)
fun1()
'''
(1, 2, 3)
{}
'''
fun1(4,5,6)
'''
(1, 2, 3, 4, 5, 6)
{}
'''
fun1(a='python',b='hello')
'''
(1, 2, 3)
{'a': 'python', 'b': 'hello'}
'''

# functools模块的wraps方法:用在装饰器中



# =========================
# === pdb : python自带的调试工具
# =========================
'''
以pdb工具去调试一个py文件: python -m pdb test.py
l -> list 显示当前执行的代码
n -> next 向下执行一行代码
c -> continue 继续执行代码(执行到下一个断点处)
b -> break 添加断点
clear -> 删除断点
p -> print 打印一个变量的值
a -> args 打印所有的形参数据
s -> step 进入一个函数
r -> return 直接执行到函数的最后一行
q -> quit 退出凋试

b   -> 列表显示所有断点
b 7 -> 在第7行添加断点
clear 1 ->删除由b添加的第1个断点
s -> 进入当前执行的方法
p a ->查看当前行的a变量的值
a -> arg

'''