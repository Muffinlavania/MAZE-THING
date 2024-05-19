oooG=False
import os,time,sys,random,json
from threading import Thread
import threading,ctypes

WINDOWS = os.name=='nt'
if WINDOWS:
  import msvcrt

  #WALRUS OPERATOR OP 
  somekeys = {'H': 'up', 'P': 'down', 'K': 'left', 'M': 'right', '\\r': 'enter', '\\x08': 'backspace','\\xe0':'yippe yay','\\t':'tab'}
else:
  from getkey import keys
  from getkey import getkey as GETkey

GTIME = time.time()
def C(f = ''):
  global GTIME
  os.system('clear' if os.name!='nt' else 'cls')
def UPME():
  global GTIME
  if time.time()-GTIME > .03:
    GTIME = time.time()
    C()
    printmaze(mazeq)
c = C
def getkey():
  return (h if (h:=str(msvcrt.getch())[2:-1]) not in somekeys.keys() or h in ['P','H','K','M'] else somekeys[h] if h!='\\xe0' else somekeys[str(msvcrt.getch())[2:-1]]) if WINDOWS else GETkey()
UP='up' if WINDOWS else keys.UP
DOWN='down' if WINDOWS else keys.DOWN
RIGHT='right' if WINDOWS else keys.RIGHT
LEFT='left' if WINDOWS else keys.LEFT
BACKSPACE='backspace' if WINDOWS else keys.BACKSPACE
ENTER='enter' if WINDOWS else keys.ENTER
TAB='tab' if WINDOWS else keys.TAB

print('\033[?25l')
name=input("hey who are you?\n> ")
C('clear')
if name=='five-nine':
  name='Joe'
try:
  with open(name+'.json','r'):
    pass
except:
  with open(name+'.json','w') as h:
    h.write('[1,0]')
try:
  with open(name+'2.json','r'):
    pass
except:
  with open(name+'2.json','w') as h:
    h.write('')
    
def load2():
  with open(name+'.json') as h:
    pass
def save(fileath, thething=True):
  with open(fileath, "w") as f:
    f.write(json.dumps(thething))
def load(filePpath,k=True):
  with open(filePpath, "r") as f:
    if k:
      return json.loads(f.read())[0]
    else:
      return json.loads(f.read())[1]

secr=load(name+'.json',False)


#SETUP.py


red2 = "\033[38;5;124m"
orange2 = "\033[38;5;166m"
yellow2 = "\033[38;5;226m" 
green2 = "\033[38;5;34m"
blue2 = "\033[38;5;21m" 
purple2 = "\033[38;5;57m" 

black = "\033[48;5;232m" 
red = "\033[48;5;124m" 
orange = "\033[48;5;166m" 
green = "\033[48;5;34m" 
yellow = "\033[48;5;226m" 
blue = "\033[48;5;21m" 
purple = "\033[48;5;57m" 
cyan = "\033[48;5;87m" 
bright_black = "\033[48;5;240m" 
bright_red = "\033[48;5;196m" 
bright_green = "\033[48;5;118m" 
bright_yellow = "\033[48;5;228m" 
bright_blue = "\033[48;5;45m" 
bright_magenta = "\033[48;5;92m" 
bright_cyan = "\033[48;5;123m" 
bright_white = "\033[48;5;254m"
bold='\033[01m'
reset='\033[0m'
import json
try:
  with open(name+'.json', "r") as f:
    p=json.loads(f.read())
except:
  p=[1,0]
#First objective: get working achievments in this game at least lol
#SOme ideas: Secret Hunter (Get all secrets), ULTRA Secret Hunter (Get the useless secret), Die (die in every level),
achi='''
┌──────────────────────────────────────┐
|             Achievements             |
|             ------------             |
|                                      |
|            Secret Hunting            |
|            [Find every Y]            |
|                  !!                  |
|                                      |
|             Useless Pog              |
|       [Find the useless secret]      |
|                  @@                  |
|                                      |
|                \e die                |
|     [Die in every level possible]    |
|                  ##                  |
|                                      |
|                wwwwwww               |
|      [Collect 1.5k Ws in one run]    |
|                  $$                  |
└──────────────────────────────────────┘
'''
if secr==0:
  astr='''
    ┌───────────────────────────────────────────────────────────────┐
    │                         '''+bold+'''Controls:'''+reset+'''                             │
    │        --------------------------------------------           │
    │          WASD/Arrow Keys to move your character               │
    │     Stuck? Press 'H' when playing the mazes to get a hint!    │ 
    │       Screen got messed up? Reset the screen with 'C'!        │
    │                    End your game with 'Z'                     │ 
    │        --------------------------------------------           │
    │    Hit 'L' rn if you have a save file you want to load!       │
    │      Hit 'C' rn if you want to customize your maze!           │ 
    │        --------------------------------------------           │
    │     (If the maze is too big for your screen zoom out)         │
    │                                                               │
    │                     [Any Key to Continue]                     │
    │                                                               │
    └───────────────────────────────────────────────────────────────┘
  '''
else:
  astr='''
    ┌───────────────────────────────────────────────────────────────┐
    │                         '''+bold+'''Controls:'''+reset+'''                             │
    │        --------------------------------------------           │
    │          WASD/Arrow Keys to move your character               │
    │     Stuck? Press 'H' when playing the mazes to get a hint!    │ 
    │       Screen got messed up? Reset the screen with 'C'!        │
    │                 Restart the level with 'R'!                   │ 
    │        --------------------------------------------           │
    │     Hit 'L' if you have a save file you want to load!         │ 
    │     (Z to toggle saving, to save must fork this project)      │
    │        Hit 'C' if you want to customize your maze!            │ 
    │        --------------------------------------------           │
    │     (If the maze is too big for your screen zoom out)         │
    │              '''+red2+'''Press'''+orange2+''' Q '''+yellow2+'''To'''+green2+''' Enable '''+blue2+'''Rainbow '''+purple2+'''Mode!'''+reset+'''                  │
    │                     [Any Key to Continue]                     │
    │                                                               │
    │                                                               │
    └───────────────────────────────────────────────────────────────┘
  '''
'''
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|X----------------------------------------------T-X+
|X------------------------------------------------X+
|X------------------------------------------------X+
|X------------------------------------------------X+
|X------------------------------------------------X+
|X------------------------------------------------X+
|X------------------------------------------------X+
|X------------------------------------------------X+
|X------------------------------------------------X+
|X------------------------------------------------X+
|X------------------------------------------------X+
|X------------------------------------------------X+
|X------------------------------------------------X+
|X------------------------------------------------X+
|X------------------------------------------------X+
|X------------------------------------------------X+
|X-┌┐---------------------------------------------X+
|X-└┘---------------------------------------------X+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
'''
mazeo1='''
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|X---------------------------SSSS---SSSSSSSS--4Y--X+
|X------XXXXX----------------------------------4--X+
|X------3D333----------------SSSSSS---SSSSSS---444X+
|X------3333UUUUUUUXUWUXWU------------------SSSS--X+
|X---UUUU-------------------------SSSSSSS---------X+
|X---WWWW---------XXX------------------------SSSS-X+
|XSSSXXXXS---S-----------XXXXXX-------------------X+
|X---WWWW------XXXXXX-------------SSSSSSS---------X+
|X-------------SSSSSS-----------------------------X+
|X222-----XXXX--------UXWUXUWXUUWXUUXWUUW---------X+
|X--2---SSSS--------------------------SSSSSS------X+
|XA-2----------SSSSSS-----------------------------X+
|XXXXUUU---XXXXX--33333333--------XXXX------------X+
|XUUU-------------3B3-------XXX--------SSSSSSSSSSSX+
|XUUU-----------C-33-------------SSSSSSSSSSSSSSSSSX+
|XUUU-111-----X---3XXX----X------------SSSSSSSSSSSX+
|X-┌┐-1--1SSSSX---3---------------------SSSSSSSSSSX+
|X-└┘-1-T1----X---3---------XXX-------------SSSSSSX+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
'''
maze1='''
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|X----------------------------------------------T-X+
|X------------------------------------------------X+
|X------------------------------------------------X+
|X------------------------------------------------X+
|X------------------------------------------------X+
|X------------------------------------------------X+
|X------------------------------------------------X+
|X------------------------------------------------X+
|X------------------------------------------------X+
|X------------------------------------------------X+
|X------------------------------------------------X+
|X------------------------------------------------X+
|X------------------------------------------------X+
|X------------------------------------------------X+
|X------------------------------------------------X+
|X------------------------------------------------Y+
|X-┌┐---------------------------------------------X+
|X-└┘---------------------------------------------X+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
'''
maze2='''
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--------T-X+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX----------X+
|X------------------------------------------------X+
|X------------------------------------------------X+
|X--------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX----X+
|X--------------YXXXXXXXXXXXXXXXXXXXXXXXXXXXXX----X+
|X------------------------------------------------X+
|X------------------------------------------------X+
|X--------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|X--------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|X------------------------------------------------X+
|X------------------------------------------------X+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--------------X+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--------------X+
|X------------------------------------------------X+
|X------------------------------------------------X+
|X┌┐------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|X└┘------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
'''
maze3='''
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|X------------XXXX------------------------------T-X+
|X------------XXXX--------------------------------X+
|X------------YXXX------------------XXXXXXXXXXXXXXX+
|X------------XXXX------------------XXXXXXXXXXXXXXX+
|XXXXXXX----------------------------XXXX----------X+
|XXXXXXX----------------------------XXXX----------X+
|XXXXXXX----------------------------XXXX------XXXXX+
|XXXXXXXXXXXXXXXXXXX--------------------------XXXXX+
|XXXXXXXXXXXXXXXXXXX--------------------------XXXXX+
|XXXXXXXXXXXXXXXXXXXXX----------------------------X+
|XXXXXXXXXXXXXXXXXXXXX----------------------------X+
|XXXXXXXXXXXXXXXXXXXXXXXXXXX-----------XX---------X+
|XXXXXXXXXXXXXXXXXXXXXXXXXXX-----------XX---------X+
|XXXXXXXXXXXXXXXXXXXXXXXXXXX-----------XX---------X+
|XXXXXXXXXXXXXXXXXXXXXXXXXXX-----------XX---------X+
|X┌┐-----------------------------------XX---------X+
|X└┘-----------------------------------XX---------X+
|X-------------------------------------XX---------X+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
'''
maze4='''
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|X----------------------------------------------T-X+
|X------------------------------------------------X+
|XXXXXXXXXXXXXXXXX------XXXXXXXXXXXXXXXXXXXXXXXXXXX+
|XXXXXXX------------------------------------------X+
|XXXXXXX------------------------------------------X+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX---X+
|XXXXXXXXXXXXX--------------------XXXXXXXXXXXXX---X+
|XXXXXXXXXXXXX-------------------XXXXXXXXXXXXXX---X+
|XXXXXXXXX-----------------------------------XX---X+
|XXXXXXXXX-----------------------------------XX---X+
|XXXXXXXXX----XXXX---------------------------XX---X+
|XXXXXXXXX----YXXX------------------XXXX----------X+
|XXXXXXXXX----XXXX------XXXXXXXXXXXXXXXX----------X+
|XXXXXXXXX----XXXX------XXXXXXXXXXXXXXXX----------X+
|XXXXXXXXX----XXXX------XXXXXXXXXXXXXXXX----------X+
|X┌┐----------------------------------------------X+
|X└┘----------------------------------------------X+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
'''
maze5='''
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|X------------------------------XX--------------T-X+
|X------------------------------XX----------------X+
|XXXXXX----XX----XXXXXXXXXXXXXXXXXXX---XXXXXXXXXXXX+
|XXXXXX----XX----XXXXXXXXXXXX----------XXXXXXXXXXXX+
|XXXXXX----XX----XXXXXXXXXXXX----------XXXXXXXXXXXX+
|XXXXXX----XX----XXXXXXXXXXXX---XXXXX--XXXXXX--XXXX+
|XXXXXX----XX----XXXXXXXXXXXX---XXXXX--XXXXXX--XXXX+
|XXXXXX----XXXXXXXXXXXXXXXXXX---XXXXX--XXXXXX--XXXX+
|XXXXXX-------------------------XXXXX----------XXXX+
|XXXXXX-------------------------XXXXX----------XXXX+
|XXXXXX---------XXXXXXXXXXXXXXXXXXXXXXXXXXXXX--XXXX+
|XXXXXX---------------X------------XXXXXXXX----XXXX+
|XXXXXX---------------X------------YXXXXXXX----XXXX+
|XXXXXX---------------XXXXXXXXXXX--XXXXXXXXXX--XXXX+
|XXXXXXXXXXXXXXXX-----XXXXXXXXXXX--XXXXXXXXXX--XXXX+
|XXXXXXXXXXXXXXXX-----XXXXXXXXXXX--XXXXXXXXXX--XXXX+
|X-┌┐---------------------------------------------X+
|X-└┘---------------------------------------------X+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
'''
maze6='''
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|XX----------------------------XXXXXX-----------T-X+
|XX----------------------------XXXXXX-------------X+
|XXXXXXXXXX----XXXXXXXXXX---XX-X---XX----XXXXXXXXXX+
|XXXXXXXXXX----XXXXXXXXXX---XX-X---XX----XXXXXXXXXX+
|XX-----XXX----XXXXXXXXXX---XX-X--------------XXXXX+
|XX-----XXX----XXXXXXXXXX---XX-X-------------XXXXXX+
|XX------------------XXXX------XXXXXXX---------XXXX+
|XX------------------XXXX------XXXXXXX---------XXXX+
|XXXXXXXXXX--------------XXXX------------------XXXX+
|XXXXXXXXXX--------------XXXX------------XXXXXXXXXX+
|XXXXXXXXXX----------X---XXXX--XXXXXXX---XXXXXXXXXX+
|X-------XX----------X---XXXX----XXXXX---XXXXXXXXXX+
|X-------XX----------X---XXXX----XXXXX---------XXXX+
|XXXX----XX------XXXXX---XXXXXX--XXXXX---------XXXX+
|XXXX----XX------YXXXX---XXXXXX-----XXXXXXXXXXXXXXX+
|XXXX----XX------XXXXX---XXXXXX-----XXXXXXXXXXXXXXX+
|X-┌┐---------------------------------------------X+
|X-└┘---------------------------------------------X+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
'''
maze7='''
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|X------------------XX----------------------XX--T-X+
|X------------------XX----------------------XX----X+
|XXXXXXXX---XXXX---XXXXXXXX---XXXXXXXXXXX---XX----X+
|XXXXXXXX---XXXX---------XX---XXXXXXXXXXX---XX----X+
|XXX--------XXXX---------XX---XXXXXXXXXXX---XX----X+
|XXX--------XXXX---------XX-------XXXXXXX---------X+
|XXX---XXXXXXXXX---YXXXXXXX-------XXXXXXX---------X+
|XXX---XXXXXXXXX---XXXXXXXX---XXXXXXXXXXXXXXXXXXXXX+
|XXX---XXXXXXXXX--------XXX---XXXXXXX-------------X+
|XXX--------------------XXX---XXXXXXX-------------X+
|XXX-------------------XXXX---XXXXXXX----XXXXXX---X+
|XXXXXXXXX---XXXXXXX---XXXX--------------XXXXXX---X+
|XXXXXXXXX---XXXXXXX---XXXX--------------XXXXXX---X+
|XXXXXXXXX-------------XXXX---XXXXXXX----XXXXXX---X+
|XXXXXXXXX-------------XXXXXXXXXXXXXX----XXXXXX---X+
|XXXXXXXXX---XXXXXXXXXXXXXXXXXXXXXXXX----XXXXXX---X+
|X-┌┐---------------------------------------------X+
|X-└┘---------------------------------------------X+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
'''
maze8='''
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|XXXX--------------------------------------XXXXXXXX+
|XXXX--------------------------------------XXXXXXXX+
|XXXX---XXXXXXX---XXXXXXXXXXXXXXXXXXXXXX---XXXXXXXX+
|XXXX---XXXXXXX---XXXXXXXXXXXXXXXXXXXXXX---XXXXXXXX+
|XXXX---XXXXXXX---XXXXXXXXXXXXXXXXXXXXXX---XXXXXXXX+
|XXXX---XXXXXXX----------------------------YXXXXXXX+
|XXXX---XXXXXXX----------------------------XXXXXXXX+
|XXXX---XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX---XXXXXXXX+
|XXXX---XXXXXXXXXXXXXX-------XXXXXXXXXXX---XXXXXXXX+
|XXXX---XXXXXXXXXXXXXX---T---XXXXXXXXXXX---XXXXXXXX+
|XXXX---XXXXXXXXXXXXXX-------XXXXXXXXXXX---XXXXXXXX+
|XXXX---WWWWWW---------------XXXX----------XXXXXXXX+
|XXXX---WWWWWW---------------XXXX----------XXXXXXXX+
|XXXX---WWWWWW---------------XXXXXXXXXXX---XXXXXXXX+
|XXXX---XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX---XXXXXXXX+
|X------------------------------------------------X+
|X-┌┐---------------------------------------------X+
|X-└┘---------------------------------------------X+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
'''
maze9='''
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|X------------------XX-WW-----------------------T-X+
|X------------------XX-WW-------------------------X+
|X------------------XX-WW-------------------------X+
|XXXXXX---XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWWWWX+
|XXXXXX---XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWWWWX+
|XXXXXX---XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWWWWX+
|XXXXXX-------------XXXXXXXXXXXXXXXXXXXXX---------X+
|XXXXXX-------------XXXXXXXXXXXXXXXXXXXXX---------X+
|XXXXXXXXX---XXXXXXXXXXXX--------------------XXXXXX+
|XXXXXXXXX---XXXXXXXXXXXX--------------------XXXXXX+
|XXXXXXXXX---XXXXXXXXXXXXXXXXXXXXXXXXXXXX----XXXXXX+
|XXXXXXXXX---XXXXXXXXXXXXXXXXXXXXXXXXXXXX----XXXXXX+
|XXXXXXXXX---UUUYXXXXXXXXXXXXXXXXXXXXXXXX----XXXXXX+
|XXXXXXXXX---UUUXXXXXXXXXXXXXXXXXXXXXXXXX----XXXXXX+
|XXXXXXXXXXXXUUUXXXXXXXXXXXXXXXXXXXXXXXXXUUUUXXXXXX+
|XXXXXXXXXXXXUUUXXXXXXXXXXXXXXXXXXXXXXXXXUUUUXXXXXX+
|X-┌┐---------------------------------------------X+
|X-└┘---------------------------------------------X+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
'''
maze10='''
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|X---XXX----------------------------------------T-X+
|X---XXX------------------------------------------X+
|X---XXXXXUUUXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWWXXX+
|X---XXXXXWWWWWWWWWW-----------------------XXXWWXXX+
|X---XXXXXWWWWWWWWWW-----------------------XXXWWXXX+
|X---XXXXXUUUXXXXXXXXXXXXXXXXXXXXXXXXXXX---XXXXXXXX+
|X---XXXXXUUUXXXXXXXXXXXXXXXXXXXXXXXXXXX---XXXXXXXX+
|X---XXXXX---------------XXXXXXXXXXXXXXX---XXXXXXXX+
|X---XXXXX---------------XXXXXXXXXXXXXXX---XXXXXXXX+
|X---XXXXX---XXXXXXXXX---XXXXXXXXXXXXXXX---XXXXXXXX+
|X---XXXXXXXXXXXXXXXXX---XXXXXXXXXXXXXXX---XXXXXXXX+
|X---XXXXXXXXXXXXXXXXX---XXXXXXX-----------XXXXXXXX+
|X---XX------------------XXXXXXX-----------XXXXXXXX+
|X---XX------------------XXXXXXX-----XXXXXXXXXXUUUY+
|X---XXWWWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXUUUX+
|X---XXWWWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXUUUX+
|X-┌┐---------------------------------------------X+
|X-└┘---------------------------------------------X+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
'''
maze11='''
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|X----------------------------------------------T-X+
|X------------------------------------------------X+
|XWWWWWWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|XWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWX+
|XWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWX+
|XWWWWWWWWWWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|XWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWX+
|XWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWX+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWWWWWWWWWWWWWWWWX+
|XWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWX+
|XWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWX+
|XWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWX+
|XWWWWWWWWWWWWWWXXXXXXXXXXXXXXUUUUUUUUUUXXXXXXXXXXX+
|XWWWWWWWWWWWWWWXXXXXXXXXXXXXXUUUUUUUUUUYXXXXXXXXXX+
|XWWWWWWWWWWWWWWXXXXXXXXXXXXXXUUUUUUUUUUXXXXXXXXXXX+
|XWWWWWWWWWWWWWWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|X┌┐----------------------------------------------X+
|X└┘----------------------------------------------X+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
'''
maze12='''
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|X----------------------------------UU----------T-X+
|X----------------------------------UU------------X+
|XXXXXXXXXXXXXXXXXXX---XXXXXXXXXXXXXXX---XXXXXXXXXX+
|XXXXXXXXXX-----XXXX---XXXXXXXXXXXXXXX---XXXXXXXXXX+
|XXXXXXXXXX-----UUUU---XXXXXXXXXXXXXXX---XXX------X+
|XXXXXXXXXX-----UUUU---XX-----UXXXXXXXXXXXXX------X+
|XXXXXXXXXX-----XXXXXXXXX-----UYXXXXXXXXXXXX------X+
|XXXXXXXXXXUUUUUWWWWWXXXX-----XXXXXXXXXXXXXX------X+
|XXXXXXXXXXUUUUUWWWWWXXXX-----XXXXXXXXXXXXXX------X+
|XUUUUUUUUXXXXXXWWWWWXXXX-----WU------------------X+
|XUUUUUUUUXXXXXXUUUUUXXXX-----WU------------------X+
|XXXXUUUUUXXXXXXUUUUUXXXX-----XXXXXXXXXXXXXXXXXXXXX+
|XXXXUUUUUXXXXXXUUUUUXXXX-----XXXXXXXXXXXXXXXXXXXXX+
|XXXXWWWWWXXXXXXUUUUUXXXX-----XXXXXXXXXXXXXXXXXXXXX+
|XXXXUUUUUXXXXXXUUUUUXXXX-----XXXXXXXXXXXXXXXXXXXXX+
|XXXXWWWWWXXXXXXWUUUUXXXX-----XXXXXXXXXXXXXXXXXXXXX+
|X-┌┐---------------------------------------------X+
|X-└┘---------------------------------------------X+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
'''
maze13='''
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|XXX------------------------------------------XXXXX+
|XXX------------------------------------------XXXXX+
|XXX-----XXXXXXXXXXXXXXXUUUUXXXXXXXXXXXXX-----XXXXX+
|XXX-----XXXXXXXXXXXXXXXUUUUXXXXXXXXXXXXX-----XXXXX+
|XXX-----XXXXXXXXXXXXXXXUUUUXXXXXXXXXXXXX-----XXXXX+
|XXX-----XXXXXXXXXXXXXXXUUUUXXXXXXXXXXXXX-----XXXXX+
|XXX-----XXXXXXXXXXXXXXXWWWWXXX---------------UUUXX+
|XXX-----XXXXXXXXXXXXXXXWWWWXXX---------------UUUXX+
|XXX-----XXXXXXX----XXX-----XXXXXXXXXXXXXXXXXXWWWXX+
|XXX-----XXXXXXX----XXX--T--XXXXXXXXXXXXXXXXXXWWWXX+
|XXX-----XXXXXXX----XXX-----XXXXXXXWWWYXXXXXXXWWWXX+
|XXX-----XXXXXXX----XXXXXXXXXXXXXXXUUUXXXXXXXXWWWXX+
|XXX-----XXXXXXX----XXXXXXXXXXXXXXXWWWXXXXXXXXWWWXX+
|XXX-----XXXXXXX----XXXXXXXXXXXXXXXUUUXXXXXXXXWWWXX+
|XXWWWWWWWXXXXXX----XXXXXXXXXXXXXXXUUUXXXXXXXXWWWXX+
|X-┌┐---------------UU----------------------------X+
|X-└┘---------------UU----------------------------X+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
'''
maze14='''
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|XWWWWWWWWWWWWUWWWWWWWWWWWUWWWWWWWWWWWWWWWWWWWWWWWX+
|XWWWWWWWWWWWWWWWXWWWWWWWWWWWWWWWWWWWWWXWWWWWWWWWWX+
|XWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWXWWWWWWUWWWX+
|XWWWWUWWWWWWWWWWWWWWWWWUWWWWWWWWWWWWWWWWWWWWWUWWWX+
|XWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWX+
|XWWWWWWWWWWWTWWWWWWWWWWWWWWWWWUWWWWWWWWWWWWWWWWWWX+
|XWWWWWWWWWWUWWWWWWWWUWWWWWWWWWWUWWWWWWWWWWWWWWWWWX+
|XWWWWWWWWWWWWWWWWWWWUWWWWWWWWWWWWWWWWWWWWWWWWWWWWX+
|XWWWWWWWWWWWWUWWWWWWWWWWWWWWWWWWWWWWWWWUWWWWWUWWWX+
|XWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWX+
|XWWWWWWWWWWWWWWWWWWWWWWWWWWWWWXWWWWWWWWWWWWWWWWWWX+
|XWWWWWWWWWWWWWWWWWWWWWWWUWWWWWWWWWWWWWWWWWWWWWWWYX+
|XWWWWWUWWWWWWWWWWWWWWWWWWXWUWWWWWWWWWWWWWWWWWWWWWX+
|XWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWX+
|XWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWUWWWWWWWWX+
|XWWWWWWWXWWWWWWWWWWWWWWWWWWWWWWWWXWWWWWWWWWWWWWWWX+
|XW┌┐WWWWUWWWWWWWWWWWWWWWWWUWWWWWWWWWWWWWWWWWWWWWWX+
|XW└┘WWWWWWWWWWWWWWWWWWWWWWWWUWWWWWWWWWWWWWWWWUWWWX+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
'''
maze15='''
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|XXXXXXX------------UUXX----------------------XX(:X+
|XXXXXXX------------UUXX----------------------XXXXX+
|XXXXXXX----XXXXXXXUUUXXXXXXXXXXXXXXXWWWXXXXXXXXXXX+
|XXXXXXX----XXXXXXXUUUXXXXXXXXXXXXXXXWWWXXXXXXXXXXX+
|XXXXXXX----XXXXXXXWWWXXXXXUXXXXXXXXXWWWXXXXXXXXXXX+
|XXXXXXX----XXX------------UTXXXXXXXXWWWXXXXXXXXXXX+
|XXXXXXX----XXX------------UXXXXXXXXXWWWXXXXXXXXXXX+
|XXXXXXX----XXXUWWXXXXXXXXXXXXXXXXXXXWWWXXXXXXXXXXX+
|XXXXXXX----XXXUWWXXXXXXXXXXXXXXXXXXXWWWXXXXXXXXXXX+
|XXXXXXX----XXXUWWYXXXXXXXXXXXXXXXXXXWWWXXXXXXXXXXX+
|XXXXXXX----XXXXXXXXXXXXXXXXXXXXXXXXXWWWXXXXXXXXXXX+
|XXXXXXX----XXXXXXXXXXXXXXXXXXXXXXXXXWWWXXXXXXXXXXX+
|XXXXXXX----XXXXXXXXXXXXXXXXXXXXXXXXXWWWXXXXXXXXXXX+
|XUUUUUUUUUUXXXXXXXXXXXXXXXXXXXXXXXXXWWWXXXXXXXXXXX+
|XUUUUUUUUUUXXXXXXXXXXXXXWWWWWWWWWWWWWWWXXXXXXXXXXX+
|XUUUUX----UXXXXXXXXXXXXXWWWWWWWWWWWWWWWXXXXXXXXXXX+
|X-┌┐XX---------------------XXXXXXXXXXXXXXXXXXXXXXX+
|X-└┘XX---------------------XXXXXXXXXXXXXXXXXXXXXXX+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
'''
maze16='''
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|X-----------------------------------U------------X+
|X-----------------------------------U------------X+
|X----XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX---X+
|X----XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX---X+
|X----XXX:LXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX---X+
|X----XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX---X+
|X----XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX---X+
|X----XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX---X+
|X----XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX---X+
|X----XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX---X+
|X----XXXXXXXXXXXX-----------------------UUUUUU---X+
|X----UUXXXXXXXXXX-----------------------UUUUUU---X+
|X----UUYXXXXXXXXX----XXXXXXXXXXXXXXXXXXXUUUXXX---X+
|XUUUUXXXXXXWWWWWWWWWWXXXXXXXXXXXXXXXXXXXUUUXXXXXXX+
|X----XXXXXXUUUXXXWWWWWWWWWWWWUUUUUUUUUUUUUUXXX---X+
|X----XUUUUUUUUXXX----UUUUUUUUUUUUUUUUUUUXXXXXX---X+
|X┌┐------UUUUUXXX----XXXXXXXWWWWWWWWWWWWUUUUUU---X+
|X└┘------XXXXXXXX----XXXXXXXXXXXXXXXXUUUUUUUUU-T-X+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
'''
maze17='''
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|X------------------------------------------------X+
|X------------------------------------------------X+
|XXXXXXXXXXXXXXXXXXXXXXXX--XXXXXXXXXXXXXXXXXXXXXXXX+
|XXXXXXXXXXXXXXXXXXXXXXXXUUXXXXXXXXXXXXXXXXXXXXXXXX+
|XXXXXXXXXXXXXXXXXXXXXXXXUUXXXXXXXXXXXXXXXXXXXXXXXX+
|XXXXXXXXXXXXXXXXXXXXXXXXUUXXXXXXXUUUUUUUUUUUXXXXXX+
|XXXXXXXXXXXXXXXXXXXXXXXXUUXXXXXXXUUUUUUUUUUUXXXXXX+
|XXXXXXXXXXXXXXXXXXXXXXXXUUXXXXXXXUUUXXXXUUUUXXXXXX+
|XXXXXXXXXXXXXXXXXXXXXXXXUUXXXXXXXUUUXXXXWWWWXXXXXX+
|XXXXWWWWWWWUUUWWWUUUUUUU┌┐UUUUUUUWWWXXXXWWWWXXXXXX+
|XXXXWWWWWWWUUUWWWUUUUUUU└┘UUUUUUUWWWXXXXWWWWYXXXXX+
|XXXXXXXXXXXXXXUUUXXXXXXXXXXXXXXXXUUUXXXXXXXXXXXXXX+
|XXXXXXXXXXXXXXUUUXXXXXXXXXXXXXXXXUUUXXXXXXXXXXXXXX+
|XXXXXXXXXXXXXXUUUXXXXXXXXXXXXXXXXUUUXXXXXXXXXXXXXX+
|XXXXXXXXXXXXXXUUUXXXXXXX---XXXXXXXXXXXXXXXXXXXXXXX+
|XXXXXXXX-------------------XXXXXXXXXXXXXXXXXXXXXXX+
|XXXXXXXX-------------------XXXXXXXXXXXXXXXXXXXXXXX+
|XXXXXXXX-T-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
'''
maze18='''
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXUUUUUUUUUUUUUUUUUUUUUUX+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXUUUUUUUUUUUUUUUUUUUUUUX+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXUUUUXXXXXXXXXXXXXXXXXXX+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXUUUUXXXXXXXXXXXXXXXXXXX+
|XXXXXXXXXXXUUUUXXXXXXXXXXXXUUUUXXXXXXXXXXXXXXXXTXX+
|XXXXXXXXXXXUUUUXXXXXXXXXXXXUUUUUUUUUUUUUUUUUXXUUUX+
|XXXXXXXXXXXUUUUXXXXXXXXXXXXUUUUUUUUUUUUUUUUUUUUUUX+
|XXXXXXXXXXXUUUUXXXXXXXXXXXXUUUUXXXXXXXXXXUUUUUUUUX+
|XXXXXXXXXXXUUUUXXXXXXXXXXXXUUUUXXXXXXXXXXXXXXXXXXX+
|XXXXXXXXXXXUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUXX+
|XXXXXXXXXXXUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUXX+
|XX┌┐UUUUUUUUUUUXXXXXUUUUUUUUUUXXXXXXXXXXXXXXXXXXXX+
|XX└┘UUUUUUUUUUUXXXXXUUUUUUUUUUYXXXXXXXXXXXXXXXXXXX+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
'''
#New mazes
maze19='''
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|XXXXXX-----------XXXXXXXXXXXXXXXXXXXXXXXX-------TX+
|XXXXXX-----A-----XXXXXXXXXXXXXXXXXXXXXXXX--------X+
|XXXXXX-----------XXXXXXXXXXXXXXXXXXXXXXXX111XXXXXX+
|XXXXXXWWWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX---XXXXXX+
|XXXUUUWWWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX---XXXXXX+
|XXXUUUWWWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX---XXXXXX+
|XXXUUUXXXXXXXXXXXXX-------------------------XXXXXX+
|XXXUUUXXXXXXXXXXXXX-------------------------XXXXXX+
|XXXUUU---WWWXXXXXXX-------------------------XXXXXX+
|XXXUUU---WWWXXXXXXX----XXXXXXXXXXXXXXXXXXXXXXXXXXX+
|XXXXXX---XXXXXXXXXX----XXXXXXXXXXXXXXXXXXXXXXXXXXX+
|XXXXXX---XXXXXXXXXX----XXXXXXXXXXXXXXXXXXXXXXXXXXX+
|XXXXXX---XXXXXXXXXX----XXXXXXXXXXXXXXXXXXXXXXXXXXX+
|XXXXXXWWWXXXXXXXXXX----XXXXXXXXXXXXXXXXXXXXXXXXXXX+
|XXXXXXWWWXXXXXXXXXX----XXXXXXXXXXXUUUUUUUUUUUUUUUX+
|XXXXXXWWWXXXXXXXXXX----XXXXXXXXXXXUUUUUUUUUUUUUUUY+
|XX┌┐------------------------------WWWWXXXXXXXXXXXX+
|XX└┘------------------------------WWWWXXXXXXXXXXXX+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
'''
maze20='''
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|XX----------------------------------------------YX+
|XX----------------------------------------------XX+
|XX-----XXXXXXXXXXXXXXXX-----XXXXXXXXXXXXXXX-----XX+
|XX-----XXXXXXXXXXXXXXXX-----XXXXXXXXXXXXXXX-----XX+
|XX-----XXXXXXXXXXXXXXXX11111XXXXXXXXXXXXXXX-----XX+
|XX-----XXXXXXXXXXXXXXXX22222XXXXXXXXXXXXXXX-----XX+
|XX----------------XXXXX-----XXXXX---------------XX+
|XX------------B---XXXXX--T--XXXXX---A-----------XX+
|XX----------------XXXXX-----XXXXX---------------XX+
|XX-----XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----XX+
|XX-----XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----XX+
|XX-----XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----XX+
|XX-----XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----XX+
|XX-----XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----XX+
|XX-----XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----XX+
|XX┌┐--------------------------------------------XX+
|XX└┘--------------------------------------------XX+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
'''
maze21='''
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|XXXXXXXUUUXXXXXXXXXXXXX--T--XXXXXXXXXXXXXXXXXXXXXX+
|XXXXXXXUUUYXXXXXXXXXXXX-----XXXXXXXXXXXXXXXXXXXXXX+
|XXXXXXXUUUXXXXXXXXXXXXX-----XXXXXXXXXXXXXXXXXXXXXX+
|XXXXWWWUUUXXXXXXXXXXXXX-----XXXXXXXXXXXXXXXXXXXXXX+
|XXXXWWW---------------X-----X---------------XXXXXX+
|XXXXXXX---------------X-----X---------------XXXXXX+
|XXXXXXX---333333333---X-----X---222222222---XXXXXX+
|XXXXXXX---3-------3---X-----X---2-------2---XXXXXX+
|XXXXXXX---3---B---3---X-----X---2---A---2---XXXXXX+
|XXXXXXX---3-------3---X-----X---2-------2---XXXXXX+
|X-C--XX---333333333---X33333X---222222222---X--C-X+
|X----XX---------------X22222X---------------X----X+
|X----XX---------------X11111X---------------X----X+
|X----XXXXXXXWWWXXXXXXXX-----XXXXXXXWWWXXXXXXX----X+
|X----XXXXXXXWWWXXXXXXXX-----XXXXXXXWWWXXXXXXX----X+
|X----XXXXXXXWWWXXXXXXXX-----XXXXXXXWWWXXXXXXX----X+
|X-┌┐---------------------------------------------X+
|X-└┘---------------------------------------------X+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
'''
maze22='''
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|XXXXXXXXX------XX---------------XX------UUXXXXXXXX+
|XX------1------XX-------T-------XX------UUXXXXXXXX+
|XX---B--1------XX---------------XX------UUYXXXXXXX+
|XX------1------XX111111111111111XX------UUXXXXXXXX+
|XXXXXXXXX------XX222222222222222XX------UUXXXXXXXX+
|XSSSSSSSS3333333333333333333333333333333SSSSSSSSSX+
|XSSSSSSSS-------------------------------SSSSSSSSSX+
|X---------------------------------------SSSSSSSSSX+
|XSSSSSSSSSSSSSS-------------------SSSSSSSSSSSSSSSX+
|X----------S----------------S-----------S--------X+
|X-----------------------------------------------CX+
|X------------------S---------------S-------------X+
|X----SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSX+
|X--------------------------------SSSSSS---------SX+
|X--------------------------------SSSSSS---------SX+
|X-----------------------------------------SS----SX+
|X-┌┐--------------------------------------SS-AA-SX+
|X-└┘-----------------------------SSSSSSSSSSS----SX+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
'''
maze23='''
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|X-----------------------T------------------------X+
|X333333333333333333333333333333333333333333333333X+
|XSSSSSSSSSSSSSSSSSSSSSS---SSSSSSSSSSSSSSSSSSSSSSSX+
|X----------SSSSSSSSS---------UUUUUUU#UUUUUUUUUUUUX+
|X----------------------------UUUUUUUUUUUUUUUUUUUCX+
|X----SSS---------------SSS---U#UUUUUUUUUUU#UUUUUUX+
|X222222222222222222222222222222222222222222222222X+
|XWWWWXXXXXXXXXXXXXXWWWXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|XWWWWUUUUUUUUUUXXXXXXXXXXXXXUUUUUUUUXXXX---------X+
|XWWWWUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU--------BX+
|XWWWWXXXXUUUUUUUUUUUUUUUUUUUUUUXXUUUUUUU---------X+
|X----XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|X111111111111111111111111111111111111111111111111Y+
|X------------------------------------------------X+
|X----XXXXXXXXXXXXXXXXXXXUUUUUUUUXXXXXXXXXXXXXXXXXX+
|X-----------S------------------------------------X+
|X-┌┐------------------------S-------------------AX+
|X-└┘----S--------S--------------------S----------X+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
'''
maze24='''
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|X----111-----222---------333-------------XXX---T-X+
|X----111-----222---------333---------------------X+
|X----XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX---------XXX+
|X----XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|X----WUUUUUUUU#UUUUUUUUU#UUUUUUUUUUUU#UUUUU#XXXXXX+
|X----WUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUXXXXXX+
|X----WUUUUUUUUUUUUU#UUUUUUUUUU#UUUUUUUUUUUUAXXXXXX+
|X----XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|X----2--SSSS----------SSSS-------S--------CXXXXXXX+
|X----2-------------------------------------UUUUUUX+
|X----2----------SSS----------S--------S----UUUUUUX+
|X----XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXUUUX+
|X----1UUUUUXXUUUUUUUUUUUUUUXXUUUUUUUUXXUUUBXXXUUUX+
|X----1UUUUUUUUUUXXUUUUUUUUUUUUUUUUUUUUUUUUUXXXUUUX+
|X----1UUUUUUUUUUUUUUUUUUUUUUUUUUXXUUUUUUUUUXXXDUUX+
|X----XXXXXXXXUUUUUUUUXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|X-┌┐---------4444444-----------------------YXXXXXX+
|X-└┘---------4444444-----------------------XXXXXXX+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
'''
maze26='''
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX------T-X+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX--------X+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----XXXX+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----XXXX+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----XXXX+
|XXXXXXXXXXXXXXXXXXXXXXXXUUUPUUUUUUUUUUUUW-----XXXX+
|XXXXXXXXXXXXXXXXXY------UUUUUUUUUUUUUUUUW-----XXXX+
|XXXXXXXXXXXXXXXXX-------UUUUUUUUUPUUUUUUW-----XXXX+
|XXXXXXXXXXXXXXXXXXPUUUPXXXXXXXXXXXXXXXXXX-----XXXY+
|XXXXXXXXXXXXXXXXXPUUUUPXXXXXXXXXXXXXXXXXX-----XXXX+
|X------P---------------P----------------------XXXX+
|X-------P---------------P---------------------XXXX+
|X--------P---------------P--------------------XXXX+
|X--------------P---------P--------------------XXXX+
|X---------------P--------P-------P------------XXXX+
|X---------P------P-------P------P-------------XXXX+
|X-┌┐-----P--------P------------P--------------XXXX+
|X-└┘----P---------P-----------P---------------XXXX+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
'''
maze27='''
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|X----------------------------------------------T-X+
|X------------------------------------------------X+
|XPPPPPPPPPPPPPPPPPUWUPPPPPPPPPPPPPPPPPPPPPPPPPPPPX+
|XPPPPPPPPPPPPPPPPPUWUPPP###PPPPPPPPPPPPPPPPPPPPPPX+
|XPPPPPPPPPPPPPPPPPUUUUUUUUUUUUUUUUUUUUPPPPPPPPPPPX+
|XPPPPPPPPPPPPPPPPPUUUUUUUUUUUUUUUUUUUUPPPPPPPPPPPX+
|XPPPPPPPPPPPPPPPPPPPPPPPUUUPPPPPPPPPPPPPPPPPPPPPPX+
|XPPPPPPPPPPPPPPPPPPPPPPPUUUPPPPPPPPPPPPPPPPPPPPPPX+
|XPPPPPPPPPPPPPPPPPPPPPPPUUUPPPPPPPPPPPPPPPPPPPPPPX+
|XUUUUUUUU#PPPPPPPPPPPPPPUWUPPPPPPPPPPPPPPPPPPPPPPX+
|XUUUUUUWUUUUUUUUUUUUUUUUUUUPPPPPPPPPPPPPPPPPPPPPPX+
|XUUUUUUUUUUUUUUUUUUUUUUUUUUPPPPPPPPPPPPPPPPPPPPPPX+
|XUUUUPPPPPPPPPPPPPPPPPPPUUUPPPPPPPPPPPPPPPPPPPPPPX+
|XUUUUPPPPPPPPPPPPPPPPUUUUUUUPPPPPPPPPPPPPPPPPPPPPX+
|XUUUUPPPPPPPPPPPPPPPPUUUUUUYPPPPPPPPPPPPPPPPPPPPPX+
|XUWUUPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPX+
|X-┌┐-PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPX+
|X-└┘-PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPX+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
'''
maze28='''
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|XPPPPPPPPPPPPPPPPP---------PPPPPPPPPPPPPPPPPPPPPPX+
|XPPPPPPPPPPPPPPPPP----T----PPPPPPPPPPPPPPPPPPPPPPX+
|XPPPPPPPPPPPPPPPPP---------PPPPPPPPPPPPPPPPPPPPPPX+
|XPP-------PPPPPPPPPPPPP----PPPPPPPPPPPPPPPPPPPPPPX+
|XPP---D---PPPPPPPPPPPPP----PPPPP-----------PPPPPPX+
|XPP-------PPPPPPPPPPPPP----PPPPP-----------PPPPPPX+
|XPP-----------------PPP-------------PP-----PPPPPPX+
|XPP-----------------PPP-------------PP-----PPPPPPX+
|XPPPPPPPPPPPPPPPP---PPPPPPPPPPPPPPPPPP-----PPPPPPX+
|XPPPPPPPPPPPPPPPP---PPPPPPPPPPPPPPPPPP-----PPPPPPX+
|XPPPPPPPWWYWWPPPP---PPPPPPPPPPPPPPPPPP-----PPPPPPX+
|XPPPPPPPWWWWWPPPP---PPPPPPPPPPP------------PPPPPPX+
|XPPPPPPPUUUUUPPPP---PPPPPPPPPPP------------PPPPPPX+
|XPPPPPPPUUUUUPPPP---PPPPPPPPPPP----PPPPPPPPPPPPPPX+
|XPPPPPPPUUUUUPPP-----PPPPPPPPPP----PPPPPPPPPPPPPPX+
|X----PPPUUUUUPPP-----PPPPPPPPPP----PPPPPPPPPPPPPPX+
|X-┌┐-PPPPP444PPP-----PPPPPPPPPP----PPPPPPPPPPPPPPX+
|X-└┘-PPPPP-------------------------PPPPPPPPPPPPPPX+
|X----PPPPP-------------------------PPPPPPPPPPPPPPX+
|X----PPPPP----PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPX+
|X----PPPPP----PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPX+
|X----PPPPP----PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPX+
|X------------------------------------------------X+
|X------------------------------------------------X+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
'''
#One way gates: 8 up, d down, R right, L left
maze29='''
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|X-------------------------T----------------------X+
|X------------------------------------------------X+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----XXXXXXXXX+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----XXXXXXXXX+
|XXXXXXXX----------LLLL-------------------XXXXXXXXX+
|XXXXXXXY----------8888-------------------XXXXXXXXX+
|XXXXXXXXXXXXXXXXXXUUUUXXXXXXXXXXXXXX-----XXXXXXXXX+
|XXXXXXXXXXXXXXXXXXUUUUXXXXXXXXXXXXXX-----XXXXXXXXX+
|XXXXXX----------------XXXXXXXXXXXXXX-----XXXXXXXXX+
|XXXXXX----------------XXXXXXXXXXXXXX-----XXXXXXXXX+
|XXXXXX----XXXXXXXX----XXXXXXXXXXXXXX-----XXXXXXXXX+
|XXXXXX----XXXXXXXX----XXXXXXXXXXXXXX-----XXXXXXXXX+
|XXXXXX----XXXXXXXX----XXXXXXXXXXXXXX-----XXXXXXXXX+
|XXXXXX----XXXXXXXX----XXXXXX--------RRRRRXXXXXXXXX+
|XXXXXX----XXXXXXXX----XXXXXX--------RRRRRXXXXXXXXX+
|XXXXXX----XXXXXXXX----XXXXXX----XXXX-----XXXXXXXXX+
|X-┌┐--------------dddd---------------------------X+
|X-└┘--------------dddd---------------------------X+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
'''
maze30='''
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|X-----------------------T------------------------X+
|X------------------------------------------------X+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----XX2222XX+
|XXA-------XXXXXXXXXXXXXXXXXXXXXXXXXXX-----XX----XX+
|XX--------XXXXXXXXXXXXXXXXXXXXXXXXXXX11111XX----XX+
|XXXXXXXXLL--------------------------------XX----XX+
|XXXXXXXX88--------------------------------XX----XX+
|XXXXXXXX88XXXXXXXXXXXXXXXXXXXXXXXXXXX-----RRddddXX+
|XXXXXXXX------------------------XXXXX-----RRRRRRXX+
|XXXXXXXX------------------------XXXXX-----XXddddXX+
|XXXXXXXX---XXXXXXX----XXXXXX----XXXXX-----XXddddXX+
|XXXXXXXX---XXXXXXX----XXXXXX----XXXXX-----XX----XX+
|XXXXXXXX---XXXXXXX----XXXXXX----XXXXX-----XX----XX+
|XXXXXXXX---XXXXXXX----XXXXXX---------RRRRRXX----YX+
|XXXXXXXX---XXXXXXX----XXXXXX---------RRRRRXXXXXXXX+
|XXXXXXXX---XXXXXXX----XXXXXXXXXXXXXXX-----XXXXXXXX+
|X-┌┐------------------LL-----------LL------------X+
|X-└┘------------------LL-----------LL------------X+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXBXXXXXXXXXXXXXXXXXXXX+
'''

maze31='''
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|XUUUU8-----------------------------------------T-X+
|XUUUU8-------------------------------------------X+
|XUUUU8dddddddddddddddddddddddddddddddddddddddddddX+
|XUUUULLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL888dddddd8888X+
|XUUUULLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL888dddddd8888X+
|X-88-LLLLLRLLLRR8888RRRRRRRRRRRRRRRRRRRdddddd8888X+
|X-88-LLLLLRLLLRRLLLLLLLLLLLLLLLLLLLL8888RRRRRRRRRX+
|X-88-LLLLLRLLLRRLLLLLLLLLLLLLLLLLLLL8888RRRRRRRRRX+
|X-88-RRRRRRRRRRRRRRRRRRRRRRRRRLLLLLLLLLL88LLLLLLLX+
|X-88-RRRRRRRRRRRRRRRRRRRRRRRRRLLLLLLLLLL88RRRRRRRX+
|X-88-LRLLRLRLLdddRRRRRRRRRRRRRRRRRRLLLLL8888RRRRRY+
|X-88-LRLLRLRLLdddRRRRRRRRRRRRRRRRRRLLLLL8888LLLLLX+
|X-88-LLLLLLLLLdddLLLLLLLLLLLLLdddddRRRRRRRRRRRRRRX+
|X-88-LLLLLLLLLdddLLLLLLLLLLLLLdddddRRRRRRRRRRRRRRX+
|X-88-LRLLRLRLLLRLLRLRLLLRLLRLRLLLRLLRLRLLLRLLRLRLX+
|X-88-LRLLRLRLLLRLLRLRLLLRLLRLRLLLRLLRLRLLLRLLRLRLX+
|X-┌┐-LRLLRLRLLLRLLRLRLLLRLLRLRLLLRLLRLRLLLRLLRLRLX+
|X-└┘-LRLLRLRLLLRLLRLRLLLRLLRLRLLLRLLRLRLLLRLLRLRLX+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
'''
maze32='''
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|X----4-----------------------------------------T-X+
|X----4-------------------------------------------X+
|X----dddddddddddddddddddddddddddddddddddddddddRRRX+
|X----2-------3--------------X----------------X---X+
|X----2-------3--------------X┓---------------X---X+
|X----XXXXXXXXXXXXXXXXXXXXXddXXXXUUUUUUUXXXXXXX111X+
|X----2--------------------ddR----------------X---X+
|X----2--------------------RRR------S--------DX---Y+
|X----XXXXXXXXXXXXXXXXXCXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|X----RRRRRRRRRRR#RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRX+
|X----RRRRRRRRRRRRRRRRRRRRRRRRR#RRRRRRR88RRRRRRRRBX+
|X----RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRX+
|X----RRRRRRRRRRRRRRRRRR#RRRRddRRRRRRRRRRRRRR#RRRRX+
|X----XXXXXXXXXXXXXXXXXXXXXXAXXXXXXXXXXXXddXXXXXXXX+
|X----RRRRRRRRRRRRRRRRRRRRR88LLLLLLLLLLLLddRRRRRRRX+
|X-┌┐-RRRRRRRRRRRRRRRRRRRRR88LLLLLLLLLLLLddRRRRRRRX+
|X-└┘-XXXXXXXXXXXXXXXXXXXXLLLddXXXXXXXXXXXXXXXXXXXX+
|X----XXXXXXXXXXXXXXXXXXXXLLLddXXXXXXXXXXXXXXXXXXXX+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
'''


maze33='''
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|XXXYXXXXXXXXXXX------T---------XXXXXXXXXXXXXXXXXXX+
|XXXUUUUUUUUUUUU----------------XXXXXXXXXXXXXXXXXXX+
|XXXUUUUUUUUUUUUUUUUUUUUUUUU----XXXXXXXXXXXXXXXXXXX+
|XXXXXXXXXXXXXXXXXXXXXXXXXXX----XXXXXXXXXXXXXXXXXXX+
|XXXXXXXXXXXXXXXXXXXXXXXXXXX1111XXXXXXXXXXXXXXXXXXX+
|XXXXX----------------------LLLL------------------X+
|XXXXX----------------------LLLL------------------X+
|XXXXX------XXXXXXXXXXXXXXXX----XXXXXXXXXXXXX-----X+
|XXXXX------XXXXXXXXXXXXXXXX----XXXXXXXXXXXXX-----X+
|XXXXX------XXXXXXXXXXXXXXXX----XXXXXXXXXXXXX-----X+
|XXXXX------XXXXXXXXXXXXXXXXLLLL------XXXXXXX-----X+
|XXXXX------XXXXXXXXXXXXXXXXLLLL------XXXXXXX-----X+
|XXXXX------XXXXXXXXXXAXXXXXXXXX------XXXXXXX-----X+
|XXXXX------RRRRR-----------LLLL------XXXXXXX-----X+
|XXXXX------RRRRR-----------LLLL------XXXXXXX-----X+
|XXXXXddddddXXXXXXXdddddddXXXXXX888888XXXXXXX88888X+
|X-┌┐---------------------------------------------X+
|X-└┘---------------------------------------------X+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
'''
maze34='''
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|X88888RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR--T-X+
|X88888RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR----X+
|XLLLLLLLLLLLL8888dddddddddd888ddddddddddddddd1111X+
|XLLLLLLLLLLLL8888LLLLLLLLLL888LLLLLLLLLLLLLdd2222X+
|XLLLL8888RRRR8888LLLLLLLLLL888LLLLLLLLLLLLLdd3333X+
|XLLLL8888RRRR8888LLLLLLLLLL888RRRRRRRRRRRRRdd4444Y+
|XDddd8888RRRR8888LLLLLLLLLL888RRRRRRRRRRRRRddRRRRX+
|Xdddd8888dddd8888dddd8888dd888RRRRRRRRRRRRRRRRRRRX+
|X8888RRRRRRRRRRRRRRRRRRRRRR888RRRRRRRRRRRRRRRRRRRX+
|X8888RRRRRRRRRRRRRRRRRRRRRR888dddLLLLLLLLLdddddddX+
|X8888LLLLLLLLLdddRRRRRRRRRR888dddLLLLLLLLLdddddddX+
|X8888LLLLLLLLLddCRRRRRRRRRR888dddLLLLLLLLLdddddddX+
|X8888RRRRRRRRRdddRRRRRRRRRR888dddLLLLLLLLLdddddddB+
|X8888RRRRRRRRRdddRRRRRRRRRR888dddLLLLLLLLLdddddddX+
|X8888RRRRRRRRRRRRRRRRRRRRRRRRRdddRRRRRRRRRRRRRRRRX+
|X8888RRRRRRRRRRRRRRRRRRRRRRRRRdddRRRRRRRRRRRRRRRRX+
|X-┌┐-RRRRRRRRRRRRRRRRLLLLLLLLLLLLLLLLLLLLLdddddddX+
|X-└┘-RRRRRRRRRRRRRRRRLLLLLLLLLLLLLLLLLLLLLdddddddX+
|XXXXXXXXXXXXXXXXXXXXXXXXAXXXXXXXXXXXXXXXXXXXXXXXXX+
'''
maze35='''
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|XPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPX+
|XPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPX+
|XPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPX+
|XPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPX+
|XPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP888RRRRRRRRRX+
|X8888PPPPPPPP888RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRX+
|XRRRRPPPPPPPP888RRRRRRRRRRRRRRRRRRRRRRRRRRRRPPdddX+
|X8888PPPPPPPP888PPPWWWWPPPPPPPPPPPPPPPPPPPPPPPdddX+
|XRRRRPPPPPPPPLLLLLLWWWWRRRRRRRRRRRRRRRRRRRPPPPdddX+
|X8888PPPPPPPPLLLLLLWWWWRRRRRRRRRRRRRRRRRRRPPPPWWWX+
|XWWWWPPPPPPPPdddPPPWWWWPPPPPPPPPPPPPPPddddPPPPdddX+
|X8888PPPPPPPPdddPPP8888PPPPPPPPPPPPPPPddddPPPPdddX+
|XWWWWPP888PPPdddPPP8888PPPPPPPPPPPPPPPddddPPPPdddX+
|X----WWWWWRRRdddPPP8888PPPPPPPPPPPPPPPddddPPPP---X+
|X----WWWWWRRRPPPPPP8888LRRRRRRRRRRRRRRddddPPPP---X+
|X----PPddddddPPPPPP8888LRRRRRRYRRRRRRRddddPPPP---Y+
|X-┌┐-PPLLLdddRRRRRRWWWWLLLLLLLLLLLLLLLddddPPPP---X+
|X-└┘-PPdddRRRRRRRRRWWWWLLLLLLLLLLLLLLLddddPPPP-T-X+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
'''
maze36='''
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|X------------------------T-----------------------X+
|X------------------------------------------------X+
|XLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL888X+
|X►-----------------------------------------------X+
|X►------------------------------77777---------777X+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXUUUUUXXXXXXXXX---X+
|X>--------___------------------------XXXXXXXXX▼▼▼X+
|X>-----------------------------------XXXXXXXXX---X+
|X>-----------------------------------XXXXXXXXX---X+
|X>--------...------------------------YXXXXXXXX---X+
|XXXXXXXXXX---XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX---X+
|X------------------------------------------------X+
|X---------)))------------------------------------X+
|X------------------------------------------------X+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX---X+
|X------------------------------------------------X+
|X--┌┐-----------------------------------------000X+
|X--└┘-----------------------------------------000X+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
'''
maze37='''
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|X►---------------------------------------------T-X+
|X►-----------------------------------------------X+
|X►-----------------------------------------------X+
|X►-----------------------------------------------X+
|X►-----------------------------------------------X+
|X►-----------------------------------------------X+
|X►-----------------------------------------------X+
|X►-----------------------------------------------X+
|XXXXXXXXXXXXXXXXXXXXXXX---XXXXXXXXXXXXXXXXXXXXUU1Y+
|XXXXUUUUXXXXXXXX-------777----------------------◄X+
|XXXXUUUUXXX----*-------777----------------------◄X+
|XALLdd__-__----*--------------------------------◄X+
|XXLLLL---------*--------------------------------◄X+
|X▼▼▼▼▼---------*--------------------------------◄X+
|X--------------*--------------------------------◄X+
|Xxxxxxxx-------*--------------------------------◄X+
|X-┌┐--00))-----*--------------------------------◄X+
|X-└┘-----------*--------------------------------◄X+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
'''
maze38='''
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXYXX+
|XXXXXXXXXXXXXXXXX--------T-------XXXXXXXXXXXXXUUXX+
|XXXXXXXXXXXXX------------------------XXXXXXXXXUUXX+
|XXXXXXXXXX------------------------------XXXXXXUUXX+
|XXXXXXXX----------------------------------XXXXUUXX+
|XXXXX----------------------------------------XUUXX+
|XX----------------------------------------------XX+
|XaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaX+
|[►---------qq----------------------qq-----------◄]+
|[►---------qq----------------------qq-----------◄]+
|[----------qq----------------------qq-----------◄]+
|[----------qq--------//////--------qq------------]+
|[►---------qq----------------------qq------------]+
|XXXXXXXXXXXXXXXXXXXXX------XXXXXXXXXXXXXXXXXXXXXXX+
|X------------------------------------------------X+
|X-┌┐---------------------------------------------X+
|X-└┘---------------------------------------------X+
|X------------------------------------------------X+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
'''
maze39='''
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|XXXXXXXXXXXXXXXXX--------T-------XXXXXXXXXXXXXXXXX+
|XXXXXXXXXXXXX------------------------XXXXXXXXXXXXX+
|XXXXXXXXXX------------------------------XXXXXXXXXX+
|XXXXXXXX----------------------------------XXXXXXXX+
|XXXXX----------------------------------------XXXXX+
|XX----------------------------------------------XX+
|XaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaX+
|[►---------qq----------------------qq-----------◄]+
|[►---------qq----------------------qq-----------◄]+
|[►---------qq----------------------qq-----------◄]+
|[----------qq----------------------qq-----------◄]+
|[----------qq--------//////--------qq------------]+
|[►---------qq----------------------qq------------]+
|XXXXXXXXXXXXXXXXXXXXX------XXXXXXXXXXXXXXXXXXXXXYX+
|X------------------------------------------------X+
|X-┌┐---------------------------------------------X+
|X-└┘---------------------------------------------X+
|X------------------------------------------------X+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
'''
maze40='''
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|X►XXXXXXXXXXXXXXXXXXXXXXXXXXX888RRRRRRRRRRRR--T--s+
|X►XXXXXXXXXXXXYLLLL888XXXXXXX888RRRRRRRRRRRR-----s+
|X►XXXXXXXXXXXXXLLLL888XXXXXXX888888RRRRRRRRRRRRRRs+
|X►XXXXXXXX888RRRRRRRRRXXXXXXX888888RRRRRRRRRRRRRRs+
|X►XXXXXXXX888RRRRRRRRRXXXXXXX888888XXXXXXXXXXXXXXs+
|X►XXXXXXXX888XXXXXXdddXXXXXXX888888XXXXXXXXXXXXXXs+
|X►XXXXXXXX888XXXXXXdddXXXXXXX888888XXXXXXXXXXXXXXs+
|X►XXXXXXXX888XXXXXXdddRRRRRRRRRRLLLLL888XXXXXXXXXs+
|X►XXXXXXXX888XXXXXXdddRRRRRRRRRRLLLLL888XXXXXXXXXs+
|X►XXXXXXXX888XXXXXXXXXXXXXXXXXXXXXXXXLLLLLLLL888Xs+
|X►XXXXXXXX888XXXXXXXXXXXXXXXXXXXXXXXXLLLLLLLL888Xs+
|X►XXXXXXXX888XXXXXXXXXXXXXXXXXXXXXXXXXXXXX888RRRXs+
|X►XXXXXXXX888XXXXXXXXXXXXXXXXXXXXXXXXXXXXX888RRRXs+
|X►XXXXXXXXLLLLLLLLLLLLLLLLLLLLLLLLLLLL888RRRRXXXXs+
|X►XXXXXXXXLLLLLLLLLLLLLLLLLLLLLLLLLLLL888RRRRXXXXs+
|X►XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX777XXXXXXXXs+
|X►X-┌┐-------------------------------------------s+
|X►X-└┘-------------------------------------------s+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
'''
maze41='''
|XXXXXXXXXXXXXXXXXXXXXXX-T-XXXXXXXXXXXXXXXXXXXXXXXX+
|XaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaX+
|[►---------qq----------------------qq-----------◄]+
|[►---------qq----------------------qq-----------◄]+
|[►---------qq----------------------qq-----------◄]+
|[----------qq---------/////--------qq-----------◄]+
|[----------qq----------------------qq------------]+
|XXXXXXXXXXXXXXXXXXXXXX-----XXXXXXXXXXXXXXXXXXXXXXX+
|X------------------------------------------------X+
|X------------------------------------------------X+
|XXXXXXXXXXXXXXXXXXXXXX1111111XXXXXXXXXXXXXXXXXXXXX+
|X>XXXXXXXXXXY---888--------------------------XXXXs+
|X>XXXXXXXXXXX---888--------------------------XXXXs+
|X>XXXXXXXXXXXXXALLLLLLLLLLddXXXXXXXXXXXXX----XXXXs+
|X>XXXXXXXXXXXXXXLLLLLLLLLL88XXXXXXXXXXXXX----XXXXs+
|X>XXXXXX-------------------------------------XXXXs+
|X>XXXXXX...----------------------------------XXXXs+
|X-┌┐-------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|X-└┘-------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXY+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
'''
#Gotta makes this ooooooooof
maze42='''
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXYXX+
|XXXXXXXXXXXXXXXX--------T-------XXXXXXXXXXXXXUUUXX+
|XXXXXXXXXXXX------------------------XXXXXXXXXUUUXX+
|XXXXXX--------------------------------------XUUUXX+
|XaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaX+
|[►---------qq----------------------qq-----------◄]+
|[►---------qq----------------------qq-----------◄]+
|[----------qq----------------------qq-----------◄]+
|[----------qq----------------------qq------------]+
|[----------qq----------------------qq------------]+
|[►---------qq----------------------qq-----------◄]+
|[----------qq----------------------qq------------]+
|[►---------qq----------------------qq------------]+
|[----------qq--------/////---------qq-----------◄]+
|[►---------qq----------------------qq-----------◄]+
|XXXXXXXXXXXXXXXXXXXXX-----XXXXXXXXXXXXXXXXXXXXXXXX+
|X------------------------------------------------X+
|X-┌┐---------------------------------------------X+
|X-└┘---------------------------------------------X+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
'''
maze43='''
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|X----------------------------------------------T-X+
|X------------------------------------------------X+
|X------------------------------------------------X+
|X------------------------------------------------X+
|X------------------------------------------------X+
|X------------------------------------------------X+
|X------------------------------------------------X+
|X------------------------------------------------X+
|X------------------------------------------------X+
|X------------------------------------------------X+
|X------------------------------------------------X+
|X------------------------------------------------X+
|X------------------------------------------------X+
|X------------------------------------------------X+
|X------------------------------------------------X+
|X------------------------------------------------Y+
|X-┌┐---------------------------------------------X+
|X-└┘---------------------------------------------X+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
'''
maze44='''
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
|X----------------------------------------------T-X+
|X------------------------------------------------X+
|X------------------------------------------------X+
|X------------------------------------------------X+
|X------------------------------------------------X+
|X------------------------------------------------X+
|X------------------------------------------------X+
|X------------------------------------------------X+
|X------------------------------------------------X+
|X------------------------------------------------X+
|X------------------------------------------------X+
|X------------------------------------------------X+
|X------------------------------------------------X+
|X------------------------------------------------X+
|X------------------------------------------------X+
|X------------------------------------------------Y+
|X-┌┐---------------------------------------------X+
|X-└┘---------------------------------------------X+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+
'''
maze1=list(maze1)
maze2=list(maze2)
maze3=list(maze3)
maze4=list(maze4)
maze5=list(maze5)
maze6=list(maze6)
maze7=list(maze7)
maze8=list(maze8)
maze9=list(maze9)
maze10=list(maze10)
maze11=list(maze11)
maze12=list(maze12)
maze13=list(maze13)
maze14=list(maze14)
maze15=list(maze15)
maze16=list(maze16)
maze17=list(maze17)
maze18=list(maze18)
maze19=list(maze19)
maze20=list(maze20)
maze21=list(maze21)
maze22=list(maze22)
maze23=list(maze23)
maze24=list(maze24)
mazeo1=list(mazeo1)
maze26=list(maze26)
maze27=list(maze27)
maze28=list(maze28)
maze29=list(maze29)
maze30=list(maze30)
maze31=list(maze31)
maze32=list(maze32)
maze33=list(maze33)
maze34=list(maze34)
maze35=list(maze35)
maze36=list(maze36)
maze37=list(maze37)
maze38=list(maze38)
maze39=list(maze39)
maze40=list(maze40)
maze41=list(maze41)
maze42=list(maze42)



maze36_2=list(maze36).copy()










  
#Temp saves poggers?
def underline(yuikjh):
  return "\u0332".join(yuikjh)

listoweird=[40,41]
rights=['►','>','╝','╜','╛']
ups=['▲','^','╭','╮','◜']
lefts=['◄','<','╚','╙','╘']
downs=['▼','_','⏊','⏋','⏌']
rights2=['>','╝','╜','╛']
ups2=['^','╭','╮','◜']
lefts2=['<','╚','╙','╘']
downs2=['_','⏊','⏋','⏌']
spikez=['▼','_','⏊','⏋','⏌','◄','<','╚','╙','╘','►','>','╝','╜','╛','▲','^','╭','╮','◜']
isgoodtogo=True
secrets=0
linez=['┘','└','┐','┌']
randomstuff=False
triggers=['0',')','.','*','9',',','7','6','/']
trigdict={
  '0':['▼',False],
  ')':['_',False],
  '9':['▲',False],
  '6':['^',False],
  '*':['◄',False],
  ',':['<',False],
  '7':['►',False],
  '.':['>',False],
  '/':['►',False],
  '?':['◄',False]
}
dictofweird={
  40:1.5,
  41:1
}
#Make it delay between each then a graph of how its going to be set up
chartdict={
  38:[[[10,'ss--s','s--ss'],[10,'s---s','--s--'],[10,'ss--s','s--ss'],[10,'s---s','--s--']],[[480,533,586,639,692],[527,580,633,686,739]]],
  39:[[[10,'ss---s','ss--ss'],[5,'s----s','s----s'],[7,'---s--','s---ss'],[10,'-s---s','--ss--']],[[427,480,533,586,639,692],[474,527,580,633,686,739]]],
  41:[[[7,'s---s','ss--s'],[4,'----s','ss---'],[15,'--s--','s----'],[7,'s---s','s---s']], [[108,160,212,264,316],[157,209,261,313,365]]],
  42:[[[7,'s--s--s--s','--s--s--s-'],[4,'s--s--s--s','--s--s--s-'],[15,'s--s--s--s','--s--s--s-']], [[269,321,373,425,477,529,581,633,685,737],[314,366,418,470,522,574,626,678,730,782]]],
}
chartindes={
  38:[765,766,767,768,769,770],
  39:[765,766,767,768,769,770],
  41:[395,396,397,398,399,400],
  42:[817,818,819,820,821,822],
}

spik = ["S",'P','#']
goods=['-','W','U',' ','0',')','.','*','9',',','7','6','/']
j=False
f=[115,101,99,114,101,116,32,115,116,117,102,102,32,104,101,114,101]
da=True
howman=-1
blockgood=False
def spikeem(which,multi=False,chart=[],chart2=[],dis=False):
  global mazeq,box1,box2,box3,box4,j,da,howman,blockgood,z
  z2=z
  j=False
  ew2=True
  if howman==-1:
    howman=0
  howman+=1
  g=0
  y_t='up'
  if which in rights:
    g=1
    y_t='right'
  if which in ups:
    g=-53
  if which in lefts:  
    g=-1
    y_t='right'
  if which in downs:
    g=53
  y=[]
  Q=0
  try:
    while True:
      R=mazeq.index(which,Q)
      Q=R+1
      y.append(R)
  except:
    pass
  nextt='-'
  replace='-'
  defi=0
  tr=1
  countp=-1
  thingon=0
  qx=False
  right=rights2.copy()
  left=lefts2.copy()
  up=ups2.copy()
  down=downs2.copy()
  try:
    while (nextt in goods or nextt in linez and tr==1 or nextt in spikez) or (z in listoweird) or nextt in ['q','x'] and nextt !='s':
      countp+=1
      for i in y:
        if da==True:
          da=False
          qx=True
        try:
          replace=mazeq[i+defi+g]
          if replace=='x':
            replace='-'
        except:
          replace='-'
        if replace in linez or z2!=z:
          replace='X'
          goback()
          mazeq=mazeq_2.copy()
          box1=int(mazeq.index('┌'))
          box2=int(mazeq.index('┐'))
          box3=int(mazeq.index('└'))
          box4=int(mazeq.index('┘'))
          tr=0
          da=False
          j=True
          k
        if j==True:
          print(a)
        if tr==1:
          if replace!='q' and nextt!='q' and mazeq[i+defi]!='q':
            if (replace=='-' and z in listoweird)==False: 
              mazeq[i+defi]=replace
            else:
              mazeq[i+defi]='X'
            ew=True
          if replace!='q' and nextt!='q' and mazeq[i+defi+g]!='q' or ew==True:
            mazeq[i+defi+g]=which
          else:
            ew2=False
          ew=False
        try:
          if tr==1:
            nextt=mazeq[i+defi+g+g]
        except:
          nextt='X'
      if ew2==False:
        while which in mazeq:
          mazeq[mazeq.index(which)]='-'
        defi+=g
        ew2=True
      if multi==True and (da==True or qx==True):
        da=False
        qx=True
        if chart[thingon][0]==countp and thingon<len(chart):
          countp=0
          if '[' in mazeq: #This is for left and right idk lol
            for i in range(len(chart2[0])):
              if chart[thingon][1][i]!='-':
                mazeq[chart2[0][i]]=right[0]
              if chart[thingon][2][i]!='-':
                mazeq[chart2[1][i]]=left[0]
            neh2=Thread(target=spikeem, args=(left[0],False,[],[],True))
            neh2.start()
            left.remove(left[0])
            time.sleep(.02)
            neh=Thread(target=spikeem, args=(right[0],False,[],[],True))
            neh.start()
            right.remove(right[0])
            time.sleep(.02)
          thingon+=1
      defi+=g
      if qx==True or dis==False and tr==1:
        UPME()
        sys.stdout.flush()
      for i in range(5):
        if y_t=='up':
          time.sleep(.12)
        else:
          if z not in listoweird:
            time.sleep(.05)
          else:
            time.sleep(dictofweird[z]/5)
        if j==True:
          print(a)
      if j==True:
        print(a)
    howman-=1
    sys.stdout.flush()
    UPME()
    if howman<=0 and j==False:
      blockgood=True
    if multi==True or dis==True:
      try:
        while which in mazeq:
          mazeq[mazeq.index(which)]='-'
      except:
        pass
    if multi==True:
      if thingon==len(chart):
        print(a)
    if qx==True and multi==True:
      for i in range(30):
        if nothing()==False:
          sys.stdout.flush()
          UPME()
          time.sleep(.4)
      da=True
  except:
    howman-=1
    sys.stdout.flush()
    UPME()
    if howman<=0 and j==False:
      blockgood=True
    if multi==True or dis==True:
      while which in mazeq:
        mazeq[mazeq.index(which)]='-'
    if qx==True:
      for i in range(30):
        if nothing()==False:
          sys.stdout.flush()
          UPME()
          time.sleep(.4)  
      da=True



#Key: - = Walls X = Player T = treasure/goal 
#Got to add other boxes
colorchoice=bright_black+bold
colorchoice2=yellow
mazeq=''
def changemaze(th=1):
  global mazeq
  if th==1:
    while '1' in mazeq:
      mazeq[mazeq.index('1')]='-'
  if th==2:
    while '2' in mazeq:
      mazeq[mazeq.index('2')]='-'
  if th==3:
    while '3' in mazeq:
      mazeq[mazeq.index('3')]='-'
  if th==4:
    while '4' in mazeq:
      mazeq[mazeq.index('4')]='-'
thnig="".join(map(chr,f))
z=1
saving=True

while True:
  C('clear')
  print(astr)
  yyou=getkey()
  if yyou=='q':
    if secr==1:
      if randomstuff==True:
        randomstuff=False
        c2='\033[38;5;1m'
      else:
        randomstuff=True
        c2='\033[38;5;34m'
      C('clear')
      print("Rainbow Mode: "+c2+str(randomstuff)+reset)
      if randomstuff==True:
        print("Slight seizure warning lol")
      time.sleep(2)
      C('clear')
  elif yyou=='l':
    try:
      z=load(name+'.json')
      C('clear')
      print("Load success!")
      time.sleep(2)
      C('clear')
    except:
      print("Load failed!")
      time.sleep(2)
  elif yyou==thnig:
    randomstuff=True
    break
  elif yyou=='z':
    if saving==True:
      saving=False
      c2='\033[38;5;1m'
    else:
      saving=True
      c2='\033[38;5;34m'
    C('clear')
    print("Saving State: "+c2+str(saving)+reset)
    time.sleep(2)
    C('clear')
  else:
    break
colordict={
  1:red,
  2:yellow,
  3:green,
  4:blue,
  5:cyan,
  6:black,
  7:purple,
  8:bright_blue,
  9:bright_red,
  10:bright_magenta,
  11:bright_green,
  12:bright_black+bold,
  13:bright_cyan,
  14:bright_yellow,
  15:red,
}
if yyou.lower()=='c':
  going=True
  while going:
    C('clear')
    print("Lets customize your maze!")
    print("What color would you like the walls to be? (Enter=Gray, Wrong input=Gray)")
    print("1) Red\n2) Orange(Yellow)\n3) Green\n4) Blue\n5) Cyan\n6) Black(Invisible)\n7) Magenta\n8) Light Blue\n9) Light Red\n10) Light Magenta\n11) Light Green\n12) Light Black(Gray)\n13) Light Cyan\n14) Light Yellow")
    thingwq=input()
    if thingwq in ['1','2','3','4','5','6','7','8','9','10','11','12','13','14']:
      print(colordict[int(thingwq)]+"This is how your color looks.")
      print(reset+"Is this good?")
      yesonobro=input().lower().strip()
      if yesonobro in ['yes','y','ye']:
        print("Ok! Onto treasure color!")
        colorchoice=colordict[int(thingwq)]
        time.sleep(2)
        going=False
      elif yesonobro in ['no','n']:
        print("Ok, lets change it!")
        time.sleep(2)
    else:
      going=False
  goingfor2=True
  while goingfor2:
    C('clear')
    print("What color would you like the treasure/goal to be? (Enter=Gray, Wrong input=Gray)")
    print("1) Red\n2) Orange(Yellow)\n3) Green\n4) Blue\n5) Cyan\n6) Black(Invisible)\n7) Magenta\n8) Light Blue\n9) Light Red\n10) Light Magenta\n11) Light Green\n12) Light Black(Gray)\n13) Light Cyan\n14) Light Yellow")
    thingwq2=input()
    if thingwq2 in ['1','2','3','4','5','6','7','8','9','10','11','12','13','14']:
      print(colordict[int(thingwq2)]+"This is how your color looks.")
      print(reset+"Is this good?")
      yesonobro=input().lower().strip()
      if yesonobro in ['yes','y','ye']:
        print("Ok! Onto the maze!")
        colorchoice2=colordict[int(thingwq2)]
        time.sleep(2)
        goingfor2=False
      elif yesonobro in ['no','n']:
        print("Ok, lets change it!")
        time.sleep(2)
    else:
      goingfor2=False
C('clear')
stuff={
  1:maze1,
  2:maze2,
  3:maze3,
  4:maze4,
  5:maze5,
  6:maze6,
  7:maze7,
  8:maze8, 
  9:maze9,
  10:maze10,
  11:maze11,
  12:maze12,
  13:maze13,
  14:maze14,
  15:maze15,
  16:maze16,
  17:maze17,
  18:maze18,
  19:maze19,
  20:maze20,
  21:maze21,
  22:maze22,
  23:maze23,
  24:maze24,
  25:mazeo1,
  26:maze26,
  27:maze27,
  28:maze28,
  29:maze29,
  30:maze30,
  31:maze31,
  32:maze32,
  33:maze33,
  34:maze34,
  35:maze35,
  36:maze36,
  37:maze37,
  38:maze38,
  39:maze39,
  40:maze40,
  41:maze41,
  42:maze42,
}
def goback():
  global mazeq,z,trigdict,blockgood
  blockgood=False
  for i in triggers:
    trigdict[i][1]=False

  mazeq[box1]='-'
  mazeq[box2]='-'
  mazeq[box3]='-'
  mazeq[box4]='-'
  if z != 17:
    mazeq[905]='┌'
    mazeq[906]='┐'
    mazeq[958]='└'
    mazeq[959]='┘'
  else:
    mazeq[556]='┌'
    mazeq[557]='┐'
    mazeq[609]='└'
    mazeq[610]='┘'
def secretpog():
  global mazeq, secrets
  mazeq[mazeq.index('Y')]="X"
  secrets+=1
  C('clear')
def printhint():
  C('clear')
  if z==1:
    print("Collect the Treasure at the top right corner!")
  if z==2:
    print("Navigate the maze to the treasure at the top right!")
  if z==3:
    print("Your goal is to get to the top right corner where the treasure is!")
  if z==4:
    print("A bit tricky, but you still have to get to the top right!")
  if z==5:
    print("Try to find the right path to the top right!")
  if z==6:
    print("Even more paths, but the goal still lies in the top right!")
  if z==7:
    print("So many paths... wonder which one leads to the treasure...")
  if z==8:
    print("This time the goal is in the center, but it seems impossible! Wait.... are those 'W's...")
  if z==9:
    print("Ok... this has to be impossible.... Unless the 'W's turned into 'X's... that cant be right?")
  if z==10:
    print("Some more fake 'X's and 'W's, nothing bad about this!")
  if z==11:
    print("Thats alot of 'W's.. Lets get to eating!")
  if z==12:
    print("Again seems impossible, must be a lot of fake walls!")
  if z==13:
    print("Seems like a clear shot to the T, gotta be fake walls at the end of the hall right?")
  if z==14:
    print("Literally just satisfaction")
  if z==15:
    print("Wait what... why is there a smiley face.. Wonder where the 'T' went")
  if z==16:
    print("The 'T' is all the way to the right? Seems easy enough!")
  if z==17:
    print("Trapped in a box..again. Guess you should try to find clues as to where the fake walls are!")
  if z==18:
    print("An invisible maze... sorry")
  if z==19:
    print("What is that white wall over to the right... And whats that white button to the left? Maybe they are connected...")
  if z==20:
    print("Two buttons now? Just some logic I guess, but its easy if you remember different color buttons open different color gateways")
  if z==21:
    print("Thats one spooky face, but I guess the hard part is getting the buttons to work huh?")
  if z==22:
    print("What are those red blobs? Maybe you shouldnt go near them...")
  if z==23:
    print("Seems like there are three sections separated by walls. Guess you have to press the buttons!")
  if z==24:
    print("Just more buttons, looks like the secret is covered too.")
  if z==25:
    print("Not gonna lie, this is a mess. At least I didnt make it :D (Submitted by JasonLiu19)")
  if z==26:
    print("Are those wall spikes? Wait what")
  if z==27:
    print("Great, wall spikes instead of walls. Maybe theres some hints as to where the real path is..")
  if z==28:
    print("Wow thats a big maze. Wonder who thought this was a good idea. Seems like they are all spikes again, be careful!")
  if z==29:
    print("Another new type of block! They seem like you can only move into 'U' blocks by going up, 'D' blocks by going down, 'L' by going left, and 'R' by going right. Yay.")
  if z==30:
    print("Buttons, one way blocks, and annoying paths. Perfect level!")
  if z==31:
    print("A maze made completly out of one way blocks b r u h")
  if z==32:
    print("Another one of these multi part mazes, but with one way blocks")
  if z==33:
    print("Not a ton of spam... Seems pretty doable!")
  if z==34:
    print('I jinxed it... Good luck')
  if z==35:
    print('Now its even harder bruh the walls are spikes')
  if z==36:
    print('Are those spikes? They seem very unstable... They look more lethal than regular spikes, I wouldn\'t stay under them for too long...')
  if z==37:
    print('Just a lot of spike traps, it seems as if they only get trigerred if you get within a certan distance, use this to your advantage!')
  if z==38:
    print('Well this looks like a survival section... Great')
  if z==39:
    print("Another survival section! A bit larger this time.")
  if z==40:
    print("Red spikes! They seem just as unstable as the previoues ones, but they cover the entire screen! You might want to hurry up!")
  print("[Any key to continue]")
  getkey()
  C('clear')

def trigdetect(io):
  global oooG
  if io=='left':
    if mazeq[box2-2]in triggers:
      cor=mazeq[box2-2]
    elif mazeq[box4-2]in triggers:
      cor=mazeq[box4-2]
    elif mazeq[box1-2]in triggers:
      cor=mazeq[box1-2] 
    elif mazeq[box3-2]in triggers:
      cor=mazeq[box3-2]
  if io=='right':
    if mazeq[box2+2]in triggers:
      cor=mazeq[box2+2]
    elif mazeq[box4+2]in triggers:
      cor=mazeq[box4+2]
    elif mazeq[box1+2]in triggers:
      cor=mazeq[box1+2] 
    elif mazeq[box3+2]in triggers:
      cor=mazeq[box3+2]
  if io=='up':
    if mazeq[box1-53] in triggers:
      cor=mazeq[box1-53]
    elif mazeq[box2-53] in triggers:
      cor=mazeq[box2-53]
  if io=='down':
    if mazeq[box3+53]in triggers:
      cor=mazeq[box3+53]
    elif mazeq[box4+53]in triggers:
      cor=mazeq[box4+53]
  if trigdict[cor][1]==False:
    trigdict[cor][1]=True
    if cor not in ['/','?']:
      try:
        newt=Thread(target=spikeem ,args=(trigdict[cor][0])) 
        newt.start()    
      except:
        pass
    else:
      if cor=='/':
        oooG=True
        newt2=Thread(target=spikeem, args=('►',True,chartdict[z][0],chartdict[z][1]))
        newt23=Thread(target=spikeem, args=('◄',False,[],[],True))
      else:
        newt2=Thread(target=spikeem, args=('▲',True,chartdict[z][0],chartdict[z][1]))
        newt23=Thread(target=spikeem, args=('▼',False,[],[],True))
      newt2.start()
      newt23.start()


totalWs=0
        


sped1=''
def nextlevel():
  global z,mazeq,isgoodtogo,sped1,trigdict,mazeq_2,blockgood,howman,j,secr,totalWs
  totalWs+=mazeq_2.count('W')-mazeq.count('W')
  j=True
  howman=-1
  blockgood=False
  for i in triggers:
    trigdict[i][1]=False
  isgoodtogo=False
  z+=1
  if z==41:
    C('clear')
    print("You Won!")
    print("You found "+str(secrets)+" secrets")
    if secrets==0:
      print("Try to look for 'Y's in the mazes... They are there somewhere!")
    elif secrets in range(1,30):
      print("Try to find them all!")
    elif secrets in range(30,40):
      print("So close to all of them!")
    elif secrets==40:
      print(red+"You"+yellow+' got '+green+"them"+blue+" all!"+reset)
      print("You might find something extra at the title screen :)")
      secr=1
    print("It took you "+str(round(time.time()-sped1))+" seconds to beat all the mazes!")
    sys.exit()
  save(name+'.json',[z,secr])
  C('clear')
  mazeq=stuff[z]
  mazeq_2=mazeq.copy()
  isgoodtogo=True
  j=False
def nothing(fr=False):
  global mazeq
  for i in rights:
    if i in mazeq:
      if fr==True:
        print("rights")
      return False
  for i in lefts:
    if i in mazeq:
      if fr==True:
        print("lefts")
      return False
  for i in ups:
    if i in mazeq:
      if fr==True:
        print("ups")
      return False
  for i in downs:
    if i in mazeq:
      if fr==True:
        print("downs")
      return False
  return True
def move(dir):
  global secrets,isgoodtogo,z
  if isgoodtogo==True:
    if dir=='left':
      if mazeq[box2-2] in triggers or mazeq[box4-2]in triggers or mazeq[box1-2]in triggers or mazeq[box3-2]in triggers:
        trigdetect("left")
      if mazeq[box3-2]=='T' or mazeq[box4-2]=='T' or mazeq[box2-2]=='T' or mazeq[box1-2]=='T':
        nextlevel()
      elif mazeq[box2-2]=='A' or mazeq[box4-2]=='A' or mazeq[box1-2]=='A' or mazeq[box3-2]=='A':
        changemaze(1)
      elif mazeq[box2-2]=='B' or mazeq[box4-2]=='B' or mazeq[box1-2]=='B' or mazeq[box3-2]=='B':
        changemaze(2)
      elif mazeq[box2-2]=='C' or mazeq[box4-2]=='C' or mazeq[box1-2]=='C' or mazeq[box3-2]=='C':
        changemaze(3)
      elif mazeq[box2-2]=='D' or mazeq[box4-2]=='D' or mazeq[box1-2]=='D' or mazeq[box3-2]=='D':
        changemaze(4)
      elif mazeq[box2-2]=='┓' or mazeq[box4-2]=='┓' or mazeq[box1-2]=='┓' or mazeq[box3-2]=='┓':
        C('clear')
        print("You found a useless secret lol")
        time.sleep(2)
        print("Flex it if you want pogggg")
        input('[Enter to continue]')
        C('clear')
      elif mazeq[box2-2]=='Y' or mazeq[box4-2]=='Y' or mazeq[box1-2]=='Y' or mazeq[box3-2]=='Y':
        secretpog()
      elif mazeq[box2-2]in spik or mazeq[box4-2]in spik or mazeq[box1-2]in spik or mazeq[box3-2]in spik:
        goback()
      elif (mazeq[box1-2] in goods or mazeq[box1-2]=='L') and (mazeq[box3-2] in goods or mazeq[box3-2]=='L'):
        mazeq[box1]='-'
        mazeq[box2]='-'
        mazeq[box3]='-'
        mazeq[box4]='-'
        mazeq[box1-2]='┌'
        mazeq[box2-2]='┐'
        mazeq[box3-2]='└'
        mazeq[box4-2]='┘'
    if dir=='right':
      if mazeq[box2+2]in triggers or mazeq[box4+2]in triggers or mazeq[box1+2]in triggers or mazeq[box3+2]in triggers:
        trigdetect('right')
      if mazeq[box2+2]=='T' or mazeq[box4+2]=='T' or mazeq[box1+2]=='T' or mazeq[box3+2]=='T':
        nextlevel()
      elif mazeq[box2+2]=='A' or mazeq[box4+2]=='A' or mazeq[box1+2]=='A' or mazeq[box3+2]=='A':
        changemaze(1)
      elif mazeq[box2+2]=='B' or mazeq[box4+2]=='B' or mazeq[box1+2]=='B' or mazeq[box3+2]=='B':
        changemaze(2)
      elif mazeq[box2+2]=='C' or mazeq[box4+2]=='C' or mazeq[box1+2]=='C' or mazeq[box3+2]=='C':
        changemaze(3)
      elif mazeq[box2+2]=='D' or mazeq[box4+2]=='D' or mazeq[box1+2]=='D' or mazeq[box3+2]=='D':
        changemaze(4)
      elif mazeq[box2+2]in spik or mazeq[box4+2]in spik or mazeq[box1+2]in spik or mazeq[box3+2]in spik:
        goback()
      elif mazeq[box2+2]=='Y' or mazeq[box4+2]=='Y' or mazeq[box1+2]=='Y' or mazeq[box3+2]=='Y':
        secretpog()
      elif (mazeq[box2+2] in goods or mazeq[box2+2]=='R') and (mazeq[box4+2] in goods or mazeq[box4+2]=='R'):
        mazeq[box1]='-'
        mazeq[box2]='-'
        mazeq[box3]='-'
        mazeq[box4]='-'
        mazeq[box1+2]='┌'
        mazeq[box2+2]='┐'
        mazeq[box3+2]='└'
        mazeq[box4+2]='┘'
    if dir=='up':
      if mazeq[box3-106] in triggers or mazeq[box4-106]in triggers or mazeq[box1-53] in triggers or mazeq[box2-53]in triggers:
        trigdetect('up')
      if mazeq[box3-106]=='T' or mazeq[box4-106]=='T' or mazeq[box2-53]=='T' or mazeq[box1-53]=='T':
        nextlevel()
      elif mazeq[box3-106]=='A' or mazeq[box4-106]=='A' or mazeq[box1-53]=='A' or mazeq[box2-53]=='A':
        changemaze(1)
      elif mazeq[box3-106]=='B' or mazeq[box4-106]=='B' or mazeq[box1-53]=='B' or mazeq[box2-53]=='B':
        changemaze(2)
      elif mazeq[box3-106]=='C' or mazeq[box4-106]=='C' or mazeq[box1-53]=='C' or mazeq[box2-53]=='C':
        changemaze(3)
      elif mazeq[box3-106]=='D' or mazeq[box4-106]=='D' or mazeq[box1-53]=='D' or mazeq[box2-53]=='D':
        changemaze(4)
      elif mazeq[box3-106]=='Y' or mazeq[box4-106]=='Y' or mazeq[box1-53]=='Y' or mazeq[box2-53]=='Y':
        secretpog()
      elif mazeq[box3-106]in spik or mazeq[box4-106]in spik or mazeq[box1-53]in spik or mazeq[box2-53]in spik:
        goback()
      elif (mazeq[box2-53] in goods or mazeq[box2-53] == '8') and (mazeq[box1-53] in goods or mazeq[box1-53]=='8'):
        mazeq[box1]='-'
        mazeq[box2]='-'
        mazeq[box3]='-'
        mazeq[box4]='-'
        mazeq[box1-53]='┌'
        mazeq[box2-53]='┐'
        mazeq[box3-53]='└'
        mazeq[box4-53]='┘'
    if dir=='down':
      if mazeq[box3+53]in triggers or mazeq[box4+53]in triggers or mazeq[box2+106]in triggers or mazeq[box1+106]in triggers:
        trigdetect('down')
      if mazeq[box3+53]=='T' or mazeq[box4+53]=='T' or mazeq[box2+106]=='T' or mazeq[box1+106]=='T':
        nextlevel()
      elif mazeq[box3+53]in spik or mazeq[box4+53]in spik or mazeq[box2+106]in spik or mazeq[box1+106]in spik:
        goback()
      elif mazeq[box3+53]=='A' or mazeq[box4+53]=='A' or mazeq[box1+106]=='A' or mazeq[box2+106]=='A':
        changemaze(1)
      elif mazeq[box3+53]=='B' or mazeq[box4+53]=='B' or mazeq[box1+106]=='B' or mazeq[box2+106]=='B':
        changemaze(2)
      elif mazeq[box3+53]=='C' or mazeq[box4+53]=='C' or mazeq[box1+106]=='C' or mazeq[box2+106]=='C':
        changemaze(3)
      elif mazeq[box3+53]=='D' or mazeq[box4+53]=='D' or mazeq[box1+106]=='D' or mazeq[box2+106]=='D':
        changemaze(4)
      elif (mazeq[box3+53] in goods or mazeq[box3+53]=='d') and (mazeq[box4+53] in goods or mazeq[box4+53]=='d'):
        mazeq[box1]='-'
        mazeq[box2]='-'
        mazeq[box3]='-'
        mazeq[box4]='-'
        mazeq[box1+53]='┌'
        mazeq[box2+53]='┐'
        mazeq[box3+53]='└'
        mazeq[box4+53]='┘'
def printmaze(themaze):
  global goods,howman
  print('\t\t\t\t\t\t\t\t Level '+str(z),end='')
  for i in themaze:
    if i=='|':
      print("\t\t\t",end="")
    elif i in ['►','>','╝','╜','╛']:
      if z not in listoweird:
        print("►",end='')
      else:
        if mazeq==maze41:
          if i=='>':
            print(colorchoice+'\033[38;5;1m'+"►"+reset,end='')
          else:
            print("►",end='')
        else:
          print(colorchoice+'\033[38;5;1m'+"►"+reset,end='')
    elif i in ['▲','^','╭','╮','◜']:
      print("▲",end='')
    elif i in ['◄','<','╚','╙','╘']:
      print("◄",end='')
    elif i in ['▼','_','⏊','⏋','⏌']:
      print("▼",end='')
    elif i in ['X','P','[',']','x','U','s']:
      print(colorchoice+" "+reset,end="")
    elif i=='-':
      print(" ",end="")
    elif i=='+':
      pass
    elif i=="T":
      print(colorchoice2+" "+reset,end="")
    elif i=="8":
      print(colorchoice+"U"+reset,end="")
    elif i in ['a','q']:
      if blockgood or nothing():
        if howman>0:
          howman=0
        print(colorchoice+'\033[38;5;34m'+'|'+reset,end='')
        if 'a' not in goods:
          goods.append('a')
          goods.append('q')
      else:
        print(colorchoice+'\033[38;5;1m'+'|'+reset,end='')
        if 'a' in goods:
          goods.remove('a')
          goods.remove('q')
    elif i=="┓" or i in triggers:
      print(" ",end='')
    elif i=='W' or i=='Y' or i=='R' or i=='L' or i=='d' or i==':':
      print(colorchoice+i.upper()+reset,end="")
    elif i=='1' or i=='A':
      print(bright_white+" "+reset,end="")
    elif i=='4' or i=='D':
      print(purple+" "+reset,end="")
    elif i=='S':
      print('\033[38;5;1m'+"∆"+reset,end="")
    elif i=='#':
      print('\033[38;5;1m'+colorchoice+"∆"+reset,end="")
    elif i=="2" or i=='B':
      print(bright_blue+" "+reset,end="")
    elif i=="3" or i=='C':
      print(bright_green+" "+reset,end="")
    else:
      print(i,end="")
  if secrets!=0:
    print('\t\t\t\t\t\t\t\t Secrets: '+str(secrets))
mazeq=stuff[z] 
mazeq_2=mazeq.copy()
sped1=time.time()
while True:
  UPME()
  if randomstuff==True:
    colorchoice=colordict[random.randint(1,15)]
    colorchoice2=colordict[random.randint(1,15)]
  box1=int(mazeq.index('┌'))
  box2=int(mazeq.index('┐'))
  box3=int(mazeq.index('└'))
  box4=int(mazeq.index('┘'))
  keyz=getkey()
  if keyz=='h':
    printhint()
  if keyz=='w' or keyz==UP:
    move('up')
  if keyz=='a' or keyz==LEFT:
    move('left')
  if keyz=='s' or keyz==DOWN:
    move('down')
  if keyz=='d' or keyz==RIGHT:
    move("right")
  if keyz=='z':
    if 'y' in input("Do you want to exit?\n>").lower():
      break
    C("")
  if keyz=='r':
    j=True
    goback()
    mazeq=mazeq_2.copy()
    randomstuff=not randomstuff
  if keyz=='e': #Yes testing
    if 'sam' in name or name in ['Muffinlavania','squidcoder']:
      nextlevel()
  if oooG==True:
    oooG=False
    for i in chartindes[z]:
      mazeq[i]='a'
  
