"""
------------------------------------------
CSC 310/392 Game of life
File: life.py
Author: Gabe Le
Due: 11 February 2018

This program plays Conway's "Game of Life" which can be found
here: https://en.wikipedia.org/wiki/Conway's_Game_of_Life

The program will stop when the board stops changing or the number of
generations is reached
------------------------------------------
"""
import os
import time
import random
import copy
from itertools import product

# Prints out the game board in a nice to read format
def display_array(ar):
    os.system('clear')
    rows = len(ar)

    if(rows == 0):
        raise ValueError("Array contains no value")

    cols = len(ar[0])

    for i in range(rows):
        for j in range(cols):
            print(ar[i][j], end=' ')
        print()

    time.sleep(1)


# Makes a square board by filling it with random integers,
# then divides the random number by 2 to see if it should be
# empty of not to achieve a random layout
def generateBoard(size):
    ar = [[0]*size for x in range(size)]

    for rIndex, row in enumerate(ar):
        for cIndex, item in enumerate(row):
            num = random.randint(1, 101)
            if(num % 2 != 0):
                num = '*'
            else:
                num = '-'
            ar[rIndex][cIndex] = num

    return ar


# Determines the neighbors of the current cell by using itertools.product
# and Python's * operator and yield expression
def checkNeighbor(cell, size):
    for c in product(*(range(n - 1, n + 2) for n in cell)):
        if c != cell and all(0 <= n < size for n in c):
            yield c


# Changes the index to its respective value according to the logic
# of the Game of Life
def changeIndex(neighbors, gameBoard, row, col):
    # we will keep track of how many neighbors are alive and if the current cell is alive
    onNeighbors = 0
    alive = False
    if(gameBoard[row][col] == '*'):
        alive = True

    for i,j in neighbors:
        if(gameBoard[i][j] == '*'):
            onNeighbors += 1

    # if the location is alive and it has less than 2 neighbors that are on, it dies
    if((alive) and (onNeighbors < 2)):
        gameBoard[row][col] = '-'
    # if the location is alive and the number of neighbors that are on is 2 or 3, it stays the same
    elif((alive) and ((onNeighbors == 2) or (onNeighbors == 3))):
        gameBoard[row][col] = '*'
    # if the location is alive and the number of neighbors that are alive is greater than 3, it dies
    elif((alive) and (onNeighbors > 3)):
        gameBoard[row][col] = '-'
    # if the location is dead and the number of neighbors that are alive is 3, it becomes alive
    elif((not alive) and (onNeighbors == 3)):
        gameBoard[row][col] = '*'


# main function runs the game and prompts for the size and generation
# then it plays the game
def main():
    print('-----------------------------------------')
    print('*****************************************')
    print('---------- The Game of Life -------------')
    print('*****************************************')
    print('-----------------------------------------\n')
    # make sure the user gives a valid value
    while(True):
        try:
            size = int(input('Enter the size of the board: '))
            if(size < 2 or size > 100):
                print('Please enter a number between 2 and 100')
            else:
                break
        except ValueError:
            print('Please enter a valid number')

    gameBoard = generateBoard(size)
    print('\nHere is your Game Board -->')
    display_array(gameBoard)
    print()

    # asks the user to run the game for how many generations they want
    while(True):
        try:
            generation = int(input('Please enter how many generations you want to run: '))
            if (generation < 0):
                print("Please enter a number that's greater than 0")
            else:
                break
        except ValueError:
            print('Please enter a valid generation')

    counter = 0
    # Play the Game of Life
    while(counter < generation):
        # we will keep a copy of the previous board to quit when it stops changing
        oldGameboard = copy.deepcopy(gameBoard)
        for row in range(len(gameBoard)):
            for col in range(len(gameBoard)):
                neighbors = list(checkNeighbor((row, col), size))
                changeIndex(neighbors, gameBoard, row, col)
        # display the updated game board after changing it once each generation
        print('\nGeneration ', counter + 1)
        counter += 1
        display_array(gameBoard)
        if(oldGameboard == gameBoard):
            break

    print('\nThe game is over, thanks for playing')

main()