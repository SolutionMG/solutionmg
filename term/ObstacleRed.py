from pico2d import*
import random

class Obstaclered:
    image=None
    def __init__(self):
        if Obstaclered.image==None:
            Obstaclered.image=load_image('redsprite.png')
        self.rx=random.randint(1,3)*200
        self.ry=600
        global life, collapse
        self.frame = 0
        self.speed=5
        self.time=0
    def draw(self):
        self.image.clip_draw(self.frame*150,0,150,150,self.rx,self.ry)
    def update(self):
        self.time+=1
        if(self.time)>2:
            self.frame=(self.frame+1) % 4
            self. ry -= 1
            if self.ry < 0:
                self.ry = 600
                self.rx =random.randint(1,3)*200
            # ry -= self.speed * weight
            self.time=0
