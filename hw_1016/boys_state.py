from pico2d import *
import game_framework
import random
import title_state
import json

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
        print(self.image)
    def draw(self):
        self.image.draw(400, 30)

class Boy:
    image = None
    def __init__(self):
        print("Creating..")
        self.x = random.randint(0, 200)
        self.y = random.randint(90, 550)
        self.speed = random.uniform(1.0, 3.0)
        self.frame = random.randint(0, 7)
        self.state=3
        # 0 - 왼쪽으로 달리기 1 - 오른쪽으로 달리기 2 -왼쪽보며 서있기 3 - 오른쪽 보며 서있기
        if Boy.image==None:
            Boy.image=load_image('animation_sheet.png')
        self.waypoints = []
        self.wp = load_image('wp.png')
    def draw(self):
        for wp in self.waypoints:
             self.wp.draw(wp[0], wp[1])
        Boy.image.clip_draw(self.frame * 100, self.state*100, 100, 100, self.x, self.y)
    def update(self):
        self.frame = (self.frame + 1) % 8
        if len(self.waypoints) > 0:
            tx, ty = self.waypoints[0]
            dx, dy = tx - self.x, ty - self.y
            dist = math.sqrt(dx ** 2 + dy ** 2)
            if dist > 0:
                self.x += self.speed * dx / dist
                self.y += self.speed * dy / dist

                if dx < 0 and self.x < tx: self.x = tx
                if dx > 0 and self.x > tx: self.x = tx
                if dy < 0 and self.y < ty: self.y = ty
                if dy > 0 and self.y > ty: self.y = ty

                if (tx > self.x):
                    self.state = 1
                    if (tx == self.x):
                        self.state = 2
                elif (tx < self.x):
                    self.state = 0
                    if (tx == self.x):
                        self.state = 3

                if (tx, ty) == (self.x, self.y):
                    del self.waypoints[0]

span = 50
def handle_events():
    global boys
    global span
    events = get_events()
    for e in events:
         if e.type == SDL_QUIT:
            game_framework.quit()
         elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                #game_framework.quit()
                game_framework.run(title_state)
            elif e.key in range(SDLK_1, SDLK_9 + 1):
                span = 20 * (e.key - SDLK_0)

         elif e.type == SDL_MOUSEBUTTONDOWN:
             if e.button == SDL_BUTTON_LEFT:
                 tx, ty = e.x, 600 - e.y
                 for b in boys:
                     bx = tx + random.randint(-span, span)
                     by = ty + random.randint(-span, span)
                     b.waypoints += [(bx, by)]
             else:
                 for b in boys:
                     b.waypoints = []
                     b.state+=2

def enter():
    global boys, grass

    boys = []
    fh= open('boys_data.json')
    data=json.load(fh)
    for e in data['boys']:
        e['name']
        e['x']
        e['y']
        e['speed']
        b.speed=e['speed']
        boys.append(b)
    #boys=[Boy() for i in range(5)]
    grass = Grass()

  # def main():
#    global running
#    enter()
#    while running:
#       handle_events()
#       print(running)
#       update()
#       draw()
#  exit()

def draw():
    global grass, boys
    clear_canvas()
    grass.draw()
    for b in boys:
        b.draw()
    update_canvas()

def update():
    global boys
    for b in boys:
        b.update()
    delay(0.01)
 # fill here

def exit():
    close_canvas()

if __name__ == '__main__':
    main
