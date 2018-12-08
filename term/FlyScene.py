from pico2d import*
import game_framework
import title_state
import random
import threading
import Back
import Wizard
import ObstacleManager

obstacleManager = None
MenuState=0 # 0- Menu바 안불러옴 1-아무것도 안누르고 안댄 상태 2- 위에 댄상태 3- 아래 댄상태
time_menu_entered = None
def handle_events(): #특수 버튼
    global wizard
    global move,MenuState,gamestate
    global obstacleManager
    global time_menu_entered
    events=get_events()
    for e in events:
        if e.type == SDL_QUIT:
            game_framework.quit()
        elif e.type == SDL_KEYDOWN:
            if gamestate==1 and e.key == SDLK_ESCAPE: #게임이 끝났을 때
                game_framework.pop_state()
            if gamestate==0 and e.key == SDLK_ESCAPE: #게임 중일 때 -> Menu불러옴
                MenuState=1
                time_menu_entered = get_time()



            if (wizard.count == 0):
                if e.key == SDLK_LEFT:
                    wizard.state = 0
                if e.key == SDLK_RIGHT:
                    wizard.state = 1
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
                obstacleManager.oldCreatedTime += get_time() - time_menu_entered
        if e.type == SDL_MOUSEBUTTONDOWN and MenuState == 2:
                MenuState = 0
                game_framework.pop_state()

def enter():
    global wizard, backs, obstacleManager, bonus, back_bgm2
    wizard = Wizard.Wizard()
    backs= Back.Back()
    obstacleManager = ObstacleManager.ObstacleManager()
    back_bgm2=load_music('start.mp3')
    back_bgm2.set_volume(64)
    back_bgm2.repeat_play()

def draw():
    global backs, wizard, obstacleManager,MenuState,gamestate
    font = Font("정10.ttf", 40)
    clear_canvas()
    backs.draw()
    wizard.draw()
    obstacleManager.draw()

    if (wizard.life == 3):
        LifeImage = load_image('Lifex3.png')
        LifeImage.draw(150, 550)
        gamestate=0
    elif (wizard.life == 2):
        LifeImage = load_image('Lifex2.png')
        LifeImage.draw(150, 550)
        gamestate=0
    elif(wizard.life==1):
        LifeImage = load_image('Lifex1.png')
        LifeImage.draw(150, 550)
        gamestate=0
    elif(wizard.life==0):
        #LifeImage = load_image('Lifex0.png')
        #LifeImage.dtaw(150,550)
        gameover = load_image('gameover.png')
        gameover.draw(400,300)
        font.draw(300,300,"Score: " + str( (int)(wizard.plus + wizard.score2)) + "M", (255, 255, 0))
        gamestate=1

    if (MenuState == 1):  # 아무것도 안눌림
        Menu = load_image('Menu.png')
        Menu.draw(400, 270)
        Exit_Button = load_image('Exit1.png')
        Exit_Button.draw(400, 300 )
        Back_Button = load_image('Back1.png')
        Back_Button.draw(400, 150)

    elif (MenuState == 2):  # Exit눌림
        Menu = load_image('Menu.png')
        Menu.draw(400, 270)
        Exit_Button = load_image('Exit2.png')
        Exit_Button.draw(400, 300)
        Back_Button = load_image('Back1.png')
        Back_Button.draw(400, 150)

    elif (MenuState == 3):  # Back 눌림
        Menu = load_image('Menu.png')
        Menu.draw(400, 270)
        Exit_Button = load_image('Exit1.png')
        Exit_Button.draw(400, 300)
        Back_Button = load_image('Back2.png')
        Back_Button.draw(400, 150)

    update_canvas()

def update():
    global wizard, obstacleManager, MenuState
    if MenuState == 0:
        wizard.update()
        obstacleManager.update()

def exit():
    pass

if __name__== '__main__':
    import sys
    current_module = sys.modules[__name__]
    open_canvas()
    game_framework.run(current_module)
    close_canvas()
