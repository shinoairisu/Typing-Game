import time
import pygame
from t2autoImage import AutoImage
from t2grid import Grid
from t2score import Score
import random
# 一个游戏场景只能有唯一的OutImage对象
# 这个对象用于对图像的管理，比如定时释放一张图片
# 注意这个类是专门为此游戏设计，所以并不通用与其他
# 与Grid类配合


class OutImage(object):
    """docstring for OutImage"""

    def __init__(self, env):
        super(OutImage, self).__init__()
        self.env = env
        self.alphabet = []  # 存储读入的图像数据
        self.maps = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                     'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        for i in self.maps:
            src = './img/' + i + '.png'
            objects = pygame.image.load(src)
            objects = objects.convert_alpha()
            # objects.set_colorkey([255,255,255])
            # objects.set_alpha(50)
            self.alphabet.append(objects)

        self.stack = []
        self.deltatime=0


    # 每隔一段时间,产生一部分新字母,时间以秒计算
    def randomDraw(self, deltatime, time, screen):
        self.deltatime += deltatime
        if self.deltatime * 1000 > time:
            self.deltatime=0
            # self, env, name, src=None, objects=None, png=False
            num = random.randint(0, 8)
            ggd = Grid(self.env['screenWidth'], self.env['screenHeight'])
            ggd.cutTo(10, 10)
            for i in range(num):
                #..............
                xnum = ggd.getX()
                #............
                alpha = random.choice(range(26))
                tempImg = self.alphabet[alpha]
                x = AutoImage(self.env, name=self.maps[alpha], objects=tempImg)

                # tempImg.set_alpha(100)
                x.setXY(xnum, 0)
                self.stack.append(x)

        # 删除Flag为False的元素以及被点击过的元素
        t1 = []
        for x in self.stack:
            if x.flag == True and x.isclicked == False:
                t1.append(x)
        self.stack = t1

        # 绘制所有栈里的元素
        for x in self.stack:
            x.drawDown(deltatime, screen)

    # 如果键盘事件触发，借助此函数传递事件
    def killByEvent(self, event):
        tt=0
        for x in self.stack:
            if x.imgEventClick(event)==True:
                tt+=1
            # if x.imgEventClick(event) == True:
            #     return True
            
                # ai=0
        #按错了扣100
        if tt==0:
            self.env['score']-=500
        


