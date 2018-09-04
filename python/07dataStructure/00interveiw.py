#coding=utf-8

import sys 


'''
给出3个数a1,a2,a3,只能对这3个数执行以下两种操作:
1. 选两个数+1
2. 选一个数+2
则最少需要多少次才能让这三个数相等?

要求:输入参数为三个数,输出为最少需要的次数.

'''
# 第1题
def first_func():
	# 读取输入的3个数,并组成一个有序的列表
    line = sys.stdin.readline().strip()
    intlist = map(int,line.split())
    intlist.sort()


    # 需要的次数count
    count = 0
    # 最大数与另外两个数的差值
    num1 = intlist[2] - intlist[0]
    num2 = intlist[2] - intlist[1]
    # 分别对两数+2,使其成为与最大数只差1或相同的数
    num1Count =  num1//2
    num2Count =  num2//2

    intlist[0] = intlist[0] + 2*num1Count
    intlist[1] = intlist[1] + 2*num2Count

    count = count + num1Count + num2Count

    # 经过上面的步骤后,只剩下四种情况
    # 差值为 1与1,1与0,0与1,0与0
    if (intlist[2]-intlist[1] == 1) and (intlist[2]-intlist[0] == 1):
        count = count + 1
    elif (intlist[2]-intlist[1] == 1) and (intlist[2]-intlist[0] == 0):
        count = count + 2
    elif (intlist[2]-intlist[1] == 0) and (intlist[2]-intlist[0] == 1):
        count = count + 2
    else:
        count = count + 0
    print(count)



# 第2题
def second_func():
	# 读取输入的13个数,并组成一个有序的列表
	line = sys.stdin.readline().strip()
	intlist = map(int,line.split())
	# 读取洗牌次数n
	n = int(sys.stdin.readline().strip())
	# 读取每次洗牌的数
	line = sys.stdin.readline().strip()
	nlist = map(int,line.split())

if __name__ == "__main__":
	first_func()
	

'''
第3题:
描述
int型范围内，将m（m<1000）个数围成一个圈，给定一个数n（n<=m）,求连续的n个数使得和最大。输出最大和及始末位置。
输入 : 多组测试数据，每组数据首行是两个数m，n，表示m个数，求n个连续最大和。
输出 : 输出三个数：sum，b，e，分别表示最大和，开始位置，结束位置。
样例输入
5 3
4 2 3 1 5
4 2
2 3 4 5
样例输出
11 5 2
9 3 4

用滑块做
'''

'''
第4题:
描述
将正整数n表示成一系列正整数之和：n=n1+n2+…+nk， 
其中n1≥n2≥…≥nk≥1，k≥1。 
正整数n的这种表示称为正整数n的划分。求正整数n的不 
同划分个数。 
例如正整数6有如下11种不同的划分： 
6； 
5+1； 
4+2，4+1+1； 
3+3，3+2+1，3+1+1+1； 
2+2+2，2+2+1+1，2+1+1+1+1； 
1+1+1+1+1+1。 

输入 : 第一行是测试数据的数目M（1<=M<=10）。以下每行均包含一个整数n（1<=n<=10）。
输出 : 输出每组测试数据有多少种分法。
样例输入
1
6
样例输出
11

用递归做
'''



