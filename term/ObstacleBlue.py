from pico2d import *
import FlyScence

class Obstacleblue:
    image=None
    def __init__(self, x):
        if Obstacleblue.image==None:
            Obstacleblue.image=load_image('bluesprite.png')
        self.bx=x*200
        self.by=600
        global life
        self.frame=0
        self.time=0
    def draw(self):
        self.image.clip_draw(self.frame*150,0,150,150,self.bx,self.by)
    def update(self):
        self.time+=1
        if(self.time)>20:
            self.frame=(self.frame+1)%4
            self.time=0
        self.by -=1
        if self.by<-10:
            FlyScence.obstacleManager.obstacles.remove(self)