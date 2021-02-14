import time
import pygame
import random

#一个游戏场景只能有唯一的Grid类对象
#这个对象用于对图片位置管理，与outimage进行配合，在指定位置放图片
class Grid(object):
    """docstring for Grid"""
    # 这是关于网格信息处理的一个类,是游戏重要的工具类

    def __init__(self, width,height):
        super(Grid, self).__init__()
        self.width = width
        self.height=height
        self.xArray=[]
        self.yArray=[]
        self.instuff=[]#所有在栈里的Rect
        self.outstuff=[]#所有已经被使用的Rect

    #请输入横行以及竖行的数量，需要能整除的数,否则会报异常
    def cutTo(self,xnum,ynum):
        x=int(self.width/xnum)
        y=int(self.height/ynum)
        xtemp=0
        ytemp=0
        for i in range(xnum):
            self.xArray.append(xtemp)
            xtemp+=x
        for i in range(ynum):
            self.yArray.append(ytemp)
            ytemp+=y

    #x是列,y是行
    def getPose(self,yHang,xLie):
      return  pygame.Rect(self.xArray[xLie-1],self.yArray[yHang-1],0,0)

    #本方法用于
    def inList(self):
        pass

    def getX(self):
        xx=random.choice(self.xArray)
        self.xArray.remove(xx)
        return xx