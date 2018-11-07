from pico2d import *
import FlyScene
import BonusObject
import ObstacleRed
import ObstacleBlue
import Item
import random

# red = ObstacleRed.Obstaclered()

class Wizard:  # 마법사 class
    image = None

    def __init__(self):
        if Wizard.image == None:
            Wizard.image = load_image('Wizard.png')
        global collapse
        self.font = Font("정10.ttf", 50)
        self.scorefont = Font("정10.ttf", 30)
        self.state = 2
        self.count = 0
        self.wx = 400
        self.wy = 90
        self.frame = 0
        self.life = 3
        self.time = 0
        self.super = 0
        self.lifetime = 0
        self.lifecheck = False
        self.score = 0
        self.score2 = 0  # 축적 score
        self.scoretime = 0
        self.drawscore = False

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.wx, self.wy)
        self.font.draw(650, 550, str(int(get_time() * 10 + self.score2)) + "M", (255, 255, 0))
        if self.drawscore == True:
            self.scorefont.draw(650, 500, "+" + str(self.score), (255, 255, 0))

    def update(self):
        self.time += 1
        if self.time > 15:
            self.frame = (self.frame + 1) % 8
            self.time = 0

        if self.state == 0 and self.count == 0:  # super - 움직이는 동안 다른 키입력 무시
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

        for i in FlyScene.obstacleManager.obstacles:
            if type(i) == ObstacleRed.Obstaclered:
                if (self.wx > i.rx - 5 and self.wx < i.rx + 5) and (self.wy > i.ry - 50 and self.wy < i.ry + 50): #빨간 장애물 충돌체크
                    if self.lifecheck == False:
                        self.lifecheck = True
                        self.life -= 1
                    elif self.lifecheck == True:
                        pass
            if type(i) == ObstacleBlue.Obstacleblue:
                if (self.wx > i.bx - 5 and self.wx < i.bx + 5) and (self.wy > i.by - 50 and self.wy < i.by + 50): #파란 장애물 충돌체크
                    if (self.super == 1) or (self.super == 2):
                        if self.lifecheck == False:
                            self.lifecheck = True
                            self.life -= 1
                        elif self.lifecheck == True:
                            pass
            if type(i) == BonusObject.Bonusobject:
                if (self.wx > i.yx - 5 and self.wx < i.yx + 5) and (self.wy > i.yy - 50 and self.wy < i.yy + 50): # 보너스 오브젝트 충돌체크
                    self.drawscore = True
                    self.scoretime = 0
                    self.score = random.randint(2, 10)
                    self.score2 += self.score
                    FlyScene.obstacleManager.obstacles.remove(i)
            if type(i) == Item.ITEM:
                if (self.wx>i.ix - 5 and self.wx < i.ix + 5) and (self. wx > i.iy - 30 and self.wy < i.iy + 30):
                    if self. lifecheck == False:
                        self.lifecheck = True
                        if(self.life < 3):
                            self.life +=1
                        elif self.lifecheck == True:
                            pass
                        FlyScene.obstacleManager.obstacles.remove(i)
        if self.lifecheck == True: #충돌 후 잠시 무적
            self.lifetime += 1
            if (self.lifetime > 150):
                self.lifecheck = False
                self.lifetime = 0
        if self.drawscore == True:#충돌 후 점수 한번만 오르게
            self.scoretime += 1
            if (self.scoretime > 50):
                self.drawscore = False
                self.scoretime = 0
            # self.lifecheck=True

