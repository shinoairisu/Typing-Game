import time
import pygame
from t2imageObject import imageObject
#这不是一个很重要的类
class Score(object):
    """docstring for Score"""
    def __init__(self, env):
        super(Score, self).__init__()
        self.env = env

    def getScoreRender(self):
        your_score=u'得分:'+str(self.env['score'])
        my_font = pygame.font.SysFont("kaiti", 20)
        score_surface = my_font.render(your_score, True, (255, 255, 255))
        temp=imageObject(objects=score_surface)
        temp.setXY(400,0)
        return temp

