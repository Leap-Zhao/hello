#coding=utf-8

from threading import Thread
import time

# define a global variable
g_var = 100

def work1():
	global g_var
	for i in xrange(3):
		g_var += 1
	print("---In work1,g_var is %d" % g_var)

def work2():
	global g_var
	print("---In work2,g_var is %d" % g_var)

def main():
	print("---In main,g_var is %d " % g_var)
	t = Thread(target=work1)
	t.start()
	time.sleep(1)
	t2 = Thread(target=work2)
	t2.start()

if __name__ == '__main__':
	main()

# 线程间通信: 线程之间共享全局变量
# 如果不同线程之间对同一个全局变量进行修改,则会不按照预想的那样执行,无法保持操作的原子性(详情看8)
# 解决不同线程原子性问题的方法有:1.轮询(效率不高) 2.互斥锁

# result
'''
---In main,g_var is 100 
---In work1,g_var is 103
---In work2,g_var is 103
'''