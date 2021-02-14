# -*- coding:utf-8 -*-
from t2scene import Scene
import pygame
import sys
from t2tools import Console
from t2imageObject import imageObject
from t2voiceObject import VoiceObject


class OverScene(Scene):
    """docstring for OverScene"""

    def __init__(self, name, env):
        super(OverScene, self).__init__(name, env)
        self.tu1 = None
        self.zi1 = None

    def start(self):
        # 场景在第一次加载时载入内容
        if self.flag == False:
            # 这里是初始化内容
            pygame.mixer.music.load('./voice/over.mp3')
            pygame.mixer.music.play(0,0.0)
            self.tu1 = imageObject(src="./img/over.png", png=True)
            self.tu1.setFromCenterPoint(
                self.env['screenWidth'] / 2, self.env['screenHeight'] / 2)
            if self.env['score']<=0:
                your_score = u'让你乱按,死了吧!你只有:' + str(self.env['score'])+u'分'
            else:
                your_score = u'最终分数:' + str(self.env['score'])
            my_font = pygame.font.SysFont("kaiti", 50)
            name_surface = my_font.render(your_score, True, (0, 0, 0))
            self.zi1 = imageObject(objects=name_surface)

            # 指数据已经被载入内存
            self.flag = True
            Console.log("成功载入" + self.name + "场景数据包")

    # 屏幕指针
    def update(self, screen):
        # 每帧要执行内容
        if self.env['scene'] == 3:
            self.start()
            # color=(255,255,255)
            # screen.fill(color)
            self.tu1.draw(screen)
            self.tu1.flashme(100, self.env['deltaTime'])
            self.zi1.draw(screen)

    # 事件,处理来自
    def event(self, events):
        # 要处理的事件
        if self.env['scene'] == 3:
            # 要处理的事件
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_RETURN or events.key == pygame.K_KP_ENTER:
                    self.env['scene'] = 2
                    self.flag = False
                elif events.key == pygame.K_ESCAPE:
                    self.env['scene'] = 1
                    self.flag = False
