from pico2d import *
import random
import FlyScene

class ITEM:
    image =None
    def __init__(self,x):
        if ITEM.image == None:
            ITEM.image=load_image('cure.png')
        self.ix=x*200
        self.iy=600
        self.time=0
        self.time2=0
    def draw(self):
        self.image.draw(self.ix,self.iy)
    def update(self):
      self.iy -= 1
      if self.iy < -10:
          FlyScene.obstacleManager.obstacles.remove(self)
