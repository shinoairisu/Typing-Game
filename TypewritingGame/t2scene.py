from t2tools import Console
import pygame
import sys
#重要共通类
class Scene(object):
	"""docstring for Scene"""
	#场景类是所有场景的父类，也是试验类
	#主要用于定义一些公用方法
	#名字,单例模式的环境变量
	def __init__(self, name,env):
		super(Scene, self).__init__()
		self.name = name
		self.env=env
		#是否被初始化了
		self.flag=False
		Console.log("成功载入"+self.name+"场景代码")

	def start(self):
		#场景在第一次加载时载入内容
		if self.flag==False:
			#这里是初始化内容
			self.flag=True
			Console.log("成功载入"+self.name+"场景数据包")

	#屏幕指针
	def update(self,screen):
		#每帧要执行内容
		if self.env['scene']==0:
			self.start()

	#事件,处理来自
	def event(self,events):
		#要处理的事件
		pass
		