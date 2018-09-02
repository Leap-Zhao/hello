#coding=utf-8

from multiprocessing import Queue
from multiprocessing import Pool
from multiprocessing import Manager
import os

'''
# 进程间通信 Queue() 队列 : 此种只适用于Process
# 方法: qsize(),put(),get(),empty(),full()

q = Queue(3) # 创建一个3个容量的队列
print(q)

# 进程池间的通信 Manager().Queue() 对象
# 方法与Queue中的一致
mq = Manager().Queue()
print(mq)
'''

# 例子: 多进程拷贝文件

# 第1步: 创建一个文件夹 os.mkdir("fileName") os.rmdir("fileName")
def copyFile(fileName,oldFolderName,newFolderName,queue):
	# 完成拷贝文件的功能
	fr = open(oldFolderName + "\\" + fileName,"rb")
	fw = open(newFolderName + "\\" + fileName,"wb")
	content = fr.read()
	fw.write(content)
	fr.close()
	fw.close()

	# 将文件名放入消息队列中去
	queue.put(fileName)

def getFolderName():
	folderName = raw_input("输入你要拷贝的文件夹名:")
	return folderName

def createNewFoler(oldFolerName):
	newFolerName = oldFolerName + "-copy"
	try :
		print("111-start")
		os.mkdir(newFolerName)
		print("111-end")
	finally:
		return newFolerName

def testFile(path):
	f = open(path)
	content = f.read()
	print(content)

def main():
	# os.rmdir("test-copy")
	# 获取要拷贝的文件夹名
	oldFolderName = getFolderName()
	print(oldFolderName)
	# 创建一个新的文件夹,返回新文件夹对象
	newFolderName = createNewFoler(oldFolderName)
	print(newFolderName)
	# 创建5个进程
	pool = Pool(5)
	queue = Manager().Queue()
	# 获取旧文件夹里的所有文件,返回列表
	fileList = os.listdir(oldFolderName)
	for fileName in fileList:
		# 每个进程执行一个拷贝任务
		pool.apply_async(copyFile,(fileName,oldFolderName,newFolderName,queue))

	# 显示copy进度
	num = 0 
	allNum = len(fileList)
	while num<allNum:
		queue.get()
		num += 1 
		copyRate = num/allNum
		print("copy的进度是 : %.2f %%" % (copyRate*100)),

	print("\ncopy finished")


if __name__ == '__main__':
	main()
	# path = "test\index.html"
	# testFile(path)
