from pico2d import *
import game_framework
import random
import title_state
import json
import boy

IDLE, RUN, SLEEP = range(3)
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, TIME_OUT = range(5)
key_event_table = { 
        (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
        (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
        (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
        (SDL_KEYUP, SDLK_LEFT): LEFT_UP
}

next_state_table = {
    IDLE: {RIGHT_UP: RUN, LEFT_UP: RUN, RIGHT_DOWN: RUN, LEFT_DOWN: RUN,
           TIME_OUT: SLEEP},
    RUN: {RIGHT_UP: IDLE, LEFT_UP: IDLE, LEFT_DOWN: IDLE, RIGHT_DOWN: IDLE},
    SLEEP: {LEFT_DOWN: RUN, RIGHT_DOWN: RUN}
}

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
    global grass
    global boys

    
    grass = Grass()
    way = [0, 0]
    
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
