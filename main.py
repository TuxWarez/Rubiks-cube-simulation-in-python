import os
import time

cube = [
    [[1, 1, 1],  # cube[0][0][x]
     [1, 1, 1],  # cube[0][1][x]
     [1, 1, 1]], # cube[0][2][x]
    [[2, 2, 2],  # cube[1][0][x]
     [2, 2, 2],  # cube[1][1][x]
     [2, 2, 2]], # cube[1][2][x]
    [[3, 3, 3],  # cube[2][0][x]
     [3, 3, 3],  # cube[2][1][x]
     [3, 3, 3]], # cube[2][2][x]
    [[4, 4, 4],  # cube[3][0][x]
     [4, 4, 4],  # cube[3][1][x]
     [4, 4, 4]], # cube[3][2][x]
    [[5, 5, 5],  # cube[4][0][x]
     [5, 5, 5],  # cube[4][1][x]
     [5, 5, 5]], # cube[4][2][x]
    [[6, 6, 6],  # cube[5][0][x]
     [6, 6, 6],  # cube[5][1][x]
     [6, 6, 6]], # cube[5][2][x]
    ]

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
    # rightmost layer movement
    cube[0][0][2], cube[0][1][2], cube[0][2][2], cube[2][0][2], cube[2][1][2], cube[2][2][2] = cube[2][0][2], cube[2][1][2], cube[2][2][2], cube[0][0][2], cube[0][1][2], cube[0][2][2]
    cube[4][0][0], cube[4][1][0], cube[4][2][0], cube[2][0][2], cube[2][1][2], cube[2][2][2] = cube[2][0][2], cube[2][1][2], cube[2][2][2], cube[4][0][0], cube[4][1][0], cube[4][2][0]
    cube[5][0][2], cube[5][1][2], cube[5][2][2], cube[2][0][2], cube[2][1][2], cube[2][2][2] = cube[2][0][2], cube[2][1][2], cube[2][2][2], cube[5][0][2], cube[5][1][2], cube[5][2][2]
    cube[4][0][0], cube[4][2][0] = cube[4][2][0], cube[4][0][0]
    cube[5][0][2], cube[5][2][2] = cube[5][2][2], cube[5][0][2]
    clockwise_movement(3)


def move_R_prime():
    cube[5][0][2], cube[5][1][2], cube[5][2][2], cube[2][0][2], cube[2][1][2], cube[2][2][2] = cube[2][0][2], cube[2][1][2], cube[2][2][2], cube[5][0][2], cube[5][1][2], cube[5][2][2]
    cube[4][0][0], cube[4][1][0], cube[4][2][0], cube[2][0][2], cube[2][1][2], cube[2][2][2] = cube[2][0][2], cube[2][1][2], cube[2][2][2], cube[4][0][0], cube[4][1][0], cube[4][2][0]
    cube[0][0][2], cube[0][1][2], cube[0][2][2], cube[2][0][2], cube[2][1][2], cube[2][2][2] = cube[2][0][2], cube[2][1][2], cube[2][2][2], cube[0][0][2], cube[0][1][2], cube[0][2][2]
    cube[0][0][2], cube[0][2][2] = cube[0][2][2], cube[0][0][2]
    cube[5][0][2], cube[5][2][2] = cube[5][2][2], cube[5][0][2]
    counterclockwise_movement(3)

def move_M():
    cube[0][0][1], cube[0][1][1], cube[0][2][1], cube[2][0][1], cube[2][1][1], cube[2][2][1] = cube[2][0][1], cube[2][1][1], cube[2][2][1], cube[0][0][1], cube[0][1][1], cube[0][2][1]
    cube[4][0][1], cube[4][1][1], cube[4][2][1], cube[2][0][1], cube[2][1][1], cube[2][2][1] = cube[2][0][1], cube[2][1][1], cube[2][2][1], cube[4][0][1], cube[4][1][1], cube[4][2][1]
    cube[5][0][1], cube[5][1][1], cube[5][2][1], cube[2][0][1], cube[2][1][1], cube[2][2][1] = cube[2][0][1], cube[2][1][1], cube[2][2][1], cube[5][0][1], cube[5][1][1], cube[5][2][1]
    cube[4][0][1], cube[4][2][1] = cube[4][2][1], cube[4][0][1]
    cube[5][0][1], cube[5][2][1] = cube[5][2][1], cube[5][0][1]

def move_L():
    cube[5][0][0], cube[5][1][0], cube[5][2][0], cube[2][0][0], cube[2][1][0], cube[2][2][0] = cube[2][0][0], cube[2][1][0], cube[2][2][0], cube[5][0][0], cube[5][1][0], cube[5][2][0]
    cube[4][0][2], cube[4][1][2], cube[4][2][2], cube[2][0][0], cube[2][1][0], cube[2][2][0] = cube[2][0][0], cube[2][1][0], cube[2][2][0], cube[4][0][2], cube[4][1][2], cube[4][2][2]
    cube[0][0][0], cube[0][1][0], cube[0][2][0], cube[2][0][0], cube[2][1][0], cube[2][2][0] = cube[2][0][0], cube[2][1][0], cube[2][2][0], cube[0][0][0], cube[0][1][0], cube[0][2][0]
    cube[0][0][0], cube[0][2][0] = cube[0][2][0], cube[0][0][0]
    cube[5][0][0], cube[5][2][0] = cube[5][2][0], cube[5][0][0]
    clockwise_movement(1)

def move_L_prime():
    # rightmost layer movement
    cube[0][0][0], cube[0][1][0], cube[0][2][0], cube[2][0][0], cube[2][1][0], cube[2][2][0] = cube[2][0][0], cube[2][1][0], cube[2][2][0], cube[0][0][0], cube[0][1][0], cube[0][2][0]
    cube[4][0][2], cube[4][1][2], cube[4][2][2], cube[2][0][0], cube[2][1][0], cube[2][2][0] = cube[2][0][0], cube[2][1][0], cube[2][2][0], cube[4][0][2], cube[4][1][2], cube[4][2][2]
    cube[5][0][0], cube[5][1][0], cube[5][2][0], cube[2][0][0], cube[2][1][0], cube[2][2][0] = cube[2][0][0], cube[2][1][0], cube[2][2][0], cube[5][0][0], cube[5][1][0], cube[5][2][0]
    cube[4][0][0], cube[4][2][0] = cube[4][2][0], cube[4][0][0]
    cube[5][0][0], cube[5][2][0] = cube[5][2][0], cube[5][0][0]
    counterclockwise_movement(1)

def move_F():
    cube[0][2][0], cube[0][2][1], cube[0][2][2], cube[3][0][0], cube[3][1][0], cube[3][2][0], = cube[3][0][0], cube[3][1][0], cube[3][2][0], cube[0][2][0], cube[0][2][1], cube[0][2][2]
    cube[0][2], cube[5][0] = cube[5][0], cube[0][2]
    cube[0][2][0], cube[0][2][1], cube[0][2][2], cube[1][0][2], cube[1][1][2], cube[1][2][2], = cube[1][0][2], cube[1][1][2], cube[1][2][2], cube[0][2][0], cube[0][2][1], cube[0][2][2]
    clockwise_movement(2)

def move_cube():
    move_list = input("type in the move: ").split(" ")
    for move in move_list:
        if move == "U": move_U()
        elif move == "U'": move_U_prime()
        elif move == "U2":
            move_U()
            move_U()
        elif move == "E": move_E()
        elif move == "E'": move_E_prime()
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
        elif move == "L": move_L()
        elif move == "L'": move_L_prime()
        elif move == "L2":
            move_L()
            move_L()
        elif move == "M": move_M()
        elif move == "F": move_F()
        print_cube()
        time.sleep(0.5)

while True:
    print_cube()
    move_cube()
