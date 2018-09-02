# coding=utf-8


'''
#=============================================
# 如何在python中动态创建一维数组和二维数组
#=============================================

# 说明:python和java不太一样,不能在创建列表list时指定其长度,也不能指定其维数,所以要用append或insert方法去动态的创建一维或多维数组

在java中创建一维数组 int a[5] 

# 创建一维数组

>>> mylist = []
>>> for i in range(0,5):
... 	mylist.append(i)
... 
>>> mylist
[0, 1, 2, 3, 4]

# 创建二维数组

>>> mylist = []
>>> for i in range(0,5):
... 	rowlist = []
... 	for j in range(0,i+1):
... 		rowlist.append(j)
... 	mylist.append(rowlist)
... 
>>> mylist
[[0], [0, 1], [0, 1, 2], [0, 1, 2, 3], [0, 1, 2, 3, 4]]

int a[i]

mylist= []
fo
mylist.append()


#=============================================
# 如何在python中创建一个已知长度的列表的一维列表和二维列表
#=============================================

# 在java语言中,创建一个数组时可以指定其长度,如int a[] = new int[5],但python中创建list时却不能指定其长度

# 创建指定个数的一维数组,length表示一组数组的第度
>>> def createlist(length):
... 	mylist = []
... 	for i in range(length):
... 		mylist.append("")
... 	return mylist
... 
>>> mylist = createlist(3)
>>> mylist
['', '', '']




# 创建指定个数的二维数组,x表示第一维的个数,y表示第二维中元素的个数
>>> def createlist(x,y):
... 	mylist = []
... 	for i in range(x):
... 		xlist = []
... 		for j in range(y):
... 			xlist.append("")
... 		mylist.append(xlist)
... 	return mylist
... 
>>> mylist = createlist(2,3)
>>> mylist
[['', '', ''], ['', '', '']]

'''


# 在一个数组里面移除指定value,并且返回新的数组长度。
def removeElement(mylist,ele):
	j = 0 
	for i in range(0,len(mylist)):
		if mylist[i] == ele :
			continue
		mylist[j] = mylist[i]
		j+=1
	# 此句是对数组进行截取,可不写,如果写了,则数组只保留去除元素后的
	mylist = mylist[:j]
	return mylist

mylist = [1,2,3,4,3,2,5,2,1,2,7]

print removeElement(mylist, 2) # [1, 3, 4, 3, 5, 1, 7]
print mylist # [1, 3, 4, 3, 5, 1, 7, 2, 1, 2, 7]


'''
题目描述:
Remove	Duplicates	from	Sorted	Array
	Given	a	sorted	array,	remove	the	duplicates	in	place	such	that	>	each	element appear	only	once	and	return	the	new	length.
Do	not	allocate	extra	space	for	another	array,	you	must	do	this	in	place	with constant	memory.
For	example,
	Given	input	array	A	=	[1,1,2],
	Your	function	should	return	length	=	2,	and	A	is	now	[1,2].


从排序数组中删除重复项
	给定一个有序数组，你需要原地删除其中的重复内容，使每个元素只出现一次,并返回新的长度。
不要另外定义一个数组，您必须通过用 O(1) 额外内存原地修改输入的数组来做到这一点。
示例：
	给定数组: nums = [1,1,2],
	你的函数应该返回新长度 2, 并且原数组nums的前两个元素必须是1和2,且不需要理会新的数组长度后面的元素

解题思路:
这道题目与前一题Remove	Element比较类似。但是在一个排序好的数组里面删除 重复的元素

步骤:
	定义i和j,让j指向数组中下标为0的元素,i指向下标为1的元素且循环整个数组(数据下标),
	在每一次循环中,判断j与i指向的对应数据的值是否相同,
		如果相同,则什么也不做,直接下一次循环(直接让i+1),
		如果两个值不同,则让此值赋给j指向元素的下一个元素(先j+1,再nums[j] = nums[i]),
	最后返回的是j+1的值(因为j为下标,始终比当前指向真正个数少1)
	注意: 上面的i直接从1开始(数组个数至少为2),当数据中元素个数为1时,不循环,直接返回1,成立,但个数为0时不成立,所以加上一个判断,个数为0时直接返回0
	
伪代码:
	如果数组中元素个数为0,返回0
	如果不为0:
	定义j =0
	for i -> 1 : 元素个数
		if 数组[i]与数组[j]相同:
			执行下次循环
		else:
			j+1
			数组[i]对应的值赋给数组[j]
	返回 j+1 
'''



class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numsLen = len(nums)
        if numsLen == 0:
            return 0
        j = 0
        for i in range(1,numsLen):
            if nums[i] == nums[j]:
                continue
            else:
                j += 1
                nums[j] = nums[i]
        return j+1       




# 下面的是n大于等于1时的,末考虑n小于1时的情况,想加的可自行添加
def pascalTriangle(n):
	mylist = []
	# 除第1行外其它行都首和尾都是1,所以第一行单独拿出来
	mylist.append([1])
	# 生成其它行的元素,i从1到n-1,表示第2行到第n行
	for i in range(1,n):
		# 代表第i+1行的列表/数组
		rowlist = []
		rowlistlength = i+1
		# 在第i+1行的行首(j=0时)插入元素1
		rowlist.insert(0,1)
		# 第i+1行一共有i+1个元素,除去首尾还有i-1个元素,下标应从1到i-1
		for j in range(1,rowlistlength-1):
			# 第j个元素的值是上一行(下标为i-1)的相邻两元素之各
			rowlist.append(mylist[i-1][j-1]+mylist[i-1][j])
		# 在第i+1行的行尾(j=i时)插入元素1
		rowlist.insert(rowlistlength-1,1)
		mylist.append(rowlist)
	return mylist

# print pascalTriangle(5)