from pico2d import*
import game_framework
import title_state
import random
import threading

score = 0
obsRed = None

class Back:  #배경그려주는 class
    def __init__(self):
        self.image=load_image('background.png')
        print(self.image)
    def draw(self):
         self.image.draw(400,0)

class Wizard: #마법사 class
    def __init__(self):
        global state, count
        global collapse, life, wx, wy
        print("Creating..")
        state = 2
        count = 0
        wx=400
        wy=90
        self.frame=0
        life = 3
        self.image=load_image('Wizard.png')

    def draw(self):
        global life, wx, wy
        self.image.clip_draw(self.frame*100,0,100,100,wx,wy)
        if(life == 3):
            LifeImage = load_image('LIFEx3.png')
        elif(life==2):
            LifeImage = load_image('LIFEx2.png')
        else:
            LifeImage = load_image('LIFEx1.png')
        LifeImage.draw_now(150,550)

    def update(self):
        global state, count, wx, wy, rx,ry,life
        self.frame=(self.frame + 1) % 8
        if state == 0: #왼쪽
            if count<200 and wx > 200:
                wx -= 20
                count += 20
            if count == 200:
                state = 2
        if state == 1: #오른쪽
            if count<200 and wx < 600:
                wx += 20
                count += 20
            if count == 200:
                state = 2
        if state == 2:
            count = 0
        if (wx>rx-5 and wx<rx+5 )and (wy>ry-50 and wy<ry)   :
            life-=1

        delay(0.05)
class Obstaclered:
    def __init__(self):
        print("Obstacles..")
        global rx
        global ry
        global life, collapse, weight
        weight=1
        self.frame = 0
        self.speed=5
        self.image=load_image('redsprite.png')
        rx=random.randint(1,3)*200
        ry=600
    def draw(self):
        self.image.clip_draw(self.frame*150,0,150,150,rx,ry)
    def update(self):
        global weight, ry
        self.frame=(self.frame+1) % 4
        ry-=self.speed*weight
        delay(0.01)

def handle_events(): #특수 버튼
    global wizards
    global state #방향 0왼 1오 2멈춤
    global move
    events=get_events()
    for e in events:
        if e.type == SDL_QUIT:
            game_framework.quit()
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                game_framework.pop_state()
            elif e.key == SDLK_LEFT:
                state = 0
            elif e.key == SDLK_RIGHT:
                state = 1

def enter():
    global wizards, backs, obsRed
    wizards = Wizard()
    backs=Back()
    obsRed=Obstaclered()

def draw():
    global backs, wizards, obsRed
    clear_canvas()
    backs.draw()
    wizards.draw()
    obsRed.draw()
    update_canvas()

def update():
    global wizards
    global obsRed
    obsRed.update()
    wizards.update()
#fill here
#def scoreTimer():
#    global score, scoretime
#    score=0
#    score+=1
#    scoretime = threading.Timer(1, scoreTimer)
#    scoretime.start()
    #scoretime.cancel() -> kill타이머

#def weightTimer():
#    global weight, weighttime
#    weight+=0.1
#    weighttime=threading.Timer(1, weightTimer)
#    weighttime.start()
#weightTimer()
def exit():
    pass

if __name__== '__main__':
    import sys
    current_module = sys.modules[__name__]
    open_canvas()
    game_framework.run(current_module)
    close_canvas()
