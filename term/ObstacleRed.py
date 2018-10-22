from pico2d import*
import random

class Obstaclered:
    image=None
    def __init__(self):
        if Obstaclered.image==None:
            self.image=load_image('redsprite.png')
        global rx
        global ry
        global life, collapse, weight
        weight=1
        self.frame = 0
        self.speed=5
        rx=random.randint(1,3)*200
        ry=600
    def draw(self):
        self.image.clip_draw(self.frame*150,0,150,150,rx,ry)
    def update(self):
        global weight, ry
        self.frame=(self.frame+1) % 4
        ry-=self.speed*weight
        delay(0.01)
