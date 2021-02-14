from t2scene import Scene
import pygame
import sys
from t2tools import Console
from t2score import Score
from t2outImage import OutImage
from t2grid import Grid
from t2imageObject import imageObject
from t2voiceObject import VoiceObject
from t2timer import Timer


class GameScene(Scene):
    """docstring for GameScene"""

    def __init__(self, name, env):
        super(GameScene, self).__init__(name, env)
        self.mytime = None
        self.myscore = None

        self.oi = OutImage(self.env)
        self.bg = None

    def start(self):
        # 场景在第一次加载时载入内容
        if self.flag == False:
            # 这里是初始化内容
            self.env['score'] = 1000
            self.mytime = Timer(427, self.env)
            self.myscore = Score(self.env)
            self.flag = True
            self.oi = OutImage(self.env)
            self.bg = imageObject(src='./img/zhuanqiang.jpg')
            # 放音乐
            pygame.mixer.music.load('./voice/game.mp3')
            pygame.mixer.music.play(0, 0.0)

            Console.log("成功载入" + self.name + "场景数据包")

    # 屏幕指针
    def update(self, screen):
        # 每帧要执行内容
        # 本场景的编号为2
        if self.env['scene'] == 2:
            self.start()
            # 绘制背景
            self.bg.draw(screen)
            # 从这里开始写渲染代码
            # color=(0,0,0)
            # screen.fill(color)
            self.oi.randomDraw(self.env['deltaTime'], 2000, screen)
            # 画背景

            # 时间与分数图层是画在最顶层的
            timeImage = self.mytime.getTimeRender()
            timeImage.draw(screen)
            scoreImage = self.myscore.getScoreRender()
            scoreImage.draw(screen)
            if self.env['score'] < 0:
                self.env['scene'] = 3

        else:
            self.flag = False

    # 事件,处理来自
    def event(self, events):
        # 要处理的事件
        if self.env['scene'] == 2:
            if events.type == pygame.KEYDOWN:
                self.oi.killByEvent(events)
