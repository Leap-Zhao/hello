#coding=utf-8

import pygame
import time
from pygame.locals import *
import random


'''
# 面向过程的写法

def main():
	#1.创建一个窗口,用来显示内容
	screen = pygame.display.set_mode((480,852),0,32)
	#2.创建一个与窗口一样大小的图片,用来充当背景
	background = pygame.image.load("./feiji/background.png")
	#3.创建一个飞机的图片
	hero = pygame.image.load("./feiji/hero1.png")

	# 飞机移动的x坐标与y坐标
	heroX = 200
	heroY = 700

	#.把图片放到窗口中显示
	while True:
		# 设定需要显示的背景图
		screen.blit(background,(0,0))
		# 设定飞机显示的位置
		screen.blit(hero,(heroX,heroY))
		#  更新所需要显示的内容
		pygame.display.update()

		# 捕获事件响应
		for event in pygame.event.get():

			# 判断是否点击退出按钮
			if event.type == pygame.QUIT:
				print("exit")
				pygame.quit()
				exit()
			elif event.type == KEYDOWN:
				# 控制飞机左右移动
				if event.key == K_d or event.key == K_RIGHT:
					print("right")
					heroX += 10
				elif event.key == K_a or event.key ==K_LEFT:
					print("left")
					heroX -= 10
				elif event.key == K_SPACE:
					print("space")

		# 3.3 延时处理(不让cpu崩溃)
		# time.sleep(0.1)


if __name__ == "__main__":
	main()
'''


'''
# 面向对象的写法
class HeroPlane(object):
	# 飞机有初使的x,y与image图像
	def __init__(self,screen_temp):
		self.x = 210
		self.y = 700
		self.screen  = screen_temp
		self.image = pygame.image.load("./feiji/hero1.png")
		self.bulletList = [] # 存储发出去的子弹对象引用

	# 显示飞机的位置
	def display(self):
		self.screen.blit(self.image,(self.x,self.y))
		for bullet in self.bulletList:
			bullet.display()
			bullet.move()
			# 当当前的子弹越界了,就要在列表中删除该子弹
			if bullet.judge():
				self.bulletList.remove(bullet)

	def moveLeft(self):
		self.x -= 8

	def moveRight(self):
		self.x += 8

	def moveUp(self):
		self.y -= 8

	def moveDown(self):
		self.y += 8

	def fire(self):
		self.bulletList.append(Bullet(self.screen,self.x,self.y))

# 子弹类(Bullet)
class Bullet(object):
	def __init__(self,screen_temp,x,y):
		self.x = x + 40
		self.y = y - 25
		self.screen = screen_temp
		self.image = pygame.image.load("./feiji/bullet.png")

	# 显示子弹的方法
	def display(self):
		self.screen.blit(self.image,(self.x,self.y))

	# 子弹移动的方法:不断向上
	def move(self):
		self.y -= 15

	# 判断子弹是否越界的方法
	def judge(self):
		if self.y < 0:
			return True
		else:
			return False

# 敌机类 EnemyPlane
class EnemyPlane(object):
	def __init__(self,x,y,screen,image):
		# 敌机的x,y位置,screen窗口,显示的图像
		self.x = x
		self.y = y
		self.screen = screen
		self.image = image
		# 敌机行驶的方向
		self.direction = "right"
		# 敌机的子弹列表
		self.bulletList = []
	# 显示敌机的方法
	def display(self):
		self.screen.blit(self.image,(self.x,self.y))
		# 显示敌机的子弹
		for bullet in self.bulletList:
			bullet.display()
			bullet.move()
			# 判断子弹是否越界
			if bullet.judge():
				self.bulletList.remove(bullet)
	# 敌机移动的方法
	def move(self):
		# 通过direction属性控制方向
		if self.direction == "right":
			self.x += 8
		elif self.direction == "left":
			self.x -= 8
		if self.x > 480-50:
			self.direction = "left"
		elif self.x <2 :
			self.direction = "right"
	# 敌机发射子弹的方法
	def fire(self):
		# 让敌机发射频率变慢
		random_num = random.randint(1,100)
		if random_num == 8 or random_num == 20:
			# 概率为1/50,循环50次能发射一次 
			self.bulletList.append(EnemyBullet(self.x+25,self.y+40,self.screen))

# 敌机子弹类(EnemyBullet)
class EnemyBullet(object):
	def __init__(self,x,y,screen_temp):
		self.x = x 
		self.y = y 
		self.screen = screen_temp
		self.image = pygame.image.load("./feiji/bullet1.png")

	# 显示子弹的方法
	def display(self):
		self.screen.blit(self.image,(self.x,self.y))

	# 子弹移动的方法:不断向下
	def move(self):
		self.y += 8

	# 判断子弹是否越界的方法
	def judge(self):
		if self.y > 852:
			return True
		else:
			return False

# 定义按键控制的方法
def keyControl(heroTemp):
	for event in pygame.event.get():
		# 判断是否点击退出按钮
		if event.type == pygame.QUIT:
			print("exit")
			pygame.quit()
			exit()
		elif event.type == KEYDOWN:
			# 控制飞机左右移动
			if event.key == K_d or event.key == K_RIGHT:
				print("right")
				heroTemp.moveR ight()
			elif event.key == K_a or event.key ==K_LEFT:
				print("left")
				heroTemp.moveLeft()
			elif event.key == K_w or event.key == K_UP:
				print("up")
				heroTemp.moveUp()
			elif event.key == K_s or event.key ==K_DOWN:
				print("down")
				heroTemp.moveDown()
			elif event.key == K_SPACE:
				print("space")
				heroTemp.fire()



def main():
	# 创建一个窗口,用来显示内容
	screen = pygame.display.set_mode((480,852),0,32)
	# 创建一个与窗口一样大小的图片,用来充当背景
	background = pygame.image.load("./feiji/background.png")
	# 创建敌机图像
	enemyImage = pygame.image.load("./feiji/enemy0.png")
	# 创建一个飞机对象
	hero = HeroPlane(screen)
	# 创建一个敌机对象
	enemyPlane = EnemyPlane(0,0,screen,enemyImage)

	#.把图片放到窗口中显示
	while True:
		# 设定需要显示的背景图
		screen.blit(background,(0,0))
		# 显示飞机
		hero.display()
		# 显示敌机并移动并发子弹
		enemyPlane.display()
		enemyPlane.move()
		enemyPlane.fire()
		# 更新所需要显示的内容
		pygame.display.update()
		# 捕获事件响应
		keyControl(hero)
		# 延时处理(不让cpu崩溃)
		time.sleep(0.01)
	

if __name__ == "__main__":
	main()

'''


# 面向对象进阶(提取基类的写法)

import pygame 
import time
from pygame.locals import *
import random

'''
飞机大战游戏制作步骤:
1.显示飞机和敌机
2.让飞机和敌机移动
3.让飞机和敌机发出子弹 并优化
4.让飞机和敌机产生爆炸效果
'''

class BaseBullet(object):
	def __init__(self, x,y,screen,image):
		self.x = x
		self.y = y
		self.screen = screen
		self.image = image

	# 显示子弹的方法
	def display(self):
		self.screen.blit(self.image,(self.x,self.y))

	# 移动子弹的方法
	def move(self):
		pass

	# 判断子弹是否越界的方法
	def judge(self):
		pass

class EnemyBullet(BaseBullet):
	def __init__(self,x,y,screen,image):
		BaseBullet.__init__(self,x,y,screen,image)

	def move(self):
		self.y += 5

	def judge(self):
		if self.y > 800:
			return True
		else:
			return False

class HeroBullet(BaseBullet):
	def __init__(self,x,y,screen,image):
		BaseBullet.__init__(self,x,y,screen,image)

	def move(self):
		self.y -= 10

	def judge(self):
		if self.y < 100:
			return True
		else: 
			return False

# 定义一个飞机的基类 Plane
class Plane(object):
	# 初始化x,y位置,窗口,图像
	def __init__(self,x,y,screen,image):
		self.x = x
		self.y = y
		self.screen =screen
		self.image = image
		# 定义飞机的子弹列表
		self.bulletList = []
		# 飞机是否爆炸
		self.hit = False
		self.bomb_list = [] # 爆炸时的图片列表
		self.image_num = 0
		self.image_index = 0 # 用来记录当前要显示的爆炸效里的图片的序号

	# 显示飞机的方法
	def display(self):
		# 如果被击中,显示爆炸的效果,否则显示正常的效果
		if self.hit == True:
			self.screen.blit(self.bomb_list[self.image_index],(self.x,self.y))
			self.image_num += 1
			if self.image_num == 3:
				self.image_num = 0
				self.image_index += 1
			if self.image_index > 3:
				exit()
		else:
			self.screen.blit(self.image,(self.x,self.y))
		# 不管飞机在不在,发出去的子弹都要显示
		for bullet in self.bulletList:
			bullet.display()
			bullet.move()
			if bullet.judge():
				self.bulletList.remove(bullet)

	# 飞机发射的方法
	def fire(self):
		pass

	# 是否爆炸
	def bomb(self):
		pass


# 定义自己的飞机--HeroPlane
class HeroPlane(Plane):
	def __init__(self, x,y,screen,image):
		Plane.__init__(self,x,y,screen,image);
		# 定义飞机爆炸的相关信息
	
	def moveLeft(self):
		if self.x > 0:
			self.x -= 8
	def moveRight(self):
		if self.x < 380:
			self.x += 8

	# 飞机发射的方法
	def fire(self):
		heroBulletImage = pygame.image.load("./feiji/bullet.png")
		self.bulletList.append(HeroBullet(self.x+40,self.y-20,self.screen,heroBulletImage))

	# 控制飞机的方法
	def keyControl(self):
		for event in pygame.event.get():
			if event.type == QUIT:
				# 退出游戏
				pygame.quit()
				# 退出系统
				exit()
			elif event.type == KEYDOWN:
				if event.key == K_a or event.key == K_LEFT:
					self.moveLeft()
				elif event.key == K_d or event.key == K_RIGHT:
					self.moveRight()
				elif event.key == K_SPACE:
					self.fire()
				elif event.key == K_b:
					print("bomb")
					self.bomb()

	def __create_images(self):
		print("create2")
		self.bomb_list.append(pygame.image.load("./feiji/hero_blowup_n1.png"))
		self.bomb_list.append(pygame.image.load("./feiji/hero_blowup_n2.png"))
		self.bomb_list.append(pygame.image.load("./feiji/hero_blowup_n3.png"))
		self.bomb_list.append(pygame.image.load("./feiji/hero_blowup_n4.png"))

	def bomb(self):
		self.__create_images() # 向列表中添加图片
		self.hit = True;

# 定义敌机  EnemyPlane
class EnemyPlane(Plane):
	"""docstring for EnemyPlane"""
	def __init__(self, x,y,screen,image):
		Plane.__init__(self,x,y,screen,image)
		self.position = "right"

	def move(self):
		if self.position == "right":
			self.x +=8
		elif self.position == "left":
			self.x -=8

		if self.x > 480-50:
			self.position = "left"
		elif self.x < 0:
			self.position = "right"

	# 飞机发射的方法
	def fire(self):
		# 让敌机子弹发射频率降低
		random_num = random.randint(1,30)
		if random_num == 14:
			enemyBulletImage = pygame.image.load("./feiji/bullet1.png")
			self.bulletList.append(EnemyBullet(self.x+25,self.y+40,self.screen,enemyBulletImage))


def main():
	# 创建窗口
	screen = pygame.display.set_mode((480,852),0,32)
	# 创建背景图
	backgroundImage = pygame.image.load("./feiji/background.png")
	# 创建heroPlane的图
	heroPlaneImage = pygame.image.load("./feiji/hero1.png")
	# 创建EnemyPlane的图
	enemyPlaneImage = pygame.image.load("./feiji/enemy0.png")
	# 创建各个对象
	heroPlane = HeroPlane(240,700,screen,heroPlaneImage)
	enemyPlane = EnemyPlane(0,0,screen,enemyPlaneImage)
	# 时间间隔显示各个对象
	while True:
		# 背景加载到窗口上
		screen.blit(backgroundImage,(0,0))
		# 显示飞机和敌机
		heroPlane.display()
		enemyPlane.display()
		# 让敌机移动
		enemyPlane.move()
		# 让敌机发射
		enemyPlane.fire()
		# 更新窗口的画面
		pygame.display.update()
		# 获取事件响应
		heroPlane.keyControl()
		# 设置时间间隔,防止cpu占用过高
		time.sleep(0.01)

if __name__ == "__main__":
	main()

