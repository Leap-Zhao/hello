# coding=utf-8
import time
import timeit


'''
算法的五大特性
输入: 算法具有0个或多个输入
输出: 算法至少有1个或多个输出
有穷性: 算法在有限的步骤之后会自动结束而不会无限循环，并且每一个步骤可以在可接受的时间内完成
确定性：算法中的每一步都有确定的含义，不会出现二义性
可行性：算法的每一步都是可行的，也就是说每一步都能够执行有限的次数完成

常见时间复杂度排序:
O(1) < O(logn) < O(n) < O(nlogn) < O(n^2) < O(n^3) < O(2^n) < O(n!) < O(n^n)
'''



# 引入题1: 如果 a+b+c=1000，且 a^2+b^2=c^2（a,b,c 为自然数），如何求出所有a、b、c可能的组合?

# 解法:穷举法
# a从0到1000循环
# 在a循环的每一次,b也从0到1000循环
# 在a,b循环的每一次,c=1000-a-b,判断是否满足平方和
# 如果满足,则输出a,b,c,不满足,继续循环,直至循环完成
def method_one():
    for a in range(1001):
        for b in range(1001):
            c = 1000 - a - b
            if a**2+b**2 == c**2:
                print("a=%d,b=%d,c=%d" % (a,b,c))

# 对method_one进行进一步改进        
def method_two():
    for a in range(1001):
        for b in range(1001-a):
            c = 1000 - a - b
            if a**2+b**2 == c**2:
                print("a=%d,b=%d,c=%d" % (a,b,c))

# if __name__ == "__main__":
#     start_time = time.time()
#     method_one()
#     end_time = time.time()
#     print("method one spend time: %f 秒" % (end_time-start_time)) 

'''
a=0,b=500,c=500
a=200,b=375,c=425
a=375,b=200,c=425
a=500,b=0,c=500
method one spend time: 0.188000 秒
'''
# method two spend time: 0.088000 秒


# 用来测试的模块timer模块

def testTimer_one():
    mylist = []
    for i in range(1001):
        mylist  = mylist + [i]
        
def testTimer_two():
    mylist = []
    for i in range(1001):
        mylist += [i]

def testTimer_three():
    mylist = []
    for i in range(1001):
        mylist.append(i)
        
def testTimer_four():
    mylist = []
    for i in range(1001):
        # 通过insert向列表尾部插入i
        mylist.insert(1000,i)
                
def testTimer_five():
    mylist = [x for x in range(1001)]
        
def testTimer_six():
    mylist = list(range(1001))
    
def testTimer_seven():
    mylist = []
    for i in range(1001):
        # 通过insert向列表头部插入i
        mylist.insert(0,i)
      
if __name__ == "__main__":  
    t1 = timeit.Timer("testTimer_one()","from __main__ import testTimer_one")
    print("= spend time : %f seconds" % t1.timeit(1000))
    t2 = timeit.Timer("testTimer_two()","from __main__ import testTimer_two")
    print("+ = spend time : %f seconds" % t2.timeit(1000))
    t3 = timeit.Timer("testTimer_three()","from __main__ import testTimer_three")
    print("append spend time : %f seconds" % t3.timeit(1000))
    t4 = timeit.Timer("testTimer_four()","from __main__ import testTimer_four")
    print("insert spend time : %f seconds" % t4.timeit(1000))
    t5 = timeit.Timer("testTimer_five()","from __main__ import testTimer_five")
    print("[x for] spend time : %f seconds" % t5.timeit(1000))
    t6 = timeit.Timer("testTimer_six()","from __main__ import testTimer_six")
    print("[range] spend time : %f seconds" % t6.timeit(1000))
    t7 = timeit.Timer("testTimer_seven()","from __main__ import testTimer_seven")
    print("insert(0,i) spend time : %f seconds" % t7.timeit(1000))
    
    '''
    = spend time : 2.108793 seconds
    + = spend time : 0.170504 seconds
    append spend time : 0.096325 seconds
    insert spend time : 0.182979 seconds
    [x for] spend time : 0.036725 seconds
    [range] spend time : 0.010788 seconds
    insert(0,i) spend time : 0.428430 seconds
    '''

    
