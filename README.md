
# Assignment 3.1

## To run the game:

run command :

`python3 game.py`

## Commands:

`1` - spawns Barbarian at position 1

`2` - spawns Barbarian at position 2

`3` - spawns Barbarian at position 3

`4` - spawns King at position 1

`5` - spawns King at position 2

`6` - spawns King at position 3

`h` - heal spell

`r` - rage spell

`w` - upward movement of king

`s` - downward movement of king

`a` - leftward movement of king

`d` - rightward movement of king

`' '` (space) - attack by king on its right block

`enter` - Area of Effect) attack by king in radius 5

`q` - quits the game

## File structure

-  `game.py` :contains main function which runs the loop and asks if the user wants to replay game or play game


- `play.py` : This contains the game class which calls other classes , helps play/replay game and renders the game

- `building.py` : - parent: Building class
                  - Townhall class
                  - Hut class
                  - Cannon class
                  - Wall class

- `troop.py` : - parent: Troop class
               - King class
               - Barbarian class

- `constants.py` : constants declaration

- `spell.py` : contains Spell class
                - handles heal and rage spell

- `input.py` : input hanlding

- `collision` : contains functions for checking general collisions
            - check_two_rectangles_collision
            - collision_rectangle_circle

## Rules and features:

○ Victory: All buildings (excluding walls) have been destroyed.

○ Defeat: All troops and the King have died without destroying all buildings.

○ Can span any number of barbarians and only 1 king.

○ Can use rage spell and heal spell any number of times.

○ 4 cannons, 5 huts , 1 townhall.

