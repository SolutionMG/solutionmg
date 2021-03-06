from pico2d import*
import FlyScene
import ObstacleManager

class Bonusobject:
    image=None
    def __init__(self, x):
        if Bonusobject.image==None:
            Bonusobject.image=load_image('yellowsprite.png')
        self.yx=x*200
        self.yy=600
        self.frame=0
        self.time=0
        self.obstacles = ObstacleManager.ObstacleManager()
    def draw(self):
        self.image.clip_draw(self.frame*150,0,150,150,self.yx,self.yy)
    def update(self):
        if self.obstacles.Menu==0:
            self.time+=1
            if(self.time)>30:
                self.frame=(self.frame+1)%4
                self.time=0
            self.yy -=1
            if self.yy < -10:
                FlyScene.obstacleManager.obstacles.remove(self)
