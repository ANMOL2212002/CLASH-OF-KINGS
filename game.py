import colorama
import sys
import os
import math
import time
import copy
from colorama import Fore, Back, Style
import pickle

from constants import *
from play import *

game = Game()

print("1. New Game : Enter 7")
print("2. Replay Game : Enter 8")
print("3. Exit : Enter 9")
inp = int(input("Enter your choice : "))

if inp == 7:
    game.mode = "play"
if inp == 8:
    file = input("Enter file which u want to play repaly for : ")
    with open(file, 'rb') as f:
        game.frames = pickle.load(f)
    game.mode = "replay"
if inp == 9:
    sys.exit()

while (game.status == "playing"):
    print("\033[H\033[J", end="")
    game.play()

if (game.status == "win"):
    print("\033[H\033[J", end="")
    print("You won!")

elif (game.status == "lose"):
    print("\033[H\033[J", end="")
    print("You lost!")
    print("Buildings destroyed:")
    print("Town Hall: " + str(game.townhall.destroyed))
    count = 0
    total = 0
    for hut in game.huts:
        if hut.destroyed == True:
            count += 1
        total += 1
    print("Huts: " + str(count) + "/" + str(total))

    count = 0
    total = 0
    for cannon in game.cannons:
        if cannon.destroyed == True:
            count += 1
        total += 1
    print("Cannons: " + str(count) + "/" + str(total))

if game.mode == "play":
    file = input("Enter the name of the file you want to save the game to : ")
    with open(file, 'wb') as f:
        pickle.dump(game.frames, f)
