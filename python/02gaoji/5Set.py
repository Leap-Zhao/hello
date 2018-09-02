#coding=utf-8

# set()集合: 用大括号{} 表示,可以去除重复元素

# 功能1:去除重复集合
a = [23,44,89,44,1,1,2,2]
a = set(a)
print(type(a))  # <type 'set'>
print(a)    # set([89, 2, 44, 1, 23])
print(list(a))  # [89, 2, 44, 1, 23]

# 功能2: 求交集,并集,补集
str1 = "abcdef"
b = set(str1)
str2 = "defghi"
B = set(str2)
# 交集
print(b&B)  # set(['e', 'd', 'f'])
# 并集
print(b|B)  # set(['a', 'c', 'b', 'e', 'd', 'g', 'f', 'i', 'h'])
# 差集 
print(b-B)  # set(['a', 'c', 'b'])
# 对称差集
print(b^B)  # set(['a', 'c', 'b', 'g', 'i', 'h'])
