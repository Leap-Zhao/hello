#coding=utf-8

import pymongo
import pprint

'''
命令行下mongodb常用操作
0. 查看所有数据库 show dbs
1. 打开/创建某一数据库 : use localtest
2. 查看当前数据库下的集合Collections : show collections
3. 查看某一集合的数据(此处以user集合为例): db.user.find()
4. 对集合中插入一行数据(插入参数为字典dict): db.user.insert({'name':'赵三'})
5. 删除某一数据库: db.dropDatabase()
'''


# 连接MongoDB数据库客户端
client = pymongo.MongoClient('localhost',27017)
# 获取localtest数据库
db = client['localtest']
# 获取user表/user的Collection
userCollection = db['user']
# 往user集合中以字典形式插入一行数据
userCollection.insert({'name':'wangwu'})
# 获取user集合中的所有数据,返回Cursor对象(此对象可迭代)
userDataCursor = userCollection.find()
# 迭代输出user集合中存储的数据(数据以字典形式存储)
for userData in userDataCursor:
    # 此处打印的是字典
    print("row: %s" % userData)
    # 此处打印的是字典的内容
    for k,v in userData.iteritems():
        print k,v