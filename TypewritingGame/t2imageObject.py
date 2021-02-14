# -*- coding:utf-8 -*-
import pygame
from t2tools import Console
# 图像物体,普通类别,左上角为0,0


class imageObject(object):
    """docstring for gameObject"""
    # 从src绘制或者直接从surface绘制。要么开src，要么开objects

    def __init__(self, src=None, objects=None, png=False):
        super(imageObject, self).__init__()
        # self.isAlphain = False
        # self.isAlphaout = False
        # # self.isExplode=False
        # self.alpha = 0
        self.isDraw = True
        self.isclicked = False
        self.isExplodeStart = False
        self.time = 0
        self.x = 0
        self.y = 0
        #出生点
        self.initx=0
        self.drawTime = 0
        # 这里标记的是image所占用的网格编号
        self.index = 0
        # self.src = src
        if src != None:
            self.imageSource = pygame.image.load(src)
        else:
            self.imageSource = objects

        if png == False and src != None:
            self.imageSource = self.imageSource.convert()
        else:
            self.imageSource = self.imageSource.convert_alpha()

        self.rect = self.imageSource.get_rect()

        # if src != None:
        #     Console.log("成功读取数据:" + src)
        # else:
        #     Console.log("成功读取数据:" + str(objects))

    # 画出图片
    def draw(self, screen):
        if self.isDraw == True:
            screen.blit(self.imageSource, pygame.Rect(self.x, self.y, 0, 0))
    # 移动图片

    def transX(self, moveAdd):
        self.x += moveAdd
    # 移动图片

    def transY(self, moveAdd):
        self.y += moveAdd

    # 强制设置位置,XY代表图片左上角所处位置
    def setXY(self, postX, postY):
        self.x = postX
        self.initx = postX
        self.y = postY

    # 这里的X与Y代表,代表图像中心点所处位置
    def setFromCenterPoint(self, postX, postY):
        self.setXY(postX - self.rect.centerx, postY - self.rect.centery)
        # print(self.rect.centerx)

    # 闪烁特效
    def flashme(self, speed, deltatime):
        self.time += deltatime
        if (1000 * self.time) >= speed:
            self.time = 0
            self.isDraw = not self.isDraw

    # 返回True时说明特效完成
    # # 特效-淡入
    # def alphain(self, deltatime):
    #     if self.alpha <= 255:
    #         self.alpha += 50 * deltatime
    #         # self.imageSource.set_alpha(int(self.alpha))
    #         self.imageSource.set_alpha(50)
    #         print(self.imageSource.get_alpha())
    #         # print('这里有特效'+str(self.alpha))
    #     else:
    #         self.isAlphain = True

    # # 特效-淡出
    # def alphaout(self, deltatime):
    #     self.isAlphaout = True

    # 特效-爆炸-弹飞-结束后会把clicked设置为True
    def explode(self, deltatime):
        if self.isExplodeStart == True:
            if self.x >= 0 and self.x <= 800:
                if self.initx < 400:
                    self.transX(200 * deltatime)
                    self.transY(-300 * deltatime)
                else:
                    self.transX(-200 * deltatime)
                    self.transY(-300 * deltatime)
            else:
                self.isclicked = True
        # 爆炸代码
