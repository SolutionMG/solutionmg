from pico2d import*
import ObstacleRed
import ObstacleBlue
import BonusObject
import random

# 0 empty
# 1 red
# 2 yellow
# 3 blue

pattern = [(0, 0, 0), (1, 0, 0), (2, 0, 0), (3, 0, 0), (0, 0, 1), (0, 0, 2), (0, 0, 3), (1, 1, 0), (2, 0, 2), (0, 3, 3)]
curPattern = None

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.oldCreatedTime = get_time()
        pass

    def update(self):
        if get_time() - self.oldCreatedTime > 3:
            self.oldCreatedTime = get_time()
            patternNum = random.randint(0, len(pattern) - 1)
            for i in range(0, 3):
                if pattern[patternNum][i] == 1:
                    self.obstacles.append(ObstacleRed.Obstaclered(i+1))
                elif pattern[patternNum][i] == 2:
                    self.obstacles.append(ObstacleBlue.Obstacleblue(i+1))
                elif pattern[patternNum][i] == 3:
                    self.obstacles.append(BonusObject.Bonusobject(i+1))
        for i in self.obstacles:
            i.update()
        pass

    def draw(self):
        for i in self.obstacles:
            i.draw()
        pass
