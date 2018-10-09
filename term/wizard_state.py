from pico2d import*
import game_framework
import title_state

dir= 0  # 0 가운데 -1 왼쪽 1 오른쪽

class Back:  #배경그려주는 class
    def __init__(self):
        self.image=load_image('background.png')
        print(self.image)
    def draw(self):
         self.image.draw(400,0)

class Wizard: #마법사 class
    def __init__(self):
        print("Creating..")
        self.x=400
        self.y=90
        self.frame=0
        self.image=load_image('Wizard.png')
    def draw(self):
        self.image.clip_draw(self.frame*100,0,100,100,self.x,self.y)
    def update(self):
            self.frame=(self.frame+1)&8
            self.x=self.x+dir

def handle_events(): #특수 버튼
    global wizards, dir
    events=get_events()
    for e in events:
        if e.type == SDL_QUIT:
            game_framework.quit()
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                game_framework.run(title_state)
            elif e.key == SDLK_LEFT:
                if(dir>-100):
                    dir=dir-1
                    delay(0.01)
            elif e.key == SDLK_RIGHT:
                if(dir<100):
                    dir=dir+1
                    delay(0.01)
def enter():
    global wizards, backs
    wizards = [Wizard() for i in range(1)]
    backs=Back()

def draw():
    global backs, wizards
    clear_canvas()
    backs.draw()
    for w in wizards:
        w.draw()
    update_canvas()

def update():
    global wizards
    for w in wizards:
        w.update()
    delay(0.1)
#fill here

def exit():
    close_canvas()

if __name__== '__Flymain__':
    main
