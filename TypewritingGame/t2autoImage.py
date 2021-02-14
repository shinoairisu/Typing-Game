from t2imageObject import imageObject
from t2tools import Console

class AutoImage(imageObject):
    """docstring for AutoImage"""
    # 本类是对于imageObject特异化的类
    # 用于自主对于分数的控制

    def __init__(self, env, name, src=None, objects=None, png=False):
        super(AutoImage, self).__init__(src, objects, png)
        self.env = env
        self.downspeed = 1000  # 每speed秒向下移动一格
        self.downdeltatime=0 # 积累时间用
        self.name=name #数组是根据这个判定点击是否正确的
        self.flag=True # True指的是未到销毁的时候。一旦到底部,就会显示为False,从而被销毁。
        # self.isControl=False # 这里是说，False时是不受drawDown
        
        # self.

    #这其实是一种特效
    #但是携带了下落到底端时会扣分的功能
    def drawDown(self, deltatime,screen):
        self.downdeltatime+=deltatime
        # if self.isAlphain==False:
        #     self.alphain(deltatime)
        #     print(self.name)
        
        if self.downdeltatime*1000>self.downspeed and self.isExplodeStart==False:
            if self.y>=self.env['screenHeight']:
                self.flag=False
                #掉出世界扣100
                self.env['score']-=100
            else:
                self.transY(60)
            self.downdeltatime=0
        self.draw(screen)
        if self.y>400:
            self.flashme(200,deltatime)
        self.explode(deltatime)



    #这个函数需要场景配合
    #在event下方放置outImage的event函数。outImage会从栈的后方向前搜索,按下的按钮如果存在
    #就会消除并加分,如果搜索完也没找到，就会扣分
    #消除的话就会找到这个函数,这个函数写该图片被点击后的效果,可以在这里写特效
    def imgEventClick(self,event):
        if event.key==Console.getkeyCode(self.name):
            self.env['score']+=100
            self.isExplodeStart=True
            # print('进来了！！！！！')
            return True
        else:
            return False

