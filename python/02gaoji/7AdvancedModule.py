#coding=utf-8

# hashlib模块
# 除了md5加密,还有sha256加密 hashlib.sha256()
import hashlib
md5Obj = hashlib.md5()  # 以md5加密方式创建hash对象,共128个比特位
print(md5Obj)  # <md5 HASH object @ 00000000029D1EE0>
md5Obj.update('password') # 更新哈希对象:对需加密的字符串对象进行加密
print(md5Obj.hexdigest()) # 返回十六进制数字字符串 128bit=32个16进制位
# 5f4dcc3b5aa765d61d8327deb882cf99 



# -------------------
# == 与 is 的区别
# -------------------
# == 用来判断值是不是相等
# is 用来判断是不是一片内存区域(id()方法可以查看内存地址)
a = [11,22]
b = [11,22]
c = a
print(a==b)  # True
print(a is b) # False
print(id(a)) # 43532232
print(id(b)) # 43550088
print(id(c))  # 43532232
print(a is c) # True


# copy模块
# ------------------------
# 深拷贝 与 浅拷贝
# = ; copy.deepcopy() ; copy.copy()
# ------------------------
# 浅拷贝 : (一浅永浅)两个变量指向同一个内存空间,只用了一个内存空间  赋值= 
source = ['hello','world'] 
soft_copy = source
# 深拷贝 : 两个变量指向不同的内存空间,用了两个内存空间 
# 注意: copy.deepcopy(source) (一深永深)
# 若原变量中包含引用的其它变量(其它内存空间),那么会递归地进行深拷贝

# 注意: copy.copy(source)
# 对于可变类型: (一深其浅) 若原变量中包含引用的其它变量(其它内存空间),那么只会深拷贝第一层,之后都是浅拷贝(指向一片内存)
# 对于不可变类型:(一浅再浅) 相当于浅拷贝
import copy
deep_copy = copy.deepcopy(source)



# sys模块
# 查看系统导包路径 sys.path 返回路径的列表
import sys
print(sys.path)

# 将自己的路径添加到系统路径里
# myPath = "/home/feiyue/python"
# sys.path.append(myPath)

# 重新导入修改过的模块 imp.reload(moduleName)  
from imp import *
reload(sys)

# 模块循环导入问题:不要在模块之间相互调用