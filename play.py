import sys
import os
import math
import time
import copy

sys.path.append
from input import Input
from constants import *
from colorama import Fore, Back, Style
from building import *
from troop import *
#from input import input_to

from spell import *


class Game():
    def __init__(self):
        self.cols = COLS
        self.rows = ROWS
        self.status = "playing"
        self.timeOut = 0.3
        self.check_king = False
        self.mode = "play"

        self.townhall = TownHall(TOWN_X, TOWN_Y)

        self.huts = []
        for i in range(len(HUT_ROWS)):
            self.huts.append(Hut(HUT_COLS[i], HUT_ROWS[i]))

        self.walls = []
        for i in range(len(WALL_ROWS)):
            self.walls.append(Wall(WALL_COLS[i], WALL_ROWS[i]))

        self.cannons = []
        for i in range(len(CANNON_ROWS)):
            self.cannons.append(Cannon(CANNON_COLS[i], CANNON_ROWS[i]))

        self.king = King(KING_X, KING_Y)
        self.barbarian = []
        self.frames = []
        self.iterate = 0

    def play(self):

        input = Input()
        Buildings = []
        Troops = []
        Non_wall = []

        Buildings.append(self.townhall)
        Non_wall.append(self.townhall)
        for hut in self.huts:
            Buildings.append(hut)
            Non_wall.append(hut)
        for wall in self.walls:
            Buildings.append(wall)
        for cannon in self.cannons:
            Buildings.append(cannon)
            Non_wall.append(cannon)

        if(self.check_king):
            Troops.append(self.king)

        for barbarian in self.barbarian:
            Troops.append(barbarian)
        if self.iterate % 4 == 0:
            for cannon in self.cannons:
                for troop in Troops:
                    cannon.attack(troop)

        for barbarian in self.barbarian:
            barbarian.move(Non_wall, Buildings)

        self.render()

        if self.mode == "play":
            key = input.get_parsed_input(self.timeOut)
            self.frames.append(key)
        else:
            key = self.frames[self.iterate]
            time.sleep(self.timeOut)
        
        if key == 'q':
            sys.exit()
        elif key == 'w' or key == 'a' or key == 's' or key == 'd':
            if self.check_king:
                self.king.move(key, Buildings)
        elif key == '1' or key == '2' or key == '3':
            self.spawn_bar(key)
        elif key == '4' or key == '5' or key == '6':
            if self.check_king == False:
                self.spawn_king(key)
                self.check_king = True

        elif key == ' ':
            if self.check_king:
                for building in Buildings:
                    self.king.attack1(building)
        elif key == 'enter':
            if self.check_king:
                for building in Buildings:
                    self.king.attack2(building)
        elif key == 'h':
            Spell.spell(1.5, 1, Troops)
        elif key == 'r':
            Spell.spell(1, 2, Troops)

        num = len(Troops)
        for i in range(num):
            if Troops[i].destroyed == False:
                break
            elif i == len(Troops)-1:
                self.status = "lose"

        num = len(Non_wall)
        for i in range(num):
            if Non_wall[i].destroyed == False:
                break
            elif i == len(Non_wall)-1:
                self.status = "win"
        self.iterate += 1

    def render_health(self):
        print("King's Health: ", end="")
        print(str(self.king.health) + '/' +
              str(self.king.max_health), end='\n')
        print('Health Bar: ', end="")
        dash = int((self.king.health * 100) / self.king.max_health)
        print('|' + '-'*dash + ' '*(100-dash) + '|', end='\n')

    def render(self):
        game_board = []
        for i in range(self.rows):
            row = [' ']*self.cols
            row.append('\n')
            game_board.append(row)

        Building.render(self.townhall, game_board)

        for hut in self.huts:
            Building.render(hut, game_board)

        for wall in self.walls:
            Building.render(wall, game_board)

        for cannon in self.cannons:
            Building.render(cannon, game_board)

        if self.check_king:
            Troop.render(self.king, game_board)

        for barbarian in self.barbarian:
            Barbarian.render(barbarian, game_board)

        for row in game_board:
            for j in row:
                print(j, end="")

        if self.check_king:
            self.render_health()

    def spawn_bar(self, key):
        if key == '1':
            self.barbarian.append(
                Barbarian(SPAWNING_COLS[0], SPAWNING_ROWS[0]))
        elif key == '2':
            self.barbarian.append(
                Barbarian(SPAWNING_COLS[1], SPAWNING_ROWS[1]))
        elif key == '3':
            self.barbarian.append(
                Barbarian(SPAWNING_COLS[2], SPAWNING_ROWS[2]))

    def spawn_king(self, key):
        if key == '4':
            self.king.x = SPAWNING_COLS[0]
            self.king.y = SPAWNING_ROWS[0]
        elif key == '5':
            self.king.x = SPAWNING_COLS[1]
            self.king.y = SPAWNING_ROWS[1]
        elif key == '6':
            self.king.x = SPAWNING_COLS[2]
            self.king.y = SPAWNING_ROWS[2]
