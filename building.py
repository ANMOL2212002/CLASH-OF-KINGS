
from constants import *
from troop import *
from collision import *

class Building:
    def __init__(self, x, y, width, height, health, char):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = health
        self.max_health = health
        self.damage = 0
        self.color = GREEN
        self.destroyed = False
        self.char = char
        #self.fcolor = FWHITE
        self.bit = 0

    def render(self, game_board):
        if self.destroyed == False:
            if self.health * 100 / self.max_health > 50:
                self.color = GREEN
            elif self.health * 100 / self.max_health > 20:
                self.color = YELLOW
            else:
                self.color = RED
            if self.bit == 1:
                self.color += Fore.BLACK
                self.bit = 0
            for i in range(self.height):
                for j in range(self.width):
                    game_board[self.y-i][self.x-j] = self.color + self.char + Style.RESET_ALL


class TownHall(Building):
    def __init__(self, x, y):
        T = 'T'
        super().__init__(x, y, Width_T, Height_T, Health_T,T)

class Hut(Building):
    def __init__(self, x, y):
        H = 'H'
        super().__init__(x, y, Width_H, Height_H, Health_H,H)


class Wall(Building):
    def __init__(self, x, y):
        W = 'W'
        super().__init__(x, y, Width_W, Height_W, Health_W,W)


class Cannon(Building):
    def __init__(self, x, y):
        C = 'C'
        super().__init__(x, y, Width_C, Height_C, Health_C,C)
        self.range = RANGE
        self.istarget = False
        self.damage = Damage_C

    def attack(self, target):
        if self.destroyed == False:
            if self.istarget == False:
                if target.destroyed == False and Check_Collision.collision_rectangle_circle(target.x-target.width+1, target.y-target.height+1, target.width, target.height, self.x, self.y, self.range):
                    self.istarget = True
                    #self.fcolor = FBLUE

            if self.istarget == True:
                if target.destroyed == True or Check_Collision.collision_rectangle_circle(target.x-target.width+1, target.y-target.height+1, target.width, target.height, self.x, self.y, self.range)==False:
                    self.istarget = False
                    #self.fcolor = FWHITE

                else:
                    self.bit = 1
                    target.health -= self.damage
                    if target.health <= 0:
                        target.destroyed = True
                        target.health = 0
                    
        else:
            self.istarget = False




        
