from t2scene import Scene
import pygame
import sys
from t2tools import Console
from t2imageObject import imageObject
from t2voiceObject import VoiceObject


class StartScene(Scene):
    """docstring for StartScene"""

    def __init__(self, name, env):
        super(StartScene, self).__init__(name, env)
        self.tu1 = None

    def start(self):
        # 场景在第一次加载时载入内容
        if self.flag == False:
            # 这里是初始化内容
            pygame.mixer.music.load('./voice/start.mp3')
            pygame.mixer.music.play(0,0.0)
            self.tu1 = imageObject(src="./img/start.png", png=True)
            self.tu1.setFromCenterPoint(
                self.env['screenWidth'] / 2, self.env['screenHeight'] / 2)
            # 指数据已经被载入内存
            self.flag = True
            Console.log("成功载入" + self.name + "场景数据包")

    # 屏幕指针
    def update(self, screen):
        # 每帧要执行内容
        if self.env['scene'] == 1:
            self.start()
            # color=(255,255,255)
            # screen.fill(color)
            self.tu1.draw(screen)
            self.tu1.flashme(100, self.env['deltaTime'])

    # 事件,处理来自
    def event(self, events):
        if self.env['scene'] == 1:
            # 要处理的事件
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_RETURN or events.key == pygame.K_KP_ENTER:
                    self.env['scene'] = 2
                    self.flag = False
                    # print('变化')
