import os
import random
import numpy as np
from termcolor import colored
import time

cube = [
    [['Y', 'Y', 'Y'],
     ['Y', 'Y', 'Y'],
     ['Y', 'Y', 'Y']],
    [['B', 'B', 'B'],
     ['B', 'B', 'B'],
     ['B', 'B', 'B']],
    [['R', 'R', 'R'],
     ['R', 'R', 'R'],
     ['R', 'R', 'R']],
    [['G', 'G', 'G'],
     ['G', 'G', 'G'],
     ['G', 'G', 'G']],
    [['O', 'O', 'O'],
     ['O', 'O', 'O'],
     ['O', 'O', 'O']],
    [['W', 'W', 'W'],
     ['W', 'W', 'W'],
     ['W', 'W', 'W']],
    ]
moves = ["R", "R2", "L", "L2", "U", "U2", "D", "D2", "F", "F2", "B", "B2"]

def print_cube():
    os.system("clear")
    for i in cube[0]:
        print("        ", end="")
        for j in i:
            print(j, end=" ")
        print()
    print()
    for j in range(3):
        for i in range(4):
            print(" ", end="")
            for k in range(3):
                print(cube[1+i][j][k], end=' ')
        print()
    print()
    for i in cube[5]:
        print("        ", end="")
        for j in i:
            print(j, end=" ")
        print()
    print()

def print_help():
    print("To turn the cube, you type in the 3x3 notation the turn you want")
    print("It's also possible to do multiple turns within a single input by separating the moves by spaces")
    print("Like so: `R U R' U'`")
    print("To scramble the cube type in `scramble`")
    input("Press enter to continue: ")

def clockwise_movement(face):
    # edge movement
    cube[face][0][1], cube[face][1][2] = cube[face][1][2], cube[face][0][1]
    cube[face][0][1], cube[face][2][1] = cube[face][2][1], cube[face][0][1]
    cube[face][0][1], cube[face][1][0] = cube[face][1][0], cube[face][0][1]
    # corner movement
    cube[face][0][2], cube[face][2][2] = cube[face][2][2], cube[face][0][2]
    cube[face][0][2], cube[face][2][0] = cube[face][2][0], cube[face][0][2]
    cube[face][0][2], cube[face][0][0] = cube[face][0][0], cube[face][0][2]

def counterclockwise_movement(face):
    # edge movement
    cube[face][0][1], cube[face][1][2] = cube[face][1][2], cube[face][0][1]
    cube[face][1][2], cube[face][1][0] = cube[face][1][0], cube[face][1][2]
    cube[face][1][2], cube[face][2][1] = cube[face][2][1], cube[face][1][2]
    # corner movement
    cube[face][0][0], cube[face][0][2] = cube[face][0][2], cube[face][0][0]
    cube[face][0][2], cube[face][2][0] = cube[face][2][0], cube[face][0][2]
    cube[face][0][2], cube[face][2][2] = cube[face][2][2], cube[face][0][2]

def move_U():
    cube[1][0], cube[2][0], cube[3][0], cube[4][0] = cube[2][0], cube[3][0], cube[4][0], cube[1][0]
    clockwise_movement(0)

def move_U_prime():
    cube[2][0], cube[3][0], cube[4][0], cube[1][0] = cube[1][0], cube[2][0], cube[3][0], cube[4][0]
    counterclockwise_movement(0)

def move_E():
    cube[2][1], cube[3][1], cube[4][1], cube[1][1] = cube[1][1], cube[2][1], cube[3][1], cube[4][1]

def move_E_prime():
    cube[1][1], cube[2][1], cube[3][1], cube[4][1] = cube[2][1], cube[3][1], cube[4][1], cube[1][1]

def move_D():
    cube[2][2], cube[3][2], cube[4][2], cube[1][2] = cube[1][2], cube[2][2], cube[3][2], cube[4][2]
    clockwise_movement(5)

def move_D_prime():
    cube[1][2], cube[2][2], cube[3][2], cube[4][2] = cube[2][2], cube[3][2], cube[4][2], cube[1][2]
    counterclockwise_movement(5)

def move_R():
    cube[0][0][2], cube[4][2][0], cube[5][0][2], cube[2][0][2] = cube[2][0][2], cube[0][0][2], cube[4][2][0], cube[5][0][2]
    cube[0][1][2], cube[4][1][0], cube[5][1][2], cube[2][1][2] = cube[2][1][2], cube[0][1][2], cube[4][1][0], cube[5][1][2]
    cube[0][2][2], cube[4][0][0], cube[5][2][2], cube[2][2][2] = cube[2][2][2], cube[0][2][2], cube[4][0][0], cube[5][2][2]
    clockwise_movement(3)

def move_R_prime():
    cube[0][0][2], cube[4][2][0], cube[5][0][2], cube[2][0][2] = cube[4][2][0], cube[5][0][2], cube[2][0][2], cube[0][0][2]
    cube[0][1][2], cube[4][1][0], cube[5][1][2], cube[2][1][2] = cube[4][1][0], cube[5][1][2], cube[2][1][2], cube[0][1][2]
    cube[0][2][2], cube[4][0][0], cube[5][2][2], cube[2][2][2] = cube[4][0][0], cube[5][2][2], cube[2][2][2], cube[0][2][2]
    counterclockwise_movement(3)

def move_M():
    cube[0][0][1], cube[4][2][1], cube[5][0][1], cube[2][0][1] = cube[4][2][1], cube[5][0][1], cube[2][0][1], cube[0][0][1]
    cube[0][1][1], cube[4][1][1], cube[5][1][1], cube[2][1][1] = cube[4][1][1], cube[5][1][1], cube[2][1][1], cube[0][1][1]
    cube[0][2][1], cube[4][0][1], cube[5][2][1], cube[2][2][1] = cube[4][0][1], cube[5][2][1], cube[2][2][1], cube[0][2][1]

def move_M_prime():
    cube[0][0][1], cube[4][2][1], cube[5][0][1], cube[2][0][1] = cube[2][0][1], cube[0][0][1], cube[4][2][1], cube[5][0][1]
    cube[0][1][1], cube[4][1][1], cube[5][1][1], cube[2][1][1] = cube[2][1][1], cube[0][1][1], cube[4][1][1], cube[5][1][1]
    cube[0][2][1], cube[4][0][1], cube[5][2][1], cube[2][2][1] = cube[2][2][1], cube[0][2][1], cube[4][0][1], cube[5][2][1]

def move_L():
    cube[0][0][0], cube[4][2][2], cube[5][0][0], cube[2][0][0] = cube[4][2][2], cube[5][0][0], cube[2][0][0], cube[0][0][0]
    cube[0][1][0], cube[4][1][2], cube[5][1][0], cube[2][1][0] = cube[4][1][2], cube[5][1][0], cube[2][1][0], cube[0][1][0]
    cube[0][2][0], cube[4][0][2], cube[5][2][0], cube[2][2][0] = cube[4][0][2], cube[5][2][0], cube[2][2][0], cube[0][2][0]
    clockwise_movement(1)

def move_L_prime():
    cube[0][0][0], cube[4][2][2], cube[5][0][0], cube[2][0][0] = cube[2][0][0], cube[0][0][0], cube[4][2][2], cube[5][0][0]
    cube[0][1][0], cube[4][1][2], cube[5][1][0], cube[2][1][0] = cube[2][1][0], cube[0][1][0], cube[4][1][2], cube[5][1][0]
    cube[0][2][0], cube[4][0][2], cube[5][2][0], cube[2][2][0] = cube[2][2][0], cube[0][2][0], cube[4][0][2], cube[5][2][0]
    counterclockwise_movement(1)

def move_F():
    cube[0][2][2], cube[3][2][0], cube[5][0][0], cube[1][0][2] = cube[1][0][2], cube[0][2][2], cube[3][2][0], cube[5][0][0]
    cube[0][2][1], cube[3][1][0], cube[5][0][1], cube[1][1][2] = cube[1][1][2], cube[0][2][1], cube[3][1][0], cube[5][0][1]
    cube[0][2][0], cube[3][0][0], cube[5][0][2], cube[1][2][2] = cube[1][2][2], cube[0][2][0], cube[3][0][0], cube[5][0][2]
    clockwise_movement(2)

def move_F_prime():
    cube[0][2][2], cube[3][2][0], cube[5][0][0], cube[1][0][2] = cube[3][2][0], cube[5][0][0], cube[1][0][2], cube[0][2][2]
    cube[0][2][1], cube[3][1][0], cube[5][0][1], cube[1][1][2] = cube[3][1][0], cube[5][0][1], cube[1][1][2], cube[0][2][1]
    cube[0][2][0], cube[3][0][0], cube[5][0][2], cube[1][2][2] = cube[3][0][0], cube[5][0][2], cube[1][2][2], cube[0][2][0]
    counterclockwise_movement(2)

def move_S():
    cube[0][1][2], cube[3][2][1], cube[5][1][0], cube[1][0][1] = cube[1][0][1], cube[0][1][2], cube[3][2][1], cube[5][1][0]
    cube[0][1][1], cube[3][1][1], cube[5][1][1], cube[1][1][1] = cube[1][1][1], cube[0][1][1], cube[3][1][1], cube[5][1][1]
    cube[0][1][0], cube[3][0][1], cube[5][1][2], cube[1][2][1] = cube[1][2][1], cube[0][1][0], cube[3][0][1], cube[5][1][2]
    clockwise_movement(2)

def move_S_prime():
    cube[0][1][2], cube[3][2][1], cube[5][1][0], cube[1][0][1] = cube[3][2][1], cube[5][1][0], cube[1][0][1], cube[0][1][2]
    cube[0][1][1], cube[3][1][1], cube[5][1][1], cube[1][1][1] = cube[3][1][1], cube[5][1][1], cube[1][1][1], cube[0][1][1]
    cube[0][1][0], cube[3][0][1], cube[5][1][2], cube[1][2][1] = cube[3][0][1], cube[5][1][2], cube[1][2][1], cube[0][1][0]
    counterclockwise_movement(2)

def move_B():
    cube[0][0][2], cube[3][2][2], cube[5][2][0], cube[1][0][0] = cube[3][2][2], cube[5][2][0], cube[1][0][0], cube[0][0][2]
    cube[0][0][1], cube[3][1][2], cube[5][2][1], cube[1][1][0] = cube[3][1][2], cube[5][2][1], cube[1][1][0], cube[0][0][1]
    cube[0][0][0], cube[3][0][2], cube[5][2][2], cube[1][2][0] = cube[3][0][2], cube[5][2][2], cube[1][2][0], cube[0][0][0]
    clockwise_movement(4)

def move_B_prime():
    cube[0][0][2], cube[3][2][2], cube[5][2][0], cube[1][0][0] = cube[1][0][0], cube[0][0][2], cube[3][2][2], cube[5][2][0]
    cube[0][0][1], cube[3][1][2], cube[5][2][1], cube[1][1][0] = cube[1][1][0], cube[0][0][1], cube[3][1][2], cube[5][2][1]
    cube[0][0][0], cube[3][0][2], cube[5][2][2], cube[1][2][0] = cube[1][2][0], cube[0][0][0], cube[3][0][2], cube[5][2][2]
    counterclockwise_movement(4)

def move_x():
    cube[0], cube[2], cube[5], cube[4] = cube[2], cube[5], cube[4], cube[0]
    clockwise_movement(3)
    counterclockwise_movement(1)

def move_x_prime():
    cube[0], cube[2], cube[5], cube[4] = cube[4], cube[0], cube[2], cube[5]
    clockwise_movement(0)
    clockwise_movement(0)
    clockwise_movement(4)
    clockwise_movement(4)
    clockwise_movement(1)
    counterclockwise_movement(3)

def move_y():
    cube[1], cube[2], cube[3], cube[4] = cube[2], cube[3], cube[4], cube[1]
    clockwise_movement(0)
    counterclockwise_movement(5)

def move_y_prime():
    cube[1], cube[2], cube[3], cube[4] = cube[4], cube[1], cube[2], cube[3]
    clockwise_movement(5)
    counterclockwise_movement(0)

def scramble():
    scramble_algorithm = []
    for i in range(30):
        scramble_algorithm.append(random.choice(moves))
    move_cube(scramble_algorithm)

def move_cube(sheet):
    for move in sheet:
        if move == "U": move_U()
        elif move == "U'": move_U_prime()
        elif move == "U2":
            move_U()
            move_U()
        elif move == "E": move_E()
        elif move == "E'": move_E_prime()
        elif move == 'E2':
            move_E()
            move_E()
        elif move == "D": move_D()
        elif move == "D'": move_D_prime()
        elif move == "D2":
            move_D()
            move_D()
        elif move == "R": move_R()
        elif move == "R'": move_R_prime()
        elif move == "R2":
            move_R()
            move_R()
        elif move == "M": move_M()
        elif move == "M'": move_M_prime()
        elif move == "M2":
            move_M()
            move_M()
        elif move == "L": move_L()
        elif move == "L'": move_L_prime()
        elif move == "L2":
            move_L()
            move_L()
        elif move == "F": move_F()
        elif move == "F'": move_F_prime()
        elif move == "F2":
            move_F()
            move_F()
        elif move == "S": move_S()
        elif move == "S'": move_S_prime()
        elif move == "S2":
            move_S()
            move_S()
        elif move == "B": move_B()
        elif move == "B'": move_B_prime()
        elif move == "B2":
            move_B()
            move_B()
        elif move == "Uw" or move == "u":
            move_U()
            move_E_prime()
        elif move == "Uw'" or move == "u'":
            move_U_prime()
            move_E()
        elif move == "Dw" or move == "d":
            move_D()
            move_E()
        elif move == "Dw'" or move == "d'":
            move_D_prime()
            move_E_prime()
        elif move == "Lw" or move == "l":
            move_L()
            move_M()
        elif move == "Lw'" or move == "l'":
            move_L_prime()
            move_M_prime()
        elif move == "Rw" or move == "r":
            move_R()
            move_M_prime()
        elif move == "Rw'" or move == "r'":
            move_R_prime()
            move_M()
        elif move == "Fw" or move == "f":
            move_F()
            move_S()
        elif move == "Fw'" or move == "f'":
            move_F_prime()
            move_S_prime()
        elif move == "Bw" or move == "b":
            move_B()
            move_S_Prime()
        elif move == "Bw'" or move == "b'":
            move_B_prime()
            move_S()
        elif move == "x": move_x()
        elif move == "x'": move_x_prime()
        elif move == "x2":
            move_x()
            move_x()
        elif move == "y": move_y()
        elif move == "y'": move_y_prime()
        elif move == "y2":
            move_y()
            move_y()

while True:
    print_cube()
    move_list = input("Type in the move: ").split(" ")
    if move_list[0] == "scramble": scramble()
    elif move_list[0] == "help": print_help()
    else: move_cube(move_list)
