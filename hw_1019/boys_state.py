from pico2d import *
from Boy import Boy
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
                game_framework.quit()
                #game_framework.run(title_state)
         if e.type == SDL_KEYDOWN and e.key == SDLK_LEFT:
            boy.velocity = -1
            boy.change_state(1)
         elif e.type == SDL_KEYDOWN and e.key ==SDLK_RIGHT:
            boy.velocity = 1
            boy.change_state(1)
         elif e.type == SDL_KEYUP and e.key== SDLK_LEFT:
            boy.velocity = 0
            boy.change_state(0)
         elif e.type == SDL_KEYUP and e.key==SDLK_RIGHT:
             boy.velocity = 0
             boy.change_state(0)
def enter():
    global grass
    global boy

    grass = Grass()
    boy=Boy()
def draw():
    global grass, boy
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()

def update():
    global boy
    boy.update()
    delay(0.01)
 # fill here

def exit():
    close_canvas()

if __name__ == '__main__':
    main
