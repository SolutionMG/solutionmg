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
        self.super= 0
        self.lifetime=0
        self.lifecheck=False

    def draw(self):
        self.image.clip_draw(self.frame*100,0,100,100,self.wx,self.wy)


    def update(self):
        self.time += 1
        if self.time > 15:
            self.frame=(self.frame + 1) % 8
            self.time = 0

        if self.state == 0 and self.count == 0: #super - 움직이는 동안 다른 키입력 무시
            self.super = 1
        elif self.state == 1 and self.count == 0:
            self.super = 2

        if self.state == 0 and self.super == 1 and self.wx > 200:  # 왼쪽
            self.wx -= 4
            self.count += 4
            if self.count >= 200 or self.wx <= 200:
                self.super = 3
                self.state = 2
        elif self.state == 1 and self.super == 2 and self.wx < 600:  # 오른쪽
            self.wx += 4
            self.count += 4
            if self.count >= 200 or self.wx >= 600:
                self.state = 2
                self.super = 3
        elif self.state == 2:
            self.count = 0
            self.super = 3

        if (self.wx>FlyScence.obsRed.rx-5 and self.wx<FlyScence.obsRed.rx+5 )and (self.wy>FlyScence.obsRed .ry-50 and self.wy<FlyScence.obsRed.ry+50):
            if self.lifecheck == False:
                self.lifecheck = True
                self.life -= 1
            elif self.lifecheck == True:
                pass
        if(self.wx>FlyScence.obsBlue.bx-5 and self.wx<FlyScence.obsBlue.bx+5)and (self.wy>FlyScence.obsBlue.by-50 and self.wy<FlyScence.obsBlue.by+50):
            if (self.super==1) or (self.super==2):
                if self.lifecheck == False:
                    self.lifecheck=True
                    self.life -=1
                elif self.lifecheck == True:
                    pass

        if self.lifecheck == True:
            self.lifetime += 1
            if(self.lifetime > 150):
                self.lifecheck=False
                self.lifetime = 0

            # self.lifecheck=True

