#coding=utf-8


# ======================
# ===== 多任务
# =======================
# os.fork() os.getpid() os.getppid()
# 注意，fork函数，只在Unix/Linux/Mac上运行，windows不可以
# fork()方法用于创建一个新的进程

import os
import time	

ret = os.fork()
# 执行完上一句,主进程(父进程)会调用fork方法创建一个子进程,且子进程从创建位置开始执行
# 注: 父进程的返回值大于0,创建的子进程的返回值等于0
if ret==0:
	# 子进程
	while True:
		print("----1. son process and pid: %d----" % os.getpid())
		time.sleep(1)
else:
	# 父进程
	while True:
		print("----2. father process and pid: %d----" % os.getpid())
		time.sleep(2)

# os.getpid() os.getppid()
# getppid() 为子进程得到的父进程pid

# 注:用fork创建的子进程,如果主进程结束了,不会因为子进程没结束还等待,会结束当前程序,但子进程会继续执行完
# 注:用multiprocessing的Peocess类创建的子进程,主进程会等待子进程执行结束后才会结束,与fork不同


# 每执行一次fork(),当前进程会创建一个子进程,所以,执行n次fork(),总共会有2的n次方个进程
# frok炸弹:创建无数个进程,导致主机崩溃
'''
while True:
	os.fork()
'''
