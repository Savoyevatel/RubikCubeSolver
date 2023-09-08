import numpy as np
import copy

c = ''# C is a string based on yellow, blue, red, green, orange, white and is generated 9 times as the number of squares of each color
for i in "ybrgow":
    if "ybrgow":
        for j in range(1,10):
            c = c + (f'{i}{j}')

def g(matrix):######rotate 90 degrees same as g
    matrix = np.array(matrix)
    matrix = (np.rot90(matrix)).tolist()
    return matrix

def f(matrix):######rotate -90 degrees same as f
    matrix = np.array(matrix)
    matrix = (np.rot90(matrix,-1)).tolist()
    return matrix

def ff(matrix):######rotate 180 degrees same as ff()
    matrix = np.array(matrix)
    matrix = (np.rot90(matrix,2)).tolist()
    return matrix

def turnX(string):##### Rotates the cube to the x direction based on https://ruwix.com/the-rubiks-cube/notation/
    pairs = [string[i:i + 2] for i in range(0, len(string), 2)]
    U, L, F, R, B, D = ([list(pairs[9 * i:9 * i + 9][j * 3:j * 3 + 3]) for j in range(3)] for i in range(6))
    (U, L, F, R, B, D) = (F, g(L), D, f(R), ff(U), ff(B))
    x = [U, L, F, R, B, D]
    res = ''
    for x in x:
        if x:
            for y in x:
                res = res + "".join(y)
    return res
print(turnX(c))
