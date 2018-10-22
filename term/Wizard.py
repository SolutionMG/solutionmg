from pico2d import*
import FlyScence

# red = ObstacleRed.Obstaclered()



class Wizard: #마법사 class
    image=None

    def __init__(self):
        if Wizard.image==None:
            Wizard.image = load_image('Wizard.png')
        global collapse
        self.state = 2
        self.count = 0
        self.wx=400
        self.wy=90
        self.frame=0
        self.life = 3
        self.time = 0

    def draw(self):
        self.image.clip_draw(self.frame*100,0,100,100,self.wx,self.wy)


    def update(self):
        self.time += 1
        if self.time > 3:
            self.frame=(self.frame + 1) % 8
            if self.state == 0: #왼쪽
                self.wx -= 20
                self.count += 20
                if self.count >= 200:
                    self.state = 2
            elif self.state == 1: #오#른쪽
                self.wx += 20
                self.count += 20
                if self.count >= 200:
                    self.state = 2
            elif self.state == 2:
                self.count = 0
            self.time = 0

        if (self.wx>FlyScence.obsRed.rx-5 and self.wx<FlyScence.obsRed.rx+5 )and (self.wy>FlyScence.obsRed .ry-50 and self.wy<FlyScence.obsRed.ry)   :
            self.life-=1

