from pico2d import*

class Back:  #배경그려주는 class
    image = None
    def __init__(self):
        if Back.image == None:
            Back.image=load_image('background.png')
        print(self.image)
    def draw(self):
         self.image.draw(400,0)
