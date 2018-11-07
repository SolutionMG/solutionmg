from pico2d import*
import FlyScene

class Obstaclered:
    image=None
    def __init__(self, x):
        if Obstaclered.image==None:
            Obstaclered.image=load_image('redsprite.png')
        self.rx=x*200
        self.ry=600
        self.frame = 0
        self.time=0
    def draw(self):
        self.image.clip_draw(self.frame*150,0,150,150,self.rx,self.ry)
    def update(self):
        self.time+=1
        if(self.time)>10:
            self.frame=(self.frame+1) % 4
            self.time=0

        self. ry -= 1
        if self.ry < -10:
            FlyScene.obstacleManager.obstacles.remove(self)
            # ry -= self.speed * weight
