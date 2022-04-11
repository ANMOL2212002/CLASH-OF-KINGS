from constants import *
from colorama import Fore, Back, Style
from building import *
from troop import *
from input import *


class Spell():
    def spell(heal,rage,troops):
        for troop in troops:
            if troop.destroyed == False:
                troop.health *= heal
                if troop.health > troop.max_health:
                    troop.health = troop.max_health
                troop.damage *= rage
                troop.move_speed *= rage



