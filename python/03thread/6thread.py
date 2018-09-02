#coding=utf-8
import time
from threading import Thread

# 第一种创建线程的方式:Thread(target=funcName)
def test():
	print("---test function---")
	time.sleep(1)

# 第二种创建线程的方式:继承Thread类
class MyThread(Thread):
	"""docstring for MyThread"""
	def run(self):
		for x in xrange(2):
			time.sleep(1)
			msg = "I'm " + self.name + ' @ ' + str(x)
			print(msg)
def main():
	for x in range(5):
		# 不使用多线程时消耗5s以上
		# test()

		# 使用多线程消耗1-2s
		# 第一种使用线程的方式
		# t = Thread(target=test)
		# t.start()

		# 第二种使用线程的方式
		mt = MyThread()
		mt.start()

if __name__ == '__main__':
	main()

# 注:Thread创建出子线程,特点是主线程会等待子线程执行结束后才会结束
# 注:线程的执行顺序不确定,由操作系统调度算法决定