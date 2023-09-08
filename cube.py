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

def turnY(string):
    pairs = [string[i:i + 2] for i in range(0, len(string), 2)]
    U, L, F, R, B, D = ([list(pairs[9 * i:9 * i + 9][j * 3:j * 3 + 3]) for j in range(3)] for i in range(6))
    (U, L, F, R, B, D) = (f(U), F, R, B, L, g(D))
    x = [U, L, F, R, B, D]
    res = ''
    for x in x:
        if x:
            for y in x:
                res = res + "".join(y)
    return res

def turnZ(string):
    pairs = [string[i:i + 2] for i in range(0, len(string), 2)]
    U, L, F, R, B, D = ([list(pairs[9 * i:9 * i + 9][j * 3:j * 3 + 3]) for j in range(3)] for i in range(6))
    (U, L, F, R, B, D) = (f(L), f(D), f(F), f(U), g(B), f(R))
    x = [U, L, F, R, B, D]
    res = ''
    for x in x:
        if x:
            for y in x:
                res = res + "".join(y)
    return res

def turnX_r(string):
    pairs = [string[i:i + 2] for i in range(0, len(string), 2)]
    U, L, F, R, B, D = ([list(pairs[9 * i:9 * i + 9][j * 3:j * 3 + 3]) for j in range(3)] for i in range(6))
    (U, L, F, R, B, D) = (ff(B), ff(g(L)), U, g(R), ff(D), F)
    x = [U, L, F, R, B, D]
    res = ''
    for x in x:
        if x:
            for y in x:
                res = res + "".join(y)
    return res

def turnY_r(string):
    pairs = [string[i:i + 2] for i in range(0, len(string), 2)]
    U, L, F, R, B, D = ([list(pairs[9 * i:9 * i + 9][j * 3:j * 3 + 3]) for j in range(3)] for i in range(6))
    (U, L, F, R, B, D) = (ff(f(U)),B,L,F,R,ff(g(D)))
    x = [U, L, F, R, B, D]
    res = ''
    for x in x:
        if x:
            for y in x:
                res = res + "".join(y)
    return res

def turnU(string):
    pairs = [string[i:i + 2] for i in range(0, len(string), 2)]
    U, L, F, R, B, D = ([list(pairs[9 * i:9 * i + 9][j * 3:j * 3 + 3]) for j in range(3)] for i in range(6))
    x = [f(U), L, F, R, B, D]
    U1, L1, F1, R1, B1, D1 = (f(U), F, R, B, L, D)
    y = (U1, L1, F1, R1, B1, D1)
    t = copy.deepcopy(y)
    for i in range(len(x)):
        x[i][0] = t[i][0]
    res = ''
    for x in x:
        if x:
            for y in x:
                res = res + "".join(y)
    return res

def turnU_r(string):
    pairs = [string[i:i + 2] for i in range(0, len(string), 2)]
    U, L, F, R, B, D = ([list(pairs[9 * i:9 * i + 9][j * 3:j * 3 + 3]) for j in range(3)] for i in range(6))
    U1, L1, F1, R1, B1, D1 = (g(U), B, L, F, R, D)
    x = [g(U), L, F, R, B, D]
    y = (U1, L1, F1, R1, B1, D1)
    t = copy.deepcopy(y)
    for i in range(len(x)):
        x[i][0] = t[i][0]
    res = ''
    for x in x:
        if x:
            for y in x:
                res = res + "".join(y)
    return res

def turnR(string):
    pairs = [string[i:i + 2] for i in range(0, len(string), 2)]
    U, L, F, R, B, D = ([list(pairs[9 * i:9 * i + 9][j * 3:j * 3 + 3]) for j in range(3)] for i in range(6))
    U, L, F, R, B, D = g(U), g(L), g(F), R, f(B), g(D)
    U1, L1, F1, R1, B1, D1 = (F, L, D, R, (U), B)
    x = [U, L, F, R, B, D]
    y = [U1, L1, F1, R1, B1, D1]
    t = copy.deepcopy(y)
    for i in range(len(x)):
        x[i][0] = t[i][0]
    x = [f(U), f(L), f(F), f(R), ff(f(B)), f(D)]
    res = ''
    for x in x:
        if x:
            for y in x:
                res = res + "".join(y)
    return res

def turnR_r(string):
    pairs = [string[i:i + 2] for i in range(0, len(string), 2)]
    U, L, F, R, B, D = ([list(pairs[9 * i:9 * i + 9][j * 3:j * 3 + 3]) for j in range(3)] for i in range(6))
    U1, L1, F1, R1, B1, D1 = (ff(B), g(L), ff(U), f(R), D, F)
    x = [U, L, F, R, B, D]
    y = [U1, L1, F1, R1, B1, D1]
    t = copy.deepcopy(y)
    for i in range(len(x)):
        x[i][0] = t[i][0]
    x = [f(U), f(L), f(F), f(R), ff(f(B)), f(D)]
    res = ''
    for x in x:
        if x:
            for y in x:
                res = res + "".join(y)
    return res

def turnL(string):
    pairs = [string[i:i + 2] for i in range(0, len(string), 2)]
    U, L, F, R, B, D = ([list(pairs[9 * i:9 * i + 9][j * 3:j * 3 + 3]) for j in range(3)] for i in range(6))
    x = [f(U), ff(L), f(F), f(R), g(B), f(D)]
    U1, L1, F1, R1, B1, D1 = (ff(f(B)), ff(L), f(U), f(R), f(D), f(F))

    y = [U1, L1, F1, R1, B1, D1]
    t = copy.deepcopy(y)

    for i in range(len(x)):
        x[i][0] = t[i][0]

    new_list = []
    for i in x:
        new_list.append(g(i))
    x = new_list
    x[4] = ff(x[4])
    return x

def turnL_r(string):
    pairs = [string[i:i + 2] for i in range(0, len(string), 2)]
    U, L, F, R, B, D = ([list(pairs[9 * i:9 * i + 9][j * 3:j * 3 + 3]) for j in range(3)] for i in range(6))
    x = [f(U), L, f(F), f(R), g(B), f(D)]
    U1, L1, F1, R1, B1, D1 = (f(F), L, f(D), f(R), f(U), ff(f(B)))
    y = [U1, L1, F1, R1, B1, D1]
    t = copy.deepcopy(y)

    for i in range(len(x)):
        x[i][0] = t[i][0]

    new_list = []
    for i in x:
        new_list.append(g(i))
    x = new_list
    x[4] = ff(x[4])
    res = ''
    for x in x:
        if x:
            for y in x:
                res = res + "".join(y)
    return res
