from pico2d import*
import game_framework
import title_state
import random

class Back:  #배경그려주는 class
    def __init__(self):
        self.image=load_image('background.png')
        print(self.image)
    def draw(self):
         self.image.draw(400,0)

class Wizard: #마법사 class
    def __init__(self):
        print("Creating..")
        global state
        global count
        state = 2
        count = 0
        global wx,wy
        wx=400
        wy=90
        self.frame=0
        global collapse
        global life
        life = 3
        self.image=load_image('Wizard.png')
    def draw(self):
        self.image.clip_draw(self.frame*100,0,100,100,wx,wy)
        if(life == 3):
            LifeImage = load_image('LIFEx3.png')
        elif(life==2):
            LifeImage = load_image('LIFEx2.png')
        else:
            LifeImage = load_image('LIFEx1.png')
        LifeImage.draw_now(150,550)
    def update(self):
            self.frame=(self.frame + 1) % 8
            global state
            global count
            global wx
            if(state == 0): #왼쪽
                if(count<200 and wx > 200):
                    wx -= 20
                    count += 20
                if(count == 200):
                    state = 2
            if(state == 1): #오른쪽
                if(count<200 and wx < 600):
                    wx += 20
                    count += 20
                if(count == 200):
                    state = 2
            if(state == 2):
                count = 0
class Obstaclered:
    def __init__(self):
        print("Obstacles..")
        global life
        global collapse
        global redX
        global redY
        global speed
        speed = 5
        self.frame = 0
        redX=random.randint(1,3)*200
        redY=600
        self.image=load_image('redsprite.png')
    def draw(self):
        self.image.clip_draw(self.frame*150,0,150,150,redX,redY)
    def update(self):
        self.frame=(self.frame+1) % 4
        global redY
        if(redY>-150):
            redY-=speed
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
                game_framework.run(title_state)
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
    global backs, wizards,obsRed
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
    delay(0.1)
#fill here

def exit():
    close_canvas()

if __name__== '__Flymain__':
    main
