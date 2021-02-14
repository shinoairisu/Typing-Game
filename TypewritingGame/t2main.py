# -*- coding:utf-8 -*-
import pygame
import sys
from t2tools import Console
from t2sceneStart import StartScene
from t2sceneGame import GameScene
from t2sceneOver import OverScene

Env_All = {'author': '高二四班_薛明昊',
           'deltaTime': 0.16,  # 增量时间
           'scene': 1,  # 场景编号，默认启动场景是1。调试其它场景可以更改此处编号
           'screenWidth':800,#宽度
           'screenHeight':600,#高度
           'score':0
           }

if __name__ == '__main__':
    pygame.init()  # 初始化pygame
    Console.log("游戏启动")
    Console.printEnv(Env_All, "author")
    FPS = 60
    FPSClock = pygame.time.Clock()
    size = width, height = Env_All['screenWidth'], Env_All['screenHeight']  # 设置窗口大小
    screen = pygame.display.set_mode(size)  # 显示窗口
    pygame.display.set_caption(u'打字游戏:反应练习')
    color = (255, 255, 255)  # 设置颜色
    # color = (0, 0, 0)  # 设置颜色
    screen.fill(color) 
    start = StartScene("标题", Env_All)
    game = GameScene("游戏内容", Env_All)
    over = OverScene("结束", Env_All)

    while True:  # 死循环确保窗口一直显示
        screen.fill(color)  # 填充颜色
        # 此处调用---场景.update(画的目标,比如屏幕)
        
        start.update(screen)
        game.update(screen)
        over.update(screen)

        # 场景调用======分割线

        for event in pygame.event.get():  # 遍历所有事件
            if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
                sys.exit()
            else:
                # 这里调用----场景名.event(event)
                start.event(event)
                game.event(event)
                over.event(event)
                # 场景事件=====分割线

        pygame.display.flip()  # 更新全部显示
        time_next = FPSClock.tick(FPS)
        Env_All['deltaTime'] = time_next / 1000  # 增量时间

    pygame.quit()  # 退出pygame
