from pico2d import*
import FlyScence

class Bonusobject:
    image=None
    def __init__(self, x):
        if Bonusobject.image==None:
            Bonusobject.image=load_image('yellowsprite.png')
        self.yx=x*200
        self.yy=600
        #global score 점수를 위해 만들어야함
        self.frame=0
        self.time=0
    def draw(self):
        self.image.clip_draw(self.frame*150,0,150,150,self.yx,self.yy)
    def update(self):
        self.time+=1
        if(self.time)>30:
            self.frame=(self.frame+1)%4
            self.time=0
        self.yy -=1
        if self.yy < -10:
            FlyScence.obstacleManager.obstacles.remove(self)
