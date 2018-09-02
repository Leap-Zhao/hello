#coding=utf-8

from threading import Thread
import time

# 下面两个方法希望各对g_num加1000000
# 但两个线程对同一个全局变量操作时会相互干扰,不能保证其原子性
'''
g_num = 0
def test1():
    global g_num
    for i in range(1000000):
        g_num += 1
    print("---test1---g_num=%d"%g_num)

def test2():
    global g_num
    for i in range(1000000):
        g_num += 1
    print("---test2---g_num=%d"%g_num)

p1 = Thread(target=test1)
p1.start()

#time.sleep(3) #取消屏蔽之后 再次运行程序，结果会不一样

p2 = Thread(target=test2)
p2.start()

print("---g_num=%d---"%g_num)

'''


# 下面考虑使用轮询解决线程间的原子性问题
# 轮询的缺点,当线程1执行时,线程2不断判断,浪费资源且效率不高
g_num = 0
g_flag = 1

def test1():
    global g_num
    global g_flag
    if g_flag == 1:
        for i in range(1000000):
            g_num += 1
        g_flag = 0

    print("---test1---g_num=%d"%g_num)

def test2():
    global g_num
    #轮询
    while True:
        if g_flag != 1:
            for i in range(1000000):
                g_num += 1
            break

    print("---test2---g_num=%d"%g_num)

p1 = Thread(target=test1)
p1.start()

p2 = Thread(target=test2)
p2.start()

print("---g_num=%d---"%g_num)


# 下面用互斥锁解决线程操作的原子性问题
# threading.Lock 对象 ,相关方法: lock.qcquire() lock.release()
# 互斥锁:当一个线程对某部分代码上锁,另一个线程必须等待其执行完才能执行

g_num = 0

def test1():
    global g_num
    #这个线程和ｔｅｓｔ2线程都在抢着　对这个锁　进行上锁，如果有１方成功的上锁，那么导致另外
    #一方会堵塞（一直等待）到这个锁被解开为止
    mutex.acquire()
    for i in range(1000000):
        g_num += 1
    mutex.release()#用来对mutex指向的这个锁　进行解锁，，，只要开了锁，那么接下来会让所有因为
                    #这个锁　被上了锁　而堵塞的线程　进行抢着上锁

    print("---test1---g_num=%d"%g_num)

def test2():
    global g_num
    mutex.acquire()
    for i in range(1000000):
        g_num += 1
    mutex.release()

    print("---test2---g_num=%d"%g_num)

#创建一把互斥锁，这个锁默认是没有上锁的
mutex = Lock()

p1 = Thread(target=test1)
p1.start()

#time.sleep(3) #取消屏蔽之后 再次运行程序，结果会不一样，，，为啥呢？

p2 = Thread(target=test2)
p2.start()

print("---g_num=%d---"%g_num)

# 注:锁也可以加在for循环里面的+=1语句上,其时这样更好
# 如果加在for循环里面,最终的结果一定是对的,但是在各自线程内的执行结果不一定正确,
# 例如下面的test1线程print的结果不一定是1000000,但两个线程执行完一个是2000000
'''
def test1():
    global g_num
    for i in range(1000000):
    	mutex.acquire()
        g_num += 1
    	mutex.release()

    print("---test1---g_num=%d"%g_num)
'''