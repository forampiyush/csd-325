"""Forest Fire Sim, modified by Sue Sampson, based on a program by Al Sweigart
A simulation of wildfires spreading in a forest. Press Ctrl-C to stop.
Inspired by Nicky Case's Emoji Sim http://ncase.me/simulating/model/
** use spaces, not indentation to modify **
Tags: short, bext, simulation
"""

import random
import sys
import time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Set up the constants:
WIDTH = 79
HEIGHT = 22

TREE = 'A'
FIRE = '@'
EMPTY = ' '
WATER = '~'   # Module 6: Water feature

# Try changing these settings to anything between 0.0 and 1.0:
INITIAL_TREE_DENSITY = 0.20
GROW_CHANCE = 0.01
FIRE_CHANCE = 0.01

# Pause between simulation steps
PAUSE_LENGTH = 0.5


def main():
    forest = createNewForest()
    bext.clear()

    while True:
        displayForest(forest)

        nextForest = {
            'width': forest['width'],
            'height': forest['height']
        }

        for x in range(forest['width']):
            for y in range(forest['height']):

                if (x, y) in nextForest:
                    continue

                # Module 6: Water never changes
                if forest[(x, y)] == WATER:
                    nextForest[(x, y)] = WATER

                elif (forest[(x, y)] == EMPTY and
                      random.random() <= GROW_CHANCE):
                    nextForest[(x, y)] = TREE

                elif (forest[(x, y)] == TREE and
                      random.random() <= FIRE_CHANCE):
                    nextForest[(x, y)] = FIRE

                elif forest[(x, y)] == FIRE:
                    # Spread fire only to trees
                    for ix in range(-1, 2):
                        for iy in range(-1, 2):
                            if forest.get((x + ix, y + iy)) == TREE:
                                nextForest[(x + ix, y + iy)] = FIRE

                    nextForest[(x, y)] = EMPTY

                else:
                    nextForest[(x, y)] = forest[(x, y)]

        forest = nextForest
        time.sleep(PAUSE_LENGTH)


def createNewForest():
    """Returns a dictionary for a new forest data structure."""

    forest = {
        'width': WIDTH,
        'height': HEIGHT
    }

    for x in range(WIDTH):
        for y in range(HEIGHT):

            # Module 6: Create a lake near the center
            if 30 <= x <= 48 and 8 <= y <= 14:
                forest[(x, y)] = WATER

            elif (random.random() * 100) <= INITIAL_TREE_DENSITY:
                forest[(x, y)] = TREE

            else:
                forest[(x, y)] = EMPTY

    return forest


def displayForest(forest):
    """Display the forest."""

    bext.goto(0, 0)

    for y in range(forest['height']):
        for x in range(forest['width']):

            if forest[(x, y)] == TREE:
                bext.fg('green')
                print(TREE, end='')

            elif forest[(x, y)] == FIRE:
                bext.fg('red')
                print(FIRE, end='')

            elif forest[(x, y)] == WATER:
                bext.fg('blue')
                print(WATER, end='')

            else:
                print(EMPTY, end='')

        print()

    bext.fg('reset')
    print('Grow chance: {}%  '.format(GROW_CHANCE * 100), end='')
    print('Lightning chance: {}%  '.format(FIRE_CHANCE * 100), end='')
    print('Press Ctrl-C to quit.')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()