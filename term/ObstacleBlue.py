from pico2d import *
import random

class Obstacleblue:
    image=None
    def __init__(self):
        if Obstacleblue.image==None:
            Obstacleblue.image=load_image('bluesprite.png')
        self.bx=random.randint(1,3)*200
        self.by=600
        global life, collapse
        self.frame=0
        self.speed=5
        self.time=0
    def draw(self):
        self.image.clip_draw(self.frame*150,0,150,150,self.bx,self.by)
    def update(self):
        self.time+=1
        if(self.time)>10:
            self.frame=(self.frame+1)%4
            self.time=0
        self.by -=1
        if self.by<-10:
            self.by=600
            self.bx=random.randint(1,3)*200