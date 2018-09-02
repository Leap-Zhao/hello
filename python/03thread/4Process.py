#coding=utf-8

# 解决os.fork()不能在win上使用的办法
# 跨平台的方法multiprocessing.Process 类
from multiprocessing import Process
from multiprocessing import Pool
import os
import time
import random

def test():
	while True:
		print("---test---")
		time.sleep(1)

# 第二种创建一个新的进程的方式:继承Process类
class NewProcess(Process):
	"""docstring for NewProcess"""
	def __init__(self):
		super(NewProcess, self).__init__()
	def run(self):
		while True:
			print("---test run---")
			# time.sleep(1)

# 第三种创建新的进程的方式: 进程池Pool
def worker(num):
	for i in range(3):
		print("---pid = %d--- num = %d----" % (os.getpid(),num))
		time.sleep(1)

if __name__ == '__main__':
	'''

	# 第一种方式: 用Process类创建一个实例,这个实例就是一个进程对象
	# 主进程创建一个子进程,此子进程执行test函数,不执行其它代
	p = Process(target=test)
	# start()方法: 让进程执行test函数里的代码
	p.start() 
	'''

	# 第二种方式:写一个类继承Process类,重写run方法,用start调用
	'''
	np = NewProcess()
	np.start()

	while True:
		print("---main---")
		time.sleep(1)
	'''

	# 第三种方式: 进程池Pool
	# 3表示进程池中最多有3个进程一起执行
	pool = Pool(3)
	for i in range(10):	
		print("---- %d ----" % i)
		# 向进程池中添加任务
		# 如果添加的任血管数量超过了 进程池中的个数的话,那么不会导致添加不进去
		# 添加到进程中的任务,如果还没被执行的话,那么此时它们会等待进程池中的进程完成一个任务后
		# 会自动的去刚刚那个进程,完成当前的新任务

		# 非堵塞方式
		pool.apply_async(worker,(i,))
		# 堵塞方式
		# pool.apply(worker,(i,))
		
	# 关闭进程池,相当于不能够再次添加新任务了
	pool.close()
	# 主进程创建/添加 任务后,主进程默认不会等待进程池中的任务执行完后才结束,
	# 而是 当主进程的任务做完之后 立马结束,旭果这个地方没join,会导致进程池中的任务不被执行
	pool.join()


# 注:用fork创建的子进程,如果主进程结束了,不会因为子进程没结束还等待,会结束当前程序,但子进程会继续执行完
# 注:用multiprocessing的Peocess类创建的子进程,主进程会等待子进程执行结束后才会结束,与fork不同



