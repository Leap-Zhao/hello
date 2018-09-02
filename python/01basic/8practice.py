#coding=utf-8

import timeit

def main():
    '''
    弱类型语言
    数字类型 Number :int long float complex
    布尔类型 Boolean : True False
    其它类型 String ,List,Tuple,Dictionary
    type(a)
    type(a)
    '''

    # import keyword
    # print(keyword.kwlist)

    # import keyword
    # print(keyword.kwlist)

    # import keyword
    # print(keyword.kwlist)

    # 运算符 
    # 算术运算符 ** a**b // a//b
    # 赋值运算符 
    # 比较运算符 <,>,==,>=,<=,!=,<>
    # 逻辑运算符 and,or,not
    # 位运算符 &,|,^,~,<<,>>

    import keyword 
    print(keyword.kwlist)

    import time
    timeFrom1970 = time.time()
    print(time.localtime(timeFrom1970))

    # num1 = input("input a number")
    # print(type(num1))

    # num2 = raw_input("input a number")
    # print(type(num2))

    myStr = "abcdefg"
    # 字符串遍历
    for i in range(0,len(myStr)):
        print(myStr[i])

    print(myStr[2:-1])

    # 列表(有序,可修改,可重复)
    # 元组(有序,不可修改,可重复)

    myList = [1,'2',3.12]

    # 遍历列表
    for i in range(0,len(myList)):
        print(myList[i]),
    print("")

    i=0
    while i<len(myList):
        print(myList[i]),
        i+=1
    print("")

    for i in myList:
        print(i),
    print("")

    # 增加元素 append
    # 删除元素 del,pop(),remove()
    # 修改元素 myList[0] = ""
    # 查找元素 in , not in
    # 列表切片

    myList.append("newElement")
    del myList

    # 元组(有序,不可修改,可重复)
    myTuple = ('zhao',77,99.9)
    # 删除整个元素del myTuple
    print(myTuple)
    # 元组内置函数 : cmp() len() max( min() tuple()
    # 元组的遍历
    for i in range(0,len(myTuple)):
        print(myTuple[i]),
    print("")

    for ele in myTuple:
        print(ele),
    print("")

    # 字典 Dictionary
    # 字典遍历 : keys,values,items(),has_keys("")
    # 增加元素 myDict['ass']
    # 删除元素 del clear
    # 修改元素 myDict['add'] = ""
    # 查找元素has_keys() 
    myDict = {1:"zhao",2:18,3:24}

    myDict['add'] = "beijing"
    for keyName in myDict.keys():
        print(keyName,type(keyName))

    # 函数

    # 不定长参数
    # def test(*args):
    #   for ele in args:
    #       print(ele)

    # def test(num1,*args):
    #   pass

    # def test2(num=1,age):
    #   print(age)

    # 匿名函数lambda
    sumByLam  = lambda a,b:a+b
    (lambda a,b,c:a+b+c)(1,2,3)

    # win下换行是/r/n ,linux下是/n 

    # import os
    # os.rename("a.txt","b.txt")
    # os.remove("")
    # os.mkdir("dir")
    # os.rmdir("")
    # os.getcwd()
    # os.chdir("")
    # os.listdir("./")


from collections import deque

def search(lines,pattern,history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


def bubble_sort(alist):
    '''
    n = len(alist)
    for i in range(0,n-1):
        for j in range(0,n-1-i):
            if alist[j] > alist[j+1]:
                alist[j],alist[j+1] = alist[j+1],alist[j]
    '''

    n = len(alist)
    for i in range(n-1,0,-1):
        for j in range(0,i):
            if alist[j] > alist[j+1]:
                alist[j],alist[j+1] = alist[j+1],alist[j]

def select_sort(alist):
    n = len(alist)
    for i in range(0,n-1):
        min_index = i
        for j in range(min_index+1,n):
            if alist[min_index] > alist[j]:
                min_index = j
        alist[i],alist[min_index] = alist[min_index],alist[i]

class Dog(object):
    # 类属性
    color = "white"
    # 私有属性
    __name = "xiaohuang"

    # 构造方法 :对象创建时做的事情
    def __init__(self,age):
        self.__age = age
    # 析构方法: 对象销毁时做的事情
    def __del__(self):
        pass
    # 实例方法/公共方法
    def setName(self,name):
        self.__name = name
    def getName(self):
        return self.__name
    # 私有方法
    def __call(self):
        pass
    # 类方法
    @classmethod
    def setColor(cls,color):
        cls.color = color
    # 静态方法
    @staticmethod
    def testStaticMethod():
        pass

class Test(object):
    global_parm = "hello"

    def __init__(self):
        self.name = "fei"
    
    def normalmethod(self):
        print(self.name)
    
    @classmethod
    def classmethod(cls,parm):
        cls.global_parm = parm
        cls.name = "yue"

    # def setGlobalParm(self,parm):
    #   self.__global_parm = parm

    # def getGlobalParm(self):
    #   return self.__global_parm
    
    @staticmethod
    def staticmethod():
        Test.global_parm = "fdsfs"

    def __del__(self):
        print(Test.global_parm)


# 冒泡
def bubble_sort(alist):
    n = len(alist)
    # i = n-1,n-2 ... 1
    for i in range(n-1,0,-1):
        count = 0
        for j in range(0,i):
            if alist[j] > alist[j+1]:
                alist[j],alist[j+1] = alist[j+1],alist[j]
                count += 1
            if count == 0:
                return

# 选择
def select_sort(alist):
    n = len(alist)
    # i= 0,1,...n-1
    for i in range(0,n):
        min_index = i 
        for j in range(i,n):
            if alist[min_index] > alist[j]:
                min_index = j
        alist[i],alist[min_index] = alist[min_index],alist[i]

# 插入
def insert_sort(alist):
    n = len(alist)
    # i = 1,2,...n-1
    for i in range(1,n):
        for j in range(i,0,-1):
            if alist[j-1] > alist[j]:
                alist[j-1],alist[j] = alist[j],alist[j-1]
            else:
                break

# 希尔
def shell_sort(alist):
    n = len(alist)
    gap = n//2
    while gap >= 1:
        # i = gap,gap+1,...n-1
        for i in range(gap,n):
            for j in range(i,0,-gap):
                if alist[j-gap] > alist[j]:
                    alist[j-gap],alist[j] = alist[j],alist[j-gap]
                else:
                    break
        gap = gap//2


# 快速
# def quick_sort(alist,first,last):
#     n = len(alist)

#     if first >= last:
#         return

#     low = first
#     high = last

#     middle_value = alist[low]
    
#     while low < high:
#         while low < high and middle_value <= alist[high]:
#             high -= 1
#         alist[low],alist[high] = alist[high],alist[low]

#         while low < high and alist[low] < middle_value:
#             low += 1
#         alist[low],alist[high] = alist[high],alist[low]
#     # alist[low] = middle_value

#     quick_sort(alist, first, low-1)
#     quick_sort(alist, low+1, last)


# 快排
# 最优O(nlogn),最坏O(n^2),不稳定
def quick_sort(alist,first,last):
    n = len(alist)
    if first >= last:
        return 
    low = first
    high = last
    middle_value = alist[low]
    while low < high:
        while low < high and middle_value <= alist[high]:
            high -= 1
        alist[low] = alist[high]
        # alist[low],alist[high] = alist[high],alist[low]
        while low < high and middle_value > alist[low]:
            low += 1
        alist[high] = alist[low]
        # alist[high],alist[low] = alist[low],alist[high]
    alist[low] = middle_value

    quick_sort(alist, first, low-1)
    quick_sort(alist, low+1, last)


def quick_sort2(alist,first,last):
    n = len(alist)
    if first >= last:
        return 
    low = first
    high = last
    middle_value = alist[low] 
    while low < high:
        while low < high and middle_value <= alist[high]:
            high -= 1
        alist[low] = alist[high]
        while low < high and alist[low] < middle_value:
            low += 1
        alist[high] = alist[low]
    alist[low] = middle_value

    quick_sort2(alist, first, low-1)
    quick_sort2(alist, low+1, last)


# 归并
def merge_sort(alist):
    n = len(alist)
    # 当只有1个时返回当前列表
    if n <= 1:
        return alist
    
    # 先分
    mid = n//2
    left_list = merge_sort(alist[:mid])
    right_list = merge_sort(alist[mid:])
    
    # 再合
    left_pointer,right_pointer = 0,0
    result = []
    while left_pointer < len(left_list) and right_pointer < len(right_list):
        if left_list[left_pointer] <= right_list[right_pointer]:
            result.append(left_list[left_pointer])
            left_pointer += 1
        else:
            result.append(right_list[right_pointer])
            right_pointer += 1
    # 如果有一方完毕,则另一方全部添加进去
    result += left_list[left_pointer:]
    result += right_list[right_pointer:]

    return result

# 归并
# 最优O(nlogn),最差O(n^2),是稳定的,空间复杂度O(n)
def merge_sort2(alist):
    # 先分
    n = len(alist)
    # 当分到只有1个时,返回本身这个列表
    if n <= 1:
        return alist
    middle = n//2
    left_list = merge_sort(alist[:middle])
    right_list = merge_sort(alist[middle:])

    # 再合
    left_pointer,right_pointer = 0,0
    # 保存合并的结果
    result = []
    while left_pointer < len(left_list) and right_pointer < len(right_list):
        if left_list[left_pointer] <= right_list[right_pointer]:
            result.append(left_list[left_pointer])
            left_pointer += 1
        else:
            result.append(right_list[right_pointer])
            right_pointer += 1
    # 当有一边全部走完时
    result += left_list[left_pointer:]
    result += right_list[right_pointer:]
    return result


# 算法5大特性: 输入,输出,有穷性,可行性,确定性
# 时间复杂度: 1 < longn < n < nlogn < n^2 < n^3 < 2^n < n! < n^n 
# 入门题: a + b + c = 1000,a^2 + b^2 = c^2 ,求所有的a,b,c

def basic_algorithm():
    for a in range(0,1001):
        for b in range(0,1001-a):
            c = 1000-a-b
            if a**2 + b**2 == c**2:
                print("a=%d,b=%d,c=%d" % (a,b,c))



# 用来测试的timeit模块,timeit.Timer类

# 线性表分为连续表与链表
# 连续表,数组,py中为列表list
# 单链表


# 单链表实现
# 结点类
class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None

# 单链表类
class SingleLinkList(object):
    # 初使化,头结点
    def __init__(self,node=None):
        self.__head = node

    # 判断链表是否为空
    def is_empty(self):
        return self.__head == None

    # 得到链表的长度
    def get_length(self):
        cur = self.__head
        length = 0
        while cur != None:
            length += 1
            cur = cur.next
        return length

    # 遍历列表
    def travel(self):
        cur = self.__head
        while cur != None:
            print(cur.data),
            cur = cur.next
        print("")

    # 头部添加结点
    def add(self,data):
        node = Node(data)
        node.next = self.__head
        self.__head = node

    # 尾部添加结点
    def append(self,data):
        node = Node(data)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node


    # 任意位置添加结点
    def insert(self,pos,data):
        if pos <= 0 :
            self.add(data)
        elif pos > (self.get_length()-1):
            self.append(data)
        else:
            node = Node(data)
            cur = self.__head
            index = 0
            while index < (pos-1):
                cur = cur.next
                index += 1
            node.next = cur.next 
            cur.next = node


    # 按结点数据删除结点
    def remove(self,data):
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

    # 删除头部结点
    # 删除尾部结点
    # 删除任意位置结点

    # 按结点数据修改结点
    # 修改头部结点
    # 修改尾部结点
    # 修改任意位置结点

    # 查找某结点是否存在,返回True或False
    def search(self,data):
        cur = self.__head
        while cur != None:
            if cur.data == data:
                return True
            else:
                cur = cur.next
        return False
    
    # 查找某结点是否存在,返回结点所在位置


# 双链表
# 结点类
class Node2(object):
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

# 双端链表
class DoubleLinkList(object):
    def __init__(self,node=None):
        self.__head = node

    # 判空
    def is_empty(self):
        return self.__head == None
    # 求长
    def get_length(self):
        length = 0
        cur = self.__head
        while cur!=None:
            length += 1
            cur = cur.next
        return length
    # 遍历
    def travel(self):
        cur = self.__head
        while cur!=None:
            print(cur.data),
            cur = cur.next
        print("")

    # 头插法
    def add(self,data):
        node = Node2(data)
        self.__head.prev = node
        node.next = self.__head
        self.__head = node

    # 尾插法
    def append(self,data):
        node = Node2(data)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    # 任意位置插入
    def insert(self,pos,data):
        if pos < 0:
            self.add(data)
        elif pos > self.get_length()-1:
            self.append(data)
        else:
            node = Node2(data)
            cur = self.__head
            index = 0
            while index < pos:
                cur = cur.next
                index += 1
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node

    # 删除结点(这是双端队列中与单端最不同,也是最难的地方)
    def remove(self,data):
        cur = self.__head
        while cur != None:
            # 找到该结点时
            if cur.data == data:
                # 1.先判断是不是头结点(头结点的prev为None)
                if cur == self.__head:
                    # 是头结点
                    self.__head = cur.next
                    # 是头结点后,再确定同时是不是尾结点(尾结点的next为None)
                    if cur.next != None:
                        # 是头结点且不是尾结点时
                        cur.next.prev = None
                else:
                    #不是头结点
                    cur.prev.next = cur.next
                    # 不是头结点,再判断是不是尾结点:
                    if cur.next != None:
                        # 不是头结点,且不是尾结点时
                        cur.next.prev = cur.prev
                break
            else:
                cur = cur.next 

    # 查找元素
    def search(self,data):
        cur = self.__head
        while cur!=None:
            if cur.data == data:
                return True
            else:
                cur = cur.next
        return False


# 栈Stack
# 往栈顶添加一个元素
# 弹出栈顶的元素
# 返回栈顶元素
# 

class Stack(object):
    def __init__(self):
        self.__list = []

    def is_empty(self):
        return self.__list == []

    def travel(self):
        for i in self.__list:
            print(i),
        print("")

    def get_length(self):
        return len(self.__list)


    def push(self,data):
        self.__list.append(data)

    def pop(self):
        if self.is_empty():
            return None
        else:
            self.__list.pop()

    def peek(self):
        if self.is_empty():
            return None
        else:
            self.__list[-1]


if __name__ == '__main__':
    alist = [8,7,6,3,2,5]
    print(alist)

    # bubble_sort(alist)
    # select_sort(alist)
    # insert_sort(alist)
    # shell_sort(alist)
    # quick_sort2(alist, 0, len(alist)-1)
    newlist = merge_sort2(alist)
    print(newlist)
    print(alist)

    # basic_algorithm()
    # t1 = timeit.Timer("basic_algorithm()","from __main__ import basic_algorithm")
    # print("spend time: %f s" % t1.timeit())

    # sll = DoubleLinkList()
    # print(sll.is_empty()) # True
    # print(sll.get_length()) # 0

    # sll.append(1)
    # print(sll.is_empty()) # False
    # print(sll.get_length()) # 1 

    # sll.append(5)
    # sll.add(2)
    # sll.add(1)

    # sll.insert(2,3)
    # sll.insert(3,2)
    # sll.travel() # 1 2 3 2 1 5
    # sll.remove(2) 
    # sll.travel() # 1 3 2 1 5
    # sll.remove(1) 
    # sll.travel() # 3 2 1 5
    # sll.remove(5)
    # sll.travel() # 3 2 1
    # sll.remove(3)
    # sll.remove(1)
    # sll.travel() # 2
    # sll.remove(2) 
    # sll.travel() # ''

    s = Stack()




    