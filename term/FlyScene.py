from pico2d import*
import game_framework
import title_state
import random
import threading
import Back
import Wizard
import ObstacleManager
score = 0
obstacleManager = None
MenuState=0 # 0- Menu바 안불러옴 1-아무것도 안누르고 안댄 상태 2- 위에 댄상태 3- 아래 댄상태
def handle_events(): #특수 버튼
    global wizards
    global move,MenuState
    global obstacleManager
    events=get_events()
    for e in events:
        if e.type == SDL_QUIT:
            game_framework.quit()
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                MenuState=1
                obstacleManager.Now=obstacleManager.Downspeed
                obstacleManager.Downspeed=0
                wizards.plustime=0

            if (wizards.count == 0):
                if e.key == SDLK_LEFT:
                    wizards.state = 0
                if e.key == SDLK_RIGHT:
                    wizards.state = 1
        if MenuState>0:
             if e.type == SDL_MOUSEMOTION:
                if e.x > 400 - 100 and e.x < 400 + 100 and 600 - e.y > 150 - 50 and 600 - e.y < 150 + 50: #Back
                    MenuState = 3
                elif e.x > 400 - 100 and e.x < 400 + 100 and 600 - e.y > 300 - 50 and 600 - e.y < 300 + 50:#Exit
                    MenuState = 2
                else:
                    MenuState = 1

        if e.type == SDL_MOUSEBUTTONDOWN and MenuState == 3:
                MenuState = 0
                obstacleManager.Downspeed = obstacleManager.Now
        if e.type == SDL_MOUSEBUTTONDOWN and MenuState == 2:
                MenuState = 0
                game_framework.pop_state()

def enter():
    global wizards, backs, obstacleManager, bonus
    wizards = Wizard.Wizard()
    backs= Back.Back()
    obstacleManager = ObstacleManager.ObstacleManager()
def draw():
    global backs, wizards, obstacleManager,MenuState
    clear_canvas()
    backs.draw()
    wizards.draw()
    obstacleManager.draw()

    if (wizards.life == 3):
        LifeImage = load_image('LIFEx3.png')
        LifeImage.draw(150, 550)

    elif (wizards.life == 2):
        LifeImage = load_image('LIFEx2.png')
        LifeImage.draw(150, 550)

    elif(wizards.life==1):
        LifeImage = load_image('LIFEx1.png')
        LifeImage.draw(150, 550)
    elif(wizards.life==0):
        LifeImage=load_image('LIFEx0.png')
        LifeImage.dtaw(150,550)
    else:
        pass
    if (MenuState == 1):  # 아무것도 안눌림
        Menu = load_image('Menu.png')
        Menu.draw(400, 270)
        Exit_Button = load_image('Exit1.png')
        Exit_Button.draw(400, 300 )
        Back_Button = load_image('Back1.png')
        Back_Button.draw(400, 150)
        obstacleManager.Downspeed = 0
        wizards.plustime = 0
    elif (MenuState == 2):  # Exit눌림
        Menu = load_image('Menu.png')
        Menu.draw(400, 270)
        Exit_Button = load_image('Exit2.png')
        Exit_Button.draw(400, 300)
        Back_Button = load_image('Back1.png')
        Back_Button.draw(400, 150)
        obstacleManager.Downspeed = 0
        wizards.plustime = 0

    elif (MenuState == 3):  # Back 눌림
        Menu = load_image('Menu.png')
        Menu.draw(400, 270)
        Exit_Button = load_image('Exit1.png')
        Exit_Button.draw(400, 300)
        Back_Button = load_image('Back2.png')
        Back_Button.draw(400, 150)
        obstacleManager.Downspeed = 0
        wizards.plustime = 0

    update_canvas()

def update():
    global wizards, obstacleManager
    wizards.update()
    obstacleManager.update()

#fill here
#def scoreTimer():
#    global score, scoretime
#    score=0
#    score+=1
#    scoretime = threading.Timer(1, scoreTimer)
#    scoretime.start()
    #scoretime.cancel() -> kill타이머

def exit():
    pass

if __name__== '__main__':
    import sys
    current_module = sys.modules[__name__]
    open_canvas()
    game_framework.run(current_module)
    close_canvas()
