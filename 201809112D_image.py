from pico2d import *
open_canvas()
os.chdir('D:/')
os.listdir()
['$RECYCLE.BIN', '2D게임프로그래밍', 'Agario', 'Autodesk 3ds Max 2017 SP3 (x64) - Full', 'Autodesk 3ds Max 2017 SP3 (x64) - Full.rar', 'C&C++', 'eula.1042.txt', 'Git', 'GitDesktop', 'GOMPlayer', 'install.exe', 'install.ini', 'install.res.1042.dll', 'Maple', 'Nexonplay', 'Program Files', 'ProgramData', 'Steams', 'STOVE', 'System Volume Information', 'Unetsystem', 'vcredist.bmp', 'VC_RED.cab', 'VC_RED.MSI', 'WebLauncher', '그림', '비쥬얼 2017', '새 폴더', '새 폴더 (2)', '오버워칭!!!', '컴그']
os.chdir('2D게임프로그래밍')
os.listdir()
['2dgp-2018-2-744dbe5565df9ad3bea1fa9940b29aab4fc9d529', 'solutionmg']
os.chdir('2dgp-2018-2-744dbe5565df9ad3bea1fa9940b29aab4fc9d529')
os.listdir()
['.gitignore', 'pr0911_boy', 'pr0911_tree', 'testfile']
os.chdir('pr0911_boy')
os.listdir()
['character.png', 'character_grass.py', 'character_moves.py', 'grass.png']
image=load_image('character.png')
image.draw_now(300,200)
image.draw_now(300,400)
image.draw_now(100,100)
image.draw_now(300,400)
for x in range(0,9):
    for y in range(0,7):
    	image.draw_now(x*100,y*100)
clear_canvas_now()
grass=load_image('grass.png')
character=load_image('character.png')
grass.draw_now(400,30)
character.draw_now(400,90)
delay(5)
