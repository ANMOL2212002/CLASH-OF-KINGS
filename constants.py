from colorama import Fore, Back, Style

GREEN = Back.GREEN
RED = Back.RED
YELLOW = Back.YELLOW
BLUE = Back.BLUE
MAGENTA = Back.MAGENTA
WHITE = Back.WHITE
BLACK = Back.BLACK

FGREEN = Fore.GREEN
FRED = Fore.RED
FYELLOW = Fore.YELLOW
FBLUE = Fore.BLUE
FMAGENTA = Fore.MAGENTA
FWHITE = Fore.WHITE
FBLACK = Fore.BLACK

ROWS = 40
COLS = 120

HUT_ROWS = [6,20,25,30,10] 
HUT_COLS = [30,80,30,90,100]
Height_H=2
Width_H=2
Health_H=30
       
TOWN_X = 60
TOWN_Y = 20
Height_T=4
Width_T=3
Health_T=100

CANNON_ROWS = [15,30,22,15]
CANNON_COLS = [10,80,65,55]
Height_C=1
Width_C=1
Health_C=50
RANGE=20
Damage_C = 4

WALL_ROWS = []
WALL_COLS = []

for i in range(Width_T+2):
    WALL_COLS.append(TOWN_X+1-i)
    WALL_ROWS.append(TOWN_Y+1)
    WALL_COLS.append(TOWN_X+1-i)
    WALL_ROWS.append(TOWN_Y-Height_T)

for i in range(Height_T):
    WALL_COLS.append(TOWN_X+1)
    WALL_ROWS.append(TOWN_Y-i)
    WALL_COLS.append(TOWN_X-Width_T)
    WALL_ROWS.append(TOWN_Y-i)

for i in range(COLS):
    WALL_COLS.append(i)
    WALL_ROWS.append(ROWS-1)
    WALL_COLS.append(i)
    WALL_ROWS.append(0)

for i in range(1,ROWS-1):
    WALL_COLS.append(0)
    WALL_ROWS.append(i)
    WALL_COLS.append(COLS-1)
    WALL_ROWS.append(i)

Height_W=1
Width_W=1
Health_W=20

KING_X= 10
KING_Y = 20
Health_K = 100
Damage_K = 6
Height_K = 1
Width_K = 1
Radius_Attack_K = 5

Health_B = 50
Damage_B = 2
Height_B = 1
Width_B = 1
SPAWNING_ROWS = [15,37,5]
SPAWNING_COLS = [5,38,115]