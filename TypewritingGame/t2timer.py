from t2imageObject import imageObject
import pygame
#专用工具类之一,非共通类
#这个类决定游戏结束时间，是一个计时器
class Timer(object):
    """docstring for Timer"""
    def __init__(self, time,env):
        super(Timer, self).__init__()
        self.time = time
        self.delatime=0
        self.env=env
    
    def getTimeRender(self):
        self.delatime+=self.env['deltaTime']*1000
        if self.delatime>=1000:
            self.time-=1
            self.delatime=0
        if self.time<0:
            self.env['scene']=3
        your_time=u'剩余时间:'+str(self.time)
        my_font = pygame.font.SysFont("kaiti", 20)
        time_surface = my_font.render(your_time, True, (255, 255, 255))
        return imageObject(objects=time_surface)