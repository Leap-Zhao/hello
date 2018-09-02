#coding=utf-8

# 队列类Queue(单端队列),先进先出,从队尾进队头出
class Queue(object):
	def __init__(self):
		self.__list = []
	
	# 从队尾进
	def enqueue(self,data):
		self.__list.append(data)
	
	# 从队头出
	def dequeue(self):
		if self.is_empty():
			return None
		else:
			return self.__list.pop(0)

	def is_empty(self):
		return self.__list == []

	def size(self):
		return len(self.__list)

# 双端队列,可以从队尾进队头出,也可以从队头进队尾出
# 相比单端队列,只需要添加两个方法即可:1.从队头进 2.从队尾出
class DQueue(object):
	def __init__(self):
		self.__list = []
	
	# 从队头进
	def enqueue_head(self,data):
		self.__list.insert(0, data)
	
	# 从队尾进
	def enqueue_tail(self,data):
		self.__list.append(data)
	
	# 从队头出
	def dequeue_head(self):
		if self.is_empty():
			return None
		else:
			return self.__list.pop(0)
	# 从队尾出
	def dequeue_tail(self):
		if self.is_empty():
			return None
		else:
			return self.__list.pop()
		
	def is_empty(self):
		return self.__list == []

	def size(self):
		return len(self.__list)

if __name__ == "__main__":
	queue = Queue()
	print(queue.is_empty())
	print(queue.size())
	queue.enqueue(1)
	queue.enqueue(2)
	queue.enqueue(3)
	print(queue.dequeue())
	print(queue.dequeue())
	print(queue.dequeue())
	print(queue.dequeue())