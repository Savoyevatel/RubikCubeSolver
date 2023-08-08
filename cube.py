import itertools
import random
import numpy as np

'''
result = []
for i in range(6):
    result.extend([i] + list(x) for x in itertools.product(range(3), repeat = 2))
print(result)
'''
lst = [[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [0, 1, 2], [0, 2, 0], [0, 2, 1], [0, 2, 2]]
cube = [[[i, *x[1:]] for x in lst] for i in range(0, 6)]

top, left, right, front, back, bottom = cube

def turn_horizontal(face, direction, row):
    if row == 1:
        row = row[:3]
        if direction == 0:#left
            cube[1][:l], cube[2][:l], cube[3][:l], cube[4][:l] = cube[2][:l],cube[3][:l],cube[4][:l],cube[1][:l]

        elif direction ==1: #right
            cube[1][:l], cube[2][:l], cube[3][:l], cube[4][:l] = cube[4][:l], cube[1][:l], cube[2][:l], cube[3][:l]
        else:
            print("That's not an available position!")

# = out[0]
