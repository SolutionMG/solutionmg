from pico2d import*
import ObstacleRed
import ObstacleBlue
import BonusObject
import Item
import random
import Wizard

# 0 empty
# 1 red
# 2 blue
# 3 yellow
# 4 item

pattern = [(1, 0, 0), (2, 0, 0), (3, 0, 0),
           (0, 1, 0), (0, 2, 0), (0, 3, 0),
           (0, 0, 1), (0, 0, 2), (0, 0, 3),
           (1, 1, 0), (1, 0, 1), (0, 1, 1), #확률 더 늘리려고 똑같은 패턴 반복
           (1, 1, 0), (1, 0, 1), (0, 1, 1),
           (2, 1, 1), (1, 1, 2), (1, 2, 1),
           (2, 1, 1), (1, 1, 2), (1, 2, 1),
           (2, 2, 1), (2, 1, 2), (1, 2, 2),
           (2, 2, 1), (2, 1, 2), (1, 2, 2),
           (2, 2, 3), (3, 2, 2), (2, 3, 2),
           (1, 2, 3), (1, 3, 2), (2, 1, 3),
           (1, 0, 0), (2, 0, 0), (3, 0, 0),
           (0, 1, 0), (0, 2, 0), (0, 3, 0),
           (0, 0, 1), (0, 0, 2), (0, 0, 3),
           (1, 1, 0), (1, 0, 1), (0, 1, 1), #확률 더 늘리려고 똑같은 패턴 반복
           (1, 1, 0), (1, 0, 1), (0, 1, 1),
           (2, 1, 1), (1, 1, 2), (1, 2, 1),
           (2, 1, 1), (1, 1, 2), (1, 2, 1),
           (2, 2, 1), (2, 1, 2), (1, 2, 2),
           (2, 2, 1), (2, 1, 2), (1, 2, 2),
           (2, 2, 3), (3, 2, 2), (2, 3, 2),
           (1, 2, 3), (1, 3, 2), (2, 1, 3),
           (4, 0, 0), (0, 4, 0), (0, 0, 4),
           (4, 0, 0), (0, 4, 0), (0, 0, 4),
           (2, 3, 1), (3, 1, 2), (3, 2, 1),
           (2, 3, 1), (3, 1, 2), (3, 2, 1)] #패턴 조절하기
curPattern = None

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.oldCreatedTime = get_time()
        self.Downspeed=2
        self.Now=0
        self.level=0
        self.Menu=0
        self.wizard=Wizard.Wizard()
        pass

    def update(self):
        if self.wizard.life >0:
            if self.Downspeed>1.2:
                self.level+=1
            if self.level>600:
                self.Downspeed -= 0.1
                self.level=0
            if self.Downspeed>0:
                if get_time() - self.oldCreatedTime > self.Downspeed:
                    self.oldCreatedTime = get_time()
                    patternNum = random.randint(0, len(pattern) - 1)
                    for i in range(0, 3):
                        if pattern[patternNum][i] == 1:
                            self.obstacles.append(ObstacleRed.Obstaclered(i+1))
                        elif pattern[patternNum][i] == 2:
                            self.obstacles.append(ObstacleBlue.Obstacleblue(i+1))
                        elif pattern[patternNum][i] == 3:
                            self.obstacles.append(BonusObject.Bonusobject(i+1))
                        elif pattern[patternNum][i] == 4:
                            self.obstacles.append(Item.ITEM(i+1))
                for i in self.obstacles:
                    i.update()
                pass

    def draw(self):
        if self.wizard.life > 0 and self.Downspeed>0:
            for i in self.obstacles:
                i.draw()
        pass
