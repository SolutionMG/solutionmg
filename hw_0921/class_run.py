import random
from pico2d import *

def handle_events():
    global running
    global newX,newY
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type==SDL_MOUSEMOTION:
            newX,newY=event.x, 600-1-event.y        
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

class Grass:
    def __init__(self):
        self.image=load_image('grass.png')

    def draw(self):
        self.image.draw(400,30)
class Boy:
    def __init__(self):
        self.x = random.randint(0,200)
        self.y = random.randint(90,550)
        self.speed=random.uniform(1.0,4.0) #실수에 대한 랜덤값
        self.frame = random.randint(0,8)
        self.image = load_image('character_move.png')
        
    def update(self):
        self.frame = (self.frame + 1) % 8
        #self.x += self.speed
        if(self.x>newX):
            self.x-=self.speed
        elif(self.x<newX):
            self.x+=self.speed
        if(self.y>newY):
            self.y-=self.speed
        elif(self.y<newY):
            self.y+=self.speed

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
       
            

open_canvas() #무조건 오픈캔버스 먼저 하고 load_image 하기 

boys=[]
for i in range(20):
    boys+=[Boy()]

grass=Grass()
running=True

while running:
    handle_events()

    for b in boys:
        b.update()
    
    clear_canvas()
    grass.draw()
    
    for b in boys:
        b.draw()
         
    update_canvas()

    delay(0.05)

close_canvas()
