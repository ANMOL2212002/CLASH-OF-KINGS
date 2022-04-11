from curses.textpad import rectangle
from constants import *
import math
from collision import *

class Troop:
    def __init__(self, x, y, health, char, damage, width, height, color, fcolor):
        self.x = x
        self.y = y
        self.health = health
        self.max_health = health
        self.damage = damage
        self.color = color
        self.destroyed = False
        self.char = char
        self.fcolor = fcolor
        self.width = width
        self.height = height
        self.move_speed = 1

    def render(self, game_board):

        style = Style.BRIGHT
        if self.health * 100 / self.max_health > 50:
            style = Style.BRIGHT

        elif self.health * 100 / self.max_health > 20:
            style = Style.NORMAL
        else:
            style = Style.DIM

        game_board[self.y][self.x] = style + \
            self.fcolor + self.char + Style.RESET_ALL

    def collide(self, building):
        if self.destroyed == False and building.destroyed == False:
            return Check_Collision.check_two_rectangles_collision(self.x-self.width+1, self.y-self.height+1, self.width, self.height, building.x-building.width+1, building.y-building.height+1, building.width, building.height)
        else:
            return False

    def attack(self, target):
        target.health -= self.damage
        if target.health <= 0:
            target.destroyed = True
            target.health = 0

    def reset_col(self):
        self.color = WHITE


class King(Troop):
    def __init__(self, x, y):
        K = 'K'
        super().__init__(x, y, Health_K, K, Damage_K, Width_K, Height_K, WHITE, FMAGENTA)
        self.vx = 1
        self.vy = 1
        self.radius_attack = Radius_Attack_K

    def move(self, key, buildings):
        for i in range(self.move_speed):
            if self.destroyed == False:
                if key == 'w':
                    self.y -= self.vy
                    if self.y < 0:
                        self.y = 0
                    for building in buildings:
                        if self.collide(building) == True:
                            self.y += self.vy
                elif key == 'a':
                    self.x -= self.vx
                    if self.x < 0:
                        self.x = 0
                    for building in buildings:
                        if self.collide(building) == True:
                            self.x += self.vx
                elif key == 's':
                    self.y += self.vy
                    if self.y > ROWS-1:
                        self.y = ROWS-1
                    for building in buildings:
                        if self.collide(building) == True:
                            self.y -= self.vy
                elif key == 'd':
                    self.x += self.vx
                    if self.x > COLS-1:
                        self.x = COLS-1
                    for building in buildings:
                        if self.collide(building) == True:
                            self.x -= self.vx

    def attack1(self, building):
        if self.destroyed == False:
            if self.x < COLS-1:
                if Check_Collision.check_two_rectangles_collision(self.x-self.width+2, self.y-self.height+1, self.width, self.height, building.x-building.width+1, building.y-building.height+1, building.width, building.height) == True:
                    if building.destroyed == False:
                        building.health -= self.damage
                        if building.health <= 0:
                            building.destroyed = True
                            building.health = 0

    def attack2(self, building):
        if self.destroyed == False:
            if Check_Collision.collision_rectangle_circle(building.x-building.width+1, building.y-building.height+1, building.width, building.height, self.x-self.width+1, self.y-self.height+1, self.radius_attack) == True:
                if building.destroyed == False:
                    building.health -= self.damage
                    if building.health <= 0:
                        building.destroyed = True
                        building.health = 0


class Barbarian(Troop):
    def __init__(self, x, y):
        B = 'B'
        super().__init__(x, y, Health_B, B, Damage_B, Width_B, Height_B, WHITE, FMAGENTA)
        self.vx = 1
        self.vy = 1

    def collide(self, buildings):
        if self.destroyed == False:
            for building in buildings:
                if building.destroyed == False:
                    if Check_Collision.check_two_rectangles_collision(self.x-self.width+1, self.y-self.height+1, self.width, self.height, building.x-building.width+1, building.y-building.height+1, building.width, building.height) == True:
                        self.attack(building)
                        return True
            return False
        else:
            return False

    def move(self, nonwall_list, buildings):
        for i in range(self.move_speed):
            if self.destroyed == False:
                old_dis = 1000
                pt_x = 0
                pt_y = 0
                for nonwall in nonwall_list:
                    if nonwall.destroyed == False:
                        for i in range(nonwall.height):
                            for j in range(nonwall.width):
                                new_dis = abs(self.x-(nonwall.x-j)) + \
                                    abs(self.y-(nonwall.y-i))
                                if new_dis < old_dis:
                                    old_dis = new_dis
                                    pt_x = nonwall.x-j
                                    pt_y = nonwall.y-i
                if pt_x > self.x:
                    self.x += self.vx
                    if self.x > COLS-1:
                        self.x = COLS-1
                    if self.collide(buildings) == True:
                        self.x -= self.vx
                elif pt_x < self.x:
                    self.x -= self.vx
                    if self.x < 0:
                        self.x = 0
                    if self.collide(buildings) == True:
                        self.x += self.vx
                if pt_y > self.y:
                    self.y += self.vy
                    if self.y > ROWS-1:
                        self.y = ROWS-1
                    if self.collide(buildings) == True:
                        self.y -= self.vy
                elif pt_y < self.y:
                    self.y -= self.vy
                    if self.y < 0:
                        self.y = 0
                    if self.collide(buildings) == True:
                        self.y += self.vy



