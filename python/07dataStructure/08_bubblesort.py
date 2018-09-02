#coding=utf-8

# 提前声明,下文中所指的都是下标,比如,位置2的元素即下标为2为元素,位置从0开始

'''
=====================
=======冒泡排序========
=====================
'''


# 冒泡排序基本思路
# n为排序元素的个数
# 1.定义一个变量i控制循环的趟数(i),n个数遍历n-1趟,python中range(0,n-1)
# 2.在每一趟的循环中,要比较相邻两个数的大小,定义当前比较的元素的索引j
#     第1趟j的下标从0->n-2(此时i=0), python中range(0,n-1)
#     第2趟j的下标从0->n-3(此时i=1), python中range(0,n-2)
#     所以,第i趟j的下标从0->n-2-i,   python中range(0,n-1-i)
# 3.每一趟所做的事:
#     比较相邻两个数的大小ele[j]与ele[j+1]
#     要将大的往后移,所以如果ele[j]>ele[j+1],则交换位置

# 4.注意事项:
#    因为涉及交换两个数的操作,所以选择顺序表而不是链表的方式来代表元素集合,在python中顺序表用list列表
#    第1趟下标从0->n-2是因为在比较两个元素大小时要执行+1操作,所以n-2加1时下标为n-1,即序列的最后一个元素
#    在python中列表是可变类型,在函数中修改了之后不用返回列表,原列表就是排序后的

# 5.其它说明:
#    冒泡排序主要是处理好"趟数"与"每趟中间的索引值"的关系
#    n个数需要n-1趟,如果趟数i为range(0,n-1),则j对应的就是range(0,n-i-1),和上面一样
#    如果趟数i为range(1,n),则j对应的就是range(0,n-i),这样是不是更好理解呢?
#

# 6.冒泡排序时间复杂度为o(n^2)
def bubble_sort_basic_one(alist):
    n = len(alist)
    for i in range(0,n-1):
        for j in range(0,n-1-i):
            if alist[j] > alist[j+1]:
                alist[j],alist[j+1] = alist[j+1],alist[j]
                
# 冒泡排序新思路
# 有没有可能每一趟的下标j都是range(0,i)呢?这样岂不是很容易记,只需要记i怎么循环就行了.
# 要想实现上面的,则下标j的最大值依次是n-2,n-3,n-4,...,1,0,所以i的值依次为n-1,n-2,n-3,...,2,1,所以i为range(n-1,0,-1)
def bubble_sort_basic_two(alist):
    n = len(alist)
    for i in range(n-1,0,-1):
        for j in range(0,i):
            if alist[j] > alist[j+1]:
                alist[j],alist[j+1] = alist[j+1],alist[j]

# 冒泡排序优化
# 1.在每一趟循环中增加一个变量值count来记录每一趟两个元素交换的次数,每交换一次count值+1,新的一趟时count归0
#     如果在某一趟中排序后,发现count的值仍为0,说明这一趟没有交换元素,说明此时该序列已经有序,直接退出函数
def bubble_sort_advance(alist):
    n = len(alist)
    for i in range(0,n-1):
        count = 0 
        for j in range(0,n-1-i):
            if alist[j] > alist[j+1]:
                alist[j],alist[j+1] = alist[j+1],alist[j]
                count += 1
        if count == 0:
            return   
        
        
'''
=====================
=======选择排序========
=====================
'''

# 选择排序基本思路 
# n为排序元素的个数
# 每一趟从序列中选出最小的值,将最小值的下标/索引min_index记录下来,与当前趟的位置进行交换
# 比如第1趟将最小值下标alist[min_index]与第1个数alist[0]作交换,第2趟将与第2个数alist[1]作交换
# 每一趟所做的事:
#     将这一趟的最小值先记为当前趟数,第1趟(i=0)为下标1开始
#     依次向后进行比较,遇到比它小的将min_index记为当前位置
#     将索引min_index与索引i的值进行交换

# 先考虑第1趟的情况:
# min_index = 0
# for j in range(min_index+1,n):
#     if alist[min_index] > alist[j]:
#         min_index = j
# alist[0],alist[min_index] = alist[min_index],alist[0]

# 第2趟时,min_index从下标1开始,下标j从min_index+1开始到n-1,最后将下标1位置与min_index位置作交换
# 第3趟时,min_index从下标2开始,下标j从min_index+1开始到n-1,最后将下标2位置与min_index位置作交换
# 所以添加趟数的外部循环索引i,n个数一共需要n-1趟,i从0->n-2,在python中为range(0,n-1),之后再考虑趟数i与min_index的联系
def select_sort(alist):
    n = len(alist)
    for i in range(0,n-1):
        min_index = i
        for j in range(min_index+1,n):
            if alist[min_index] > alist[j]:
                min_index = j
        alist[i],alist[min_index] = alist[min_index],alist[i]
        
'''
=====================
=======插入排序========
=====================
'''

# 基本思路:
# 将序列分为两类,一类有序的,一类无序的,从无序中的第1个插入到有序的序列中去
# 第2个数与与第1个数比较,如果小的话交换位置,相当于让第2个数插入第1个的前面,达到前两个有序
# 将第3个数插入到前2个数中,达到前3个有序

# 每一趟做的事:
# 	 将当前趟要排序的元素与之前已排序的元素一一作比较,看是否比前一个元素小
#	 如果小于前一个元素,则交换两者的位置
#	 之后再将当前的元素索引-1,继续循环

# 比如前2个数有序时,第3个数(下标为2)的情况:
'''
j = 2
while j > 0 :
	if alist[j-1] > alist[j]:
		alist[j-1],alist[j] = alist[j],alist[j-1]
	j -= 1
'''
# 或者
'''
j = 2
for j in range(2,0,-1):
	if alist[j-1] > alist[j]:
		alist[j-1],alist[j] = alist[j],alist[j-1]
'''

# 之后加入趟数,第1次要从位置1(下标1)开始比较,之后依次是位置2,位置3,位置n-1,所以是range(1,n)

# 此时的最优时间复杂度和最坏时间复杂度都是o(n^2)
# 因为最优时就算一次交换也不执行,两个循环也要执行完,所以最优也是o(n^2)
def insert_sort_basic(alist):
	n = len(alist)
	for i in range(1,n):
		for j in range(i,0,-1):
			if alist[j-1] > alist[j]:
				alist[j-1],alist[j] = alist[j],alist[j-1]
	'''
	for i in range(1,n):
		j = i
		while j > 0:
			if alist[j-1] > alist[j]:
				alist[j-1],alist[j] = alist[j],alist[j-1]
			j -= 1
	'''

# 插入排序优化
# 因为排好序的部分已经有序,所以从未排序部分的元素与排好序的部分作比较时
# 如果遇到比其大的数,则将它俩交换并将索引-1,如果遇到比其小的数,则可以不用再与之前的数作比较了
# 例如,位置5的数比位置4的数小,则交换,此时,位置4与位置3的数比较,如果位置4的数大于位置3的数,则不用再与位置2,1,0比较,因为之前都已有序

# 优化后的最优时间复杂度为o(n),最坏时间复杂度为o(n^2)
# 最优时第2层循环都是执行一次就退出循环,所以相当于只执行了第一层循环,复杂度为o(n)
def insert_sort_advance(alist):
	n = len(alist)
	for i in range(1,n):
		for j in range(i,0,-1):
			if alist[j-1] > alist[j]:
				alist[j-1],alist[j] = alist[j],alist[j-1]
			else:
				break
	'''
	for i in range(1,n):
		j = i
		while j > 0:
			if alist[j-1] > alist[j]:
				alist[j-1],alist[j] = alist[j],alist[j-1]
				j -= 1
			else:
				break
	'''



'''
=====================
=======希尔排序========
=====================
'''

# 基本思路:
# 有一个gap变量,即缝隙的意思,将n个数的序列分成几组
# 比如,有9个数字,gap=n/2为4,即隔4个数字的分为一组,之后这一组以插入排序的方式进行
# 位置0,4,8为一组,位置1,5为一组,位置2,6为一组,位置3,7为一组,将每一组都有序,再组合成这一个序列
# 之后将gap的值再缩小一半,即4/2 为2,让位置0,2,4,6,8为一组,位置1,3,5,7为一组,让每一组再以插入排序的方式排序
# 最后是让gap为1,再进行插入排序

'''
# 以第一趟为例子
gap = 4
# 这里考虑的是每一小组的起始位置i,分别是4,5,6,7
for i in range(gap,n):
	# 这里考虑的是每一个小组,比如0,4,8
	for j in range(i,0,-gap):
		if alist[j] < alist[j-gap]:
			alist[j],alist[j-gap] = alist[j-gap],alist[j]
		else:
			break
# 再将gap缩小一半的操作
gap = gap/2
'''

def shell_sort(alist):
	n = len(alist)
	# 这里用取整除,使得不管是py2还是py3都是对的
	gap = n//2
	# 最外层的gap
	while gap >= 1:
		for i in range(gap,n):
			for j in range(i,0,-gap):
				if alist[j-gap] > alist[j]:
					alist[j-gap],alist[j] = alist[j],alist[j-gap] 
				else:
					break
		gap = gap//2 





'''
=====================
=======快速排序========
=====================
'''

# 基本思路:
#	 以位置0处的素为基准,用两个游标low和high与这个基准元素的大小关系,从而找出基准元素在该序列的正确位置
#	 找出基准元素的位置后,将序列分为两部分,一部分是比基准元素小的,一部分是比基准元素大的.
#	 将分成的两部分再递归的执行上面两个步骤,从而达到排序所有元素的目的

'''
# 第1趟时:
middle_value = alist[0]
low = 0
high = n-1
# 当low==high或者low>high时,说明都已经分好了两部分
while low < high:
	# 一定要将high的比较写在low的比较前,因为第1次执行时此时alist[low]是无用的,可以赋值给它
	while low < high and alist[high] >= middle_value:
		high -= 1
	alist[low] = alish[high]

	while low < high and alist[low] < middle_value:
		low += 1
	alist[high] = alist[low]

alist[low] = middle_value
# 第1趟过后,分成了[0,low-1]与[low+1,n-1] 两部分

# 之后,再加上对这两部分的递归调用,分别完成第2,3,...n-1趟
# 最后,加上递归的结束条件,当first >= last 时,递归就结束了,
# 注意,递归结束条件不能只用first = last时,要加上>号,
# 你知道原因么?因为是每次递归时前一部分的last是本次过程的low-1,后一部分的first是本次过程的low+1,
# 所以有可能只剩下一个元素的递归时,low和high相同,之后low-1之后就比high小了 
'''

# 其它:
# 每一次将数字分为两部分,需要执行n次low,high的比较操作,但一共需要多少次这样的分开操作,却是可以由每次分开的位置决定的
# 最优时间复杂度:O(nlogn),如果每一次都刚好是中间位置,则logn次即可全部分完,所以最优是O(nlogn)
# 最坏时间复杂度:O(n^2),如果每一次都刚好是最边上的位置,则需要n次才可全部分守,所以最坏是O(n^2)
# 稳定性: 不稳定的,因为low和high需要将元素不断移动


def quick_sort(alist,first,last):
	# 结束递归的条件
	if first >= last:
		return

	low = first
	high = last 
	middle_value = alist[low]
	while low < high:
		while low < high and alist[high] >= middle_value:
			high -= 1
		alist[low] = alist[high]
		while low < high and alist[low] < middle_value:
			low += 1
		alist[high] = alist[low]
	alist[low] = middle_value

	# 递归调用
	quick_sort(alist,first,low-1)
	quick_sort(alist,low+1,last)



'''
=========================
=======归并排序==========
=========================
'''

# 用递归的思维来写
# 时间复杂度:最优和最坏都是O(nlogn),但需要用到额外的空间O(n)
# 算法是稳定的
def merge_sort(alist):
	n = len(alist)
	if n <= 1:
		return alist

	# mid 代表的是每次分完之后的序列个数,第一次为n,之后为n//2,n//4,...1
	mid = n//2

	# 将当前alist分为左半部分和右半部分
	left_list = merge_sort(alist[:mid])
	right_list = merge_sort(alist[mid:])

	# 分好之后将左右两部分合并,比如,将[1,3]与[2,4]合并
	# 定义两个从每组开始遍历的左右指针
	left_pointer,right_pointer = 0,0
	# 定义保存结果的值
	result = []
	while left_pointer < len(left_list) and right_pointer < len(right_list):
		if left_list[left_pointer] <= right_list[right_pointer]:
			result.append(left_list[left_pointer])
			left_pointer += 1
		else:
			result.append(right_list[right_pointer])
			right_pointer += 1
	# 当左边都遍历完时,将右边全部装入result
	# 当右边都遍历完时,将左边全部装入result
	result += left_list[left_pointer:]
	result += right_list[right_pointer:]
	return result

'''
=====================
=======堆排序========
=====================
'''
# 堆排序
def element_exchange(alist,low,high):
    # temp = alist[low]
    # i = low
    # j = 2*i
    # while j <= high:
    #     if j < high and alist[j] < alist[j+1]:
    #         j = j+1
    #     if temp < alist[j]:
    #         alist[i] = alist[j]
    #         i = j
    #         j = 2*i
    #     else:
    #         break

    # low 代表将要放置的元素下标
    # j = 2*low 代表将要放置元素的左子节点的下标
    temp = alist[low]
    j = 2*low 
    while j <= high:
        # j和j+1代表 左子树和右子树
        if j < high and alist[j] < alist[j+1]:
            j = j +1
        if temp >= alist[j]:
            break
        # 将alist[j]调整到双亲节点的位置上
        alist[low] = alist[j]
        low = j
        j = 2*j 
    alist[low] = temp

def top_heap_sort(alist):
    n = len(alist)-1
    # 指定第一个进行调整的元素的下标
    # 它即该无序序列完全二叉树的第一个非叶子节点
    # 它之前的元素均要进行调整
    # 9个元素时它为4
    first_exchange_element = n//2

    # 建立初始堆
    # i= 4,3,2,1
    for i in range(first_exchange_element,0,-1):
        # i=4时,需从4调到9
        # i=3时,需从3调到9
        element_exchange(alist, i, n)

    # 将根节点放到最终位置，剩余无序序列继续堆排序
    # 最后位置依次是9,8,...2,最的一个时不用考虑
    # length-1 次循环完成堆排序  
    for j in range(n,1,-1):
        # 将堆顶元素和当前未经排序子序列的最后一个记录交换
        alist[j],alist[1] = alist[1],alist[j]
        # 剩余元素继续调整为最大堆
        # 最后位置为9时,需将1-8调整
        # 最后位置为8时,需将1-7调整
        # 所以1->j-1
        element_exchange(alist, 1, j-1)



'''
=====================
=======排序总结========
=====================
'''
# 冒泡,选择,插入排序: 两个for循环
# 冒泡:最大的往后移
# 选择:需要1个变量min_index记录每趟最小数的下标
# 插入: 
# 希尔:需要1个变量gap,
# 快排:需要3个变量,low,high,mid_value,low是每趟递归序列的第一个值,high是每趟递归序列的最后一个值,mid_value是每趟需要更改的那个数



if __name__ == "__main__":
    # alist = [7,6,5,4,3,2,1]
    # print(alist)
    # quick_sort(alist,0,len(alist)-1)
    # print(alist)

    heap_alist = [0,7,6,5,4,3,2,1]
    print(heap_alist)
    top_heap_sort(heap_alist)
    print(heap_alist)
