"""
Name: Foram
Date: 06/23/2026
Assignment: Module 3

Description:
Modified Cho-Han game.

Changes Made:
1. Changed input prompts to FD:
2. Changed house fee from 10% to 12%.
3. Added bonus notice to introduction.
4. Added a 10 mon bonus when the dice total equals 2 or 7.
"""

import random
import sys

JAPANESE_NUMBERS = {
    1: 'ICHI',
    2: 'NI',
    3: 'SAN',
    4: 'SHI',
    5: 'GO',
    6: 'ROKU'
}

print('''Cho-Han, by Al Sweigart al@inventwithpython.com

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.

BONUS: If the total of the dice roll equals 2 or 7,
the player receives a 10 mon bonus.
''')

purse = 5000

while True:  # Main game loop.

    # Place your bet:
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')

    while True:
        pot = input('FD: ')

        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        elif not pot.isdecimal():
            print('Please enter a number.')

        elif int(pot) > purse:
            print('You do not have enough to make that bet.')

        else:
            pot = int(pot)
            break

    # Roll the dice.
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')
    print()
    print('    CHO (even) or HAN (odd)?')

    # Let the player bet CHO or HAN:
    while True:
        bet = input('FD: ').upper()

        if bet != 'CHO' and bet != 'HAN':
            print('Please enter either "CHO" or "HAN".')
            continue
        else:
            break

    # Reveal the dice results:
    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)

    rollTotal = dice1 + dice2

    # Bonus rule
    if rollTotal == 2 or rollTotal == 7:
        print('Bonus! The dice total was', rollTotal)
        print('You receive a 10 mon bonus.')
        purse = purse + 10

    # Determine if the player won:
    rollIsEven = (rollTotal % 2 == 0)

    if rollIsEven:
        correctBet = 'CHO'
    else:
        correctBet = 'HAN'

    playerWon = (bet == correctBet)

    # Display the bet results:
    if playerWon:
        print('You won! You take', pot, 'mon.')
        purse = purse + pot

        houseFee = int(pot * 0.12)
        print('The house collects a', houseFee, 'mon fee.')
        purse = purse - houseFee

    else:
        purse = purse - pot
        print('You lost!')

    # Check if the player has run out of money:
    if purse == 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()