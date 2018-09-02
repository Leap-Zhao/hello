# coding=utf-8

# 定义一个栈类Stack,先进后出
class Stack(object):
	"""
		接下来用顺序表来实现栈的各种操作,在python中顺序表用list列表来表示
		1. 添加一个元素到栈顶
		2. 弹出栈顶的元素
		3. 返回栈顶的元素
		4. 判断栈是否为空
		5. 返回栈中元素的个数
	"""

	def __init__(self):
		self.__list = []

	def push(self,data):
		self.__list.append(data)

	# 弹出栈项元素(此时栈已改变)
	def pop(self):
		if self.is_empty():
			return None
		else:
			return self.__list.pop()

	# 返回栈顶元素(此时栈未改变)
	def peek(self):
		if self.__list == []:
			return None
		else:
			return self.__list[-1]

	def is_empty(self):
		return self.__list == []

	def size(self):
		return len(self.__list)

if __name__ == "__main__":
	s = Stack()
	print(s.is_empty())
	print(s.size())
	print(s.peek())
	print(s.pop())

	s.push(1)
	s.push(2)
	s.push(3)
	print(s.peek())
	print(s.pop())
	print(s.peek())
	print(s.pop())