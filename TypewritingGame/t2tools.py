import time
import pygame


class Console(object):
    """docstring for Console"""

    def __init__(self):
        super(Console, self).__init__()

    @staticmethod
    def log(string):
        print('Log:', time.asctime(time.localtime(time.time())),
              "*****" + string + "*****")

    @staticmethod
    def printEnv(env, string):
        print('Env_VAR:', string, "******" + env[string] + "*****")

    @staticmethod
    def getkeyCode(alphabt):
        code = {'A': 97,
                'B': 98,
                'C': 99,
                'D': 100,
                'E': 101,
                'F': 102,
                'G': 103,
                'H': 104,
                'I': 105,
                'J': 106,
                'K': 107,
                'L': 108,
                'M': 109,
                'N': 110,
                'O': 111,
                'P': 112,
                'Q': 113,
                'R': 114,
                'S': 115,
                'T': 116,
                'U': 117,
                'V': 118,
                'W': 119,
                'X': 120,
                'Y': 121,
                'Z': 122}
        return code[alphabt]

# 注意********
# 以下所有类,在一个场景中只能声明一次,可以管理场景里的所有元素
#**********


if __name__ == '__main__':
    # xx=Grid(800,600)
    # xx.cutTo(10,10)
    # print(xx.getPose(10,10))
    pass
