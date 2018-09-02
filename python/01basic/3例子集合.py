#coding=utf-8

while True:
	print("======综合系统选择功能=====")
	print("======1.石头剪刀布游戏=====")
	print('======2.名片管理器======')
	print("======3.学生管理系统=====")
	print("======4.计算n个数的和与平均值=====")
	print("======5.退出综合系统======")

	gameNum = int(raw_input("please input a number : "))
	if gameNum == 1:
		# if的应用---剪刀,石头,布游戏
		while True:
			# 玩家输入
			player = raw_input("please input : scissors(0) stones(1) cloth(2):");
			player = int(player);
			# 电脑操作
			import random;
			computer = random.randint(0,2); #随机数0-2(包括0和2)

			print("player:%d,computer:%d" % (player,computer));
			if player==computer:
				# 平局
				print("draw");
			elif (player==0 and computer==2) or (player==1 and computer==0) or (player==2 and computer==1):
				print("you win,computer lost");
			elif (player==2 and computer==0) or (player==0 and computer==1) or (player==1 and computer==2):
				print("you lost,computer win");
			else:
				print("you put error");

			conFlag = raw_input("do you want to continue? y/n : ")
			if conFlag == "n":
				break


	elif gameNum ==2:
		# 列表的应用--名片管理器1.0
		userList = ["xiaoming","xiaohong","xiaozhang"];
		while True:
			print("======功能菜单====")
			print("====1.查看所有用户名====")
			print("====2.添加用户名====")
			print("====3.修改用户名====")
			print("====4.删除用户名====")
			print("====5.退出系统====")

			userSelection = int(raw_input("请输入您要选择的选项: "))

			if userSelection == 1:
				print("所有的用户如下: ")
				for i in range(len(userList)):
					print("%d . %s" % (i,userList[i]))
			elif userSelection == 2:
				newUserName = raw_input("请输入要添加的用户的名称: ")
				userList.append(newUserName)
				print("添加用户名成功")
				print("所有的用户如下: ")
				for i in range(len(userList)):
					print("%d . %s" % (i,userList[i]))
			elif userSelection == 3:
				print("所有的用户如下: ")
				for i in range(len(userList)):
					print("%d . %s" % (i,userList[i]))
				userNum = int(raw_input("请输入您要修改的用户编号"))
				changeUserName = raw_input("请输入新的用户名称")
				userList[userNum] = changeUserName
				print("修改成功,新的用户如下:")
				for i in range(len(userList)):
					print("%d . %s" % (i,userList[i]))
			elif userSelection == 4:
				for i in range(len(userList)):
					print("%d . %s" % (i,userList[i]))
				userNum = int(raw_input("请输入您要删除的用户编号"))
				del userList[userNum]
				print("删除成功")
				for i in range(len(userList)):
					print("%d . %s" % (i,userList[i]))
			elif userSelection == 5:
				print("您已成功退出系统")
				break
			else:
				print("您的输入有误,请重新输入!")
				continue

			conFlag = raw_input("do you want to continue? y/n : ")
			if conFlag == "n":
				break


	elif gameNum == 3:
		# 字典应用 学生管理系统
		nameList = []
		while True:
			print("-"*30)
			print("======python版学生管理系统======")
			print("======1.添加学生信息======")
			print("======2.删除学生信息======")
			print("======3.修改学生信息======")
			print("======4.查询学生信息======")
			print("======5.退出系统======")

			optionNum = int(raw_input("请进行选择(数字) :"))

			if optionNum == 1:
				newStuName = raw_input("输入学生姓名: ")
				newStuAge = int(raw_input("输入学生年龄: "))
				# 用元组来代表一个学生
				newStuInfo = {"name":newStuName,"age":newStuAge}
				nameList.append(newStuInfo)
				print("添加学生成功")
				print(nameList)
			elif optionNum ==2:
				# 没有学生信息时直接跳过此次循环
				if len(nameList) == 0:
					print("sorry,当前系统中没有任何学生的信息")
					continue

				# 如果有学生信息,先提示有哪些学生
				i = 0
				for ele in nameList:
					print("%d == name : %s,age : %d" % (i,ele["name"],ele["age"]))
					i+=1  # 记住,py没有++操作
				selectNum = int(raw_input("输入要选择学生的编号 : "))
				if selectNum < len(nameList) and selectNum >=0:
					del nameList[selectNum]
				print(nameList)
			elif optionNum	==3:
				# 没有学生信息时直接跳过此次循环
				if len(nameList) == 0:
					print("sorry,当前系统中没有任何学生的信息")
					continue

				# 如果有学生信息,先提示有哪些学生
				i = 0
				for ele in nameList:
					print("%d == name : %s,age : %d" % (i,ele["name"],ele["age"]))
					i+=1  # 记住,py没有++操作
				selectNum = int(raw_input("输入要选择学生的编号 : "))
				if selectNum < len(nameList) and selectNum >=0:
					newName = raw_input("请输入新的姓名 : ")
					newAge = int(raw_input("请输入新的年龄 : "))
					nameList[selectNum]['name'] = newName
					nameList[selectNum]['age'] = newAge
					print(nameList)
				else:
					print("您的输入有误")
			elif optionNum == 4:
				searchName = raw_input("请输入您要查询的姓名: ")
				for ele in nameList:
					if ele['name'] == searchName:
						print("恭喜你找到了,信息如下")
						print("name: %s, age:%d" % (ele['name'],ele['age']))
						continue
				print("没有找到对应的学生信息")
			elif optionNum == 5:
				print("您已成功退出系统")
				break
			else:
				print("您的输入有误,请重新输入!")
				continue

			conFlag = raw_input("do you want to continue? y/n : ")
			if conFlag == "n":
				break

	elif gameNum == 4:
		# 函数应用
		# 编写一个函数: 求n个数的和
		def sumByN(n=1):
			sum1 = 0
			i=0
			while i<n:
				num = int(raw_input("请输入第%d个数 : " % (i+1)))
				sum1 += num
				i += 1
			return sum1
		# 编写一个函数,求n个数的平均值
		def aveByN(n=1):
			sum1 = sumByN(n)
			print("sum = %d " % sum1)
			average = sum1/float(n)
			print("average = %f" % average)

		caulcateNum = int(raw_input("输入你要计算几个数: "))
		aveByN(caulcateNum)

	elif gameNum == 5:
		print("您已成功退出综合系统")
		break

	else:
		print("您的输入有误,请重新选择")
		continue





