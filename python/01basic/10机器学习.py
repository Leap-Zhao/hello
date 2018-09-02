#coding=utf-8

# python机器学习库: scikit-learn 
# 其它必要的package: numpy, Scipy,matplotlib,可使用Anaconda(包含numpy,sipy)









from sklearn.feature_extraction import


from numpy import genfromtxt, zeros
from pylab import *
import sys

data = genfromtxt('data/iris.csv',delimiter=',',usecols=(0,1,2,3)) 
target = genfromtxt('data/iris.csv',delimiter=',',usecols=(4),dtype=str)
print data.shape
print target.shape
print set(target)

reload(sys)
sys.setdefaultencoding('gb18030')
plot(data[target=='setosa',0],data[target=='setosa',2],'bo')
plot(data[target=='versicolor',0],data[target=='versicolor',2],'ro')
plot(data[target=='virginica',0],data[target=='virginica',2],'go')
show()
