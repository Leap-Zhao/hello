# coding=utf-8

# 定义结点类Node
class Node(object):
	"""结点类Node,有存储数据的数据域data,和指向下一个结点的指针域next"""
	def __init__(self,data):
		self.data = data
		self.next = None

# 定义单链表类SingleLinkList
class SingleLinkList(object):
	"""
	单链表类SingleLinkList,有指向第一个节点的头结点head
	功能:
		1.判断链表是否为空
		2.返回链表的长度
		3.遍历整个链表
		4.往链表头部添加结点
		5.往链表尾部添加结点
		6.往链表指定位置添加结点
		7.删除指定的结点
		8.查找指定结点是否存在
	"""

	def __init__(self,node = None):
		self.__head = node

	# 判断链表是否为空
	def is_empty(self):
		return self.__head == None

	# 返回链表的长度
	def getlength(self):
		# cur游标(current目前位置),遍历节点
		cur = self.__head
		count = 0
		while cur != None:
			count += 1
			cur = cur.next
		return count 

	# 遍历整个单链表
	def travel(self):
		cur = self.__head
		while cur != None:
			print(cur.data),
			cur = cur.next
		print("")

	# 在链表头部添加元素
	# 思路:
	#	 让newNode的next域指向原来的第1个结点(__head),再让头指针__head指向新的结点newNode,这样就在头部插入了新的结点newNode
	#	 之后考虑链表为空时的情况,发现符合设计,不用另加代码
	# 在链表头部添加元素的时间复杂度为o(1)
	def add(self,data):
		node = Node(data)
		node.next = self.__head
		self.__head = node
	

	# 在链表尾部添加元素,时间复杂度为o(n)
	def append(self,data):
		node = Node(data)
		if self.is_empty():
			self.__head = node
		else:
			cur = self.__head
			while cur.next != None:
				cur = cur.next
			cur.next = node


	# 在指定位置添加元素: (这里的位置指的都是下标,从0开始,最大为n-1),无返回值

	# 如果下标小于0或者等于0,则直接在头部插入,如果下标大于n-1,则直接在尾部插入
	# 思考: (为什么没有等于n-1?因为等于n-1时,是在最后一个元素的前一个位置插入了一个元素)
	
	# 如果下标正常,则执行下列步骤:
	# 例如insert(2,400)往下标为2的位置插入400(位置从0开始)	
	# 1.需将cur移动到前一个位置,即下标为1的位置,即(pos-1)的位置
	# 2.newNode.next = cur.next
	# 3.cur.next = newNode
	# 注:为方便将cur起名为pre,代表应该到前一个位置
	def insert_before(self,pos,data):
		node = Node(data)
		cur = self.__head
		if pos <= 0 :
			# 在头部插入新结点
			self.add(data)
		elif pos > (self.getlength()-1):
			# 如果插入位置的下标比(链表长度-1)还大,在尾部插入新结点
			self.append(data)
		else:
			count = 0
			# 循环让cur到达pos-1的位置
			while count<(pos-1):
				count += 1
				cur = cur.next
			# 循环退出之后cur到达pos-1的位置(从0开始)
			node.next = cur.next
			cur.next = node

	# 在指定位置后添加结点
    def insert_after(self,pos,data):
        node = Node(data)
        if pos < 0:
            self.add(data)
        elif pos >= (self.get_length()-1):
            self.append(data)
        else:
            cur = self.__head
            count = 0
            while count<pos:
                count += 1
                cur = cur.next
            node.next = cur.next
            cur.next = node

	# 查找节点是否存在,存在返回真,不存在返回假
	# 思路:
	#	 cur指向第一个节点,将cur指向结点的data域与用户查找的data作比较,
	#	 如果 两者相同,说明存在,直接返回True,否则cur = cur.next,直到遍历整个链也没找到时返回False
	# 难点:
	#	 主要难点在于判断遍历链表时的结束条件,是当cur==None时结束还是cur.next==None时结束
	#   当cur.next==None结束循环时时,当前cur为最后一个有数据的节点,而此时两者data并未比较
	#	所以结束条件是cur==None,而循环条件为cur != None时
	# 最后:
	#	考虑链表为空时的情况	
	def search(self,data):
		cur = self.__head
		while cur != None:
			if cur.data == data:
				return True
			else:
				cur = cur.next
		return False

	# 根据data值找出结点的索引,没找到返回-1
    def search_index(self,data):
        cur = self.__head
        index = 0
        while cur != None:
            if cur.data == data:
                return index
            else:
                index += 1
                cur = cur.next
        return -1
	
	# 删除结点: 若链表中有多个指定的元素,则只删除第1个,无返回值
	# 如果链表为空,则应返回None
	# 思路:
	#	  用pre指向当前结点的前一个结点,pre.next指向当前结点cur,判断当前结点(pre.next)的data域是不是同指定的data相同
	#	 如果相同,则将当前结点的前一个结点指向前结点的后一个结点,即pre.next->pre.next.next,或者pre.next->cur.next
	#	 如果不同,则遍历当前结点,或遍历前一结点pre,因为要遍历一遍所以遍历结束条件同search方法中相同,pre.next==None即cur==None时结束循环
	# 难点:
	#	 处理好当前结点cur与前一结点pre的关系,下面的是只用pre来写的,只用pre时,无法判断第1个结点的data域,所以要单独拿出来写
	#	当第1个结点满足条件时,让头指针__head直接指向下一个结点并返回,而不继续执行
	#	 当移除了一个指定元素时,就直接return,而不是继续执行,
	# 说明:
	# 	当链表只有1个元素并移除后返回的链表为空链表None,当链表为空时再移除就报异常,这样的安排是和python的list列表的remove方法保持一致
	def remove_by_data(self,data):
		if self.is_empty():
            print("simple link list is empty")
        else:
			pre = self.__head
			if pre.data == data:
				self.__head = pre.next
				return
			while pre.next != None:
				if pre.next.data == data:
					pre.next = pre.next.next
					return
				else:
					pre = pre.next

	# 根据位置删除指定结点
    def remove_by_index(self,pos):
        if self.is_empty():
            print("simple link list is empty")
        else:
            if pos <= 0:
                self.__head = self.__head.next
            elif pos >= (self.get_length()-1):
                index = 1
                pre = self.__head
                while index < self.get_length()-1:
                    index += 1
                    pre = pre.next
                pre.next = None
            else:
                index = 1
                pre = self.__head
                while index < pos:
                    index += 1
                    pre = pre.next
                pre.next = pre.next.next

if __name__ == "__main__":
	sll = SingleLinkList()
	print(sll.is_empty())
	print(sll.getlength())

	sll.append(1)
	print(sll.is_empty())
	print(sll.getlength())

	sll.append(5)
	sll.add(2)
	sll.add(1)

	sll.insert(2,3)
	sll.insert(3,2)
	sll.travel() # 1 2 3 2 1 5
	sll.remove(2) 
	sll.travel() # 1 3 2 1 5
	sll.remove(1) 
	sll.travel() # 3 2 1 5
	sll.remove(5)
	sll.travel() # 3 2 1
	sll.remove(3)
	sll.remove(1)
	sll.travel() # 2
	sll.remove(2) 
	sll.travel() # ''
	
	





