#coding=utf-8

# 第一个python程序
print("hello,python");

# 输出名片
print("=============");
print("姓名:dongGe  公司名称:itcast");
print("=============");

#单行注释

'''
多行注释的第一行
多行注释的第二行
多行注释的第三行
'''

# python变量和类型
# python是弱类型语言,可以在定义变量时不指定其类型
# 数字类型 Numbers:int(有符号整型),long(长整型),float(浮点型),complex(复数型)
# 布尔类型 Boolean:True,False
# 其它类型 String(字符串),List(列表),Tuple(元组),Dictionary(字典)
# 查看变量类型的方法: type(变量)
print("=======变量和类型=========");
a = 10;
b = "hello";
print(a);
print(b);

# python标识符:
# 数字/字母/下划线组成,数字不能开头
# 区分大小写
# 不能是关键字
# 大驼峰命名:UserName,小驼峰命名:userName

# 怎么查看所有关键字
print("=======查看所有关键字===========");
import keyword
print(keyword.kwlist);

# 输入和输出
# 输出: print("")或print('')或print '',print ''只能用于python2
# print中%s表示字符串,%d表示整数
# 输入:raw_input("input your age");返回的都是字符串
print("==========输入和输出===========");
name  = "dongGe";
company = "baidu";
print("name: %s" % name);
print("name: %s ,company: %s" % (name,company));

age = raw_input("input your age:");
print("your age is %s ,and type is %s" % (age,type(age)));
# input your age:18
# your age is 18 ,and type is <type 'str'>

# python中的运算符
# 算术运算符: +,-,*,/,%,**(幂,a**b表示a的b次方),//(取整除)
# 除法/中:只要有一个浮点数,结果就是浮点数,两个整数相除结果是整数
# 取整除//中:返回商的整数部分 9//2 输出结果 4 , 9.0//2.0 输出结果 4.0

# 加号+: 当两个参数为字符串时,为拼接字符串的用法
# 乘号*: 字符串*数字,为字符串加倍

# 赋值运算符: = ,+=,-=,*=,/=,%=,**=,//=
print("=========运算符========");
str1 = "hello,";
str2 = "python";
str3 = "nihao"*3;
print("%s,%s"%((str1+str2),str3));

# result*=num1+num2
num1 = 10;
num2 = 2;
result = 3;
result *= num1+num2
print("%d"% result);
# 结果是36,因为算术运算符的级别比赋值运算符高,所以先+再*=

# 比较运算符: >,<,==,>=,<=,,!=(不等于,还有一种写法<>)
# 逻辑运算符: and(与),or(或),not(非),例子; x and y,x or y, not x

# if判断语句
print("===========if判断========");
# 此时的age是之前自己输入的,是字符串类型,用int(str,[,base])方法转换为int类型
age = int(age);
print("%s" % type(age));
# 判断一个值是否等于另一个值用"==",而"="是赋值操作
if age==18:
	print("I'm just a grown-up"); #我刚好成年
elif age>18:
	print("I have grown up"); # 我已成年了
else:
	print("I'm still underage"); # 我还未成年

# if嵌套
chepiao = 1; # 1表示有车票,0表示没有车票
daoChang = 10; # 表示刀的长度,单位为cm
if chepiao == 1:
	print("you can go in");
	if daoChang<10:
		print("you can go to the train");
	else:
		print("you can not go to the train,please wait for police");
else:
	print("you should go to buy a ticket");

# 循环相关
print("========while循环=========");
i = 0;
while i<5:
	print("打印5遍这句话");
	i+=1;

for i in range(5):
	print("i=%d"%i);

# 循环嵌套
'''输出:
*
* *
* * *
* * * * 
* * * * *
'''
i=1;
while i<=5:
	j=1
	while j<=i:
		print("* "),
		j+=1
	print("")
	i+=1

print("第二种方式:");
i=1
while i<=5:
	print("* "*i)
	i+=1

# break 和 continue
# break/continue只能用在循环中，除此以外不能单独使用
# break/continue在嵌套循环中，只对最近的一层循环起作用

# python函数
print("==========python function===========")
# 函数定义
def printName():
	print("my name is feiyue");
#函数调用
printName()
# 调用系统函数
# 时间函数
import time
# time.time()返回从1970至今的秒数,返回类型为<type 'float'>
timeFrom1970 = time.time()
# localtime():返回<type 'time.struct_time'>类型,结构化时间类型
timeStructure = time.localtime(timeFrom1970)
# asctime(): 返回<type 'str'> 
timeStr = time.asctime(timeStructure)

print(timeFrom1970)  
# 1523580786.016
print(timeStructure) 
# time.struct_time(tm_year=2018, tm_mon=4, tm_mday=13, tm_hour=8, tm_min=53, tm_sec=58, tm_wday=4, tm_yday=103, tm_isdst=0)
print(timeStr) 
# 'Fri Apr 13 08:53:58 2018'

