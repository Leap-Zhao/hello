#coding=utf-8

import sys 



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

