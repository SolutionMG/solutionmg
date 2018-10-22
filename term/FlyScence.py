from pico2d import*
import game_framework
import title_state
import random
import threading
import Back
import Wizard
import ObstacleRed

score = 0
obsRed = None

def handle_events(): #특수 버튼
    global wizards
    global move
    events=get_events()
    for e in events:
        if e.type == SDL_QUIT:
            game_framework.quit()
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                game_framework.pop_state()
            if e.key == SDLK_LEFT:
                wizards.state = 0
            if e.key == SDLK_RIGHT:
                wizards.state = 1


def enter():
    global wizards, backs, obsRed
    wizards = Wizard.Wizard()
    backs= Back.Back()
    obsRed=ObstacleRed.Obstaclered()

def draw():
    global backs, wizards, obsRed
    clear_canvas()
    backs.draw()
    wizards.draw()
    obsRed.draw()
    if (wizards.life == 3):
        LifeImage = load_image('LIFEx3.png')
        LifeImage.draw_now(150, 550)

    elif (wizards.life == 2):
        LifeImage = load_image('LIFEx2.png')
        LifeImage.draw_now(150, 550)

    elif(wizards.life==1):
        LifeImage = load_image('LIFEx1.png')
        LifeImage.draw_now(150, 550)
    else:
        pass
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
