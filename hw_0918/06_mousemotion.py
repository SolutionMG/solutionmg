from pico2d import *
import math
open_canvas()
x, y=0, 90
newX, newY=x,y
frame=0
speed=5
KPU_WIDTH,KPU_HEIGHT=800,600
def handle_events():
    global running
    global x,y
    global newX, newY
    events=get_events()
    for event in events:
        if event.type==SDL_QUIT:
            running=False
        elif event.type==SDL_MOUSEMOTION:
            newX, newY=event.x, KPU_HEIGHT-1-event.y
        elif event.type==SDL_KEYDOWN and event.key==SDLK_ESCAPE:
            running=False

open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground=load_image('grass.png')
character=load_image('character_move.png')

running=True
x,y=KPU_WIDTH//2,KPU_HEIGHT//2

while running:
    clear_canvas()
    kpu_ground.draw(400,30)
    character.clip_draw(frame*100,0,100,100,x,y)
    update_canvas()
    frame=(frame+1)%8
    if(x>newX):
        x-=speed
    elif(x<newX):
        x+=speed
    if(y>newY):
        y-=speed
    elif(y<newY):
        y+=speed
    delay(0.01)
    handle_events()
close_canvas()
