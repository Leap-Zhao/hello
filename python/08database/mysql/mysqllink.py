#!usr/bin/env python
# coding=utf-8

import redis
import MySQLdb
import json

# import sys
# reload(sys)
# sys.setdefaultencoding("utf-8")

def process_item():
	# 创建redis数据库连接
	rediscli = redis.Redis(host="192.168.191.2",port=6379,db=0)
	# 创建mysql数据库连接
	mysqlcli = MySQLdb.connect(host="127.0.0.1",port=3306,user="root",passwd="1995421123",db="practice",charset="utf8")



	offset = 0
	while True:
		# 将数据从redis里pop出来 
		source,data = rediscli.blpop("tencent:items")
		item = json.loads(data)

		try:
			# 创建mysql操作游标对象,可以执行mysql语句对象
			cursor = mysqlcli.cursor()
			str_sql = "insert into t_tencent_position values (%s,%s,%s,%s,%s,%s)"
			cursor.execute(str_sql,[item['positionName'],item['publishTime'],item['positionLink'],item['peopleNum'],item['positionType'],item['workLocation']])

			# 提交事务
			mysqlcli.commit()

			# 关闭游标
			cursor.close()

			offset += 1
			print offset
		except:
			pass


	# print offset 


if __name__ == '__main__':
	process_item()