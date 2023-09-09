#Every move from this cube was based on "https://ruwix.com/the-rubiks-cube/notation/"
#The numpy is imported to change the matrix into different rotations 90 180 270 or -90 degrees
#The copy is imported to make a list immutable during some loops
import numpy as np
import copy
class Rubik(object):
    def __init__(self):
        pass

    def g(self, matrix): #Rotate matrix -90
        matrix = np.array(matrix)
        matrix = np.rot90(matrix).tolist()
        return matrix

    def f(self, matrix): #Rotate matrix 90
        matrix = np.array(matrix)
        matrix = np.rot90(matrix, -1).tolist()
        return matrix

    def ff(self, matrix): #Rotate matrix 180
        matrix = np.array(matrix)
        matrix = np.rot90(matrix, 2).tolist()
        return matrix

    def list_to_string(self, x): #Convert the current list to a list of strings
        res = ''
        for x in x:
            if x:
                for y in x:
                    res += "".join(y)
        return res

    def turnX(self, string): #Turn the cube into the X axis direction based on https://ruwix.com/the-rubiks-cube/notation/
        pairs = [string[i:i + 2] for i in range(0, len(string), 2)]
        U, L, F, R, B, D = (
            [list(pairs[9 * i:9 * i + 9][j * 3:j * 3 + 3]) for j in range(3)]
            for i in range(6)
        )
        (U, L, F, R, B, D) = (F, self.g(L), D, self.f(R), self.ff(U), self.ff(B))
        x = [U, L, F, R, B, D]
        x = self.list_to_string(x)
        return x

    def turnY(self, string): #Turn the cube into the Y axis direction
        pairs = [string[i:i + 2] for i in range(0, len(string), 2)]
        U, L, F, R, B, D = ([list(pairs[9 * i:9 * i + 9][j * 3:j * 3 + 3]) for j in range(3)] for i in range(6))
        (U, L, F, R, B, D) = (self.f(U), F, R, B, L, self.g(D))
        x = [U, L, F, R, B, D]
        x = self.list_to_string(x)
        return x

    def turnZ(self, string):
        pairs = [string[i:i + 2] for i in range(0, len(string), 2)]
        U, L, F, R, B, D = ([list(pairs[9 * i:9 * i + 9][j * 3:j * 3 + 3]) for j in range(3)] for i in range(6))
        (U, L, F, R, B, D) = (self.f(L), self.f(D), self.f(F), self.f(U), self.g(B), self.f(R))
        x = [U, L, F, R, B, D]
        x = self.list_to_string(x)
        return x

    def turnX_r(self, string):
        pairs = [string[i:i + 2] for i in range(0, len(string), 2)]
        U, L, F, R, B, D = ([list(pairs[9 * i:9 * i + 9][j * 3:j * 3 + 3]) for j in range(3)] for i in range(6))
        (U, L, F, R, B, D) = (self.ff(B), self.f(L), U, self.g(R), self.ff(D), F)
        x = [U, L, F, R, B, D]
        x = self.list_to_string(x)
        return x

    def turnY_r(self, string):
        pairs = [string[i:i + 2] for i in range(0, len(string), 2)]
        U, L, F, R, B, D = ([list(pairs[9 * i:9 * i + 9][j * 3:j * 3 + 3]) for j in range(3)] for i in range(6))
        (U, L, F, R, B, D) = (self.ff(self.f(U)), B, L, F, R, self.f(D))
        x = [U, L, F, R, B, D]
        x = self.list_to_string(x)
        return x

    def turnZ_r(self, string):
        pairs = [string[i:i + 2] for i in range(0, len(string), 2)]
        U, L, F, R, B, D = ([list(pairs[9 * i:9 * i + 9][j * 3:j * 3 + 3]) for j in range(3)] for i in range(6))
        (U, L, F, R, B, D) = (self.g(R), self.g(U), self.g(F), self.g(D), self.f(B), self.g(L))
        x = [U, L, F, R, B, D]
        x = self.list_to_string(x)
        return x

    def turnU(self, string):
        pairs = [string[i:i + 2] for i in range(0, len(string), 2)]
        U, L, F, R, B, D = ([list(pairs[9 * i:9 * i + 9][j * 3:j * 3 + 3]) for j in range(3)] for i in range(6))
        x = [self.f(U), L, F, R, B, D]
        U1, L1, F1, R1, B1, D1 = (self.f(U), F, R, B, L, D)
        y = (U1, L1, F1, R1, B1, D1)
        t = copy.deepcopy(y)
        for i in range(len(x)):
            x[i][0] = t[i][0]
        x = self.list_to_string(x)
        return x

    def turnU_r(self, string):
        pairs = [string[i:i + 2] for i in range(0, len(string), 2)]
        U, L, F, R, B, D = ([list(pairs[9 * i:9 * i + 9][j * 3:j * 3 + 3]) for j in range(3)] for i in range(6))
        U1, L1, F1, R1, B1, D1 = (self.g(U), B, L, F, R, D)
        x = [self.g(U), L, F, R, B, D]
        y = (U1, L1, F1, R1, B1, D1)
        t = copy.deepcopy(y)
        for i in range(len(x)):
            x[i][0] = t[i][0]
        x = self.list_to_string(x)
        return x

    def turnR(self, string):
        pairs = [string[i:i + 2] for i in range(0, len(string), 2)]
        U, L, F, R, B, D = ([list(pairs[9 * i:9 * i + 9][j * 3:j * 3 + 3]) for j in range(3)] for i in range(6))
        U, L, F, R, B, D = self.g(U), self.g(L), self.g(F), R, self.f(B), self.g(D)
        U1, L1, F1, R1, B1, D1 = (F, L, D, R, (U), B)
        x = [U, L, F, R, B, D]
        y = [U1, L1, F1, R1, B1, D1]
        t = copy.deepcopy(y)
        for i in range(len(x)):
            x[i][0] = t[i][0]
        x = [self.f(U), self.f(L), self.f(F), self.f(R), self.ff(self.f(B)), self.f(D)]
        x = self.list_to_string(x)
        return x

    def turnR_r(self, string):
        pairs = [string[i:i + 2] for i in range(0, len(string), 2)]
        U, L, F, R, B, D = ([list(pairs[9 * i:9 * i + 9][j * 3:j * 3 + 3]) for j in range(3)] for i in range(6))
        U1, L1, F1, R1, B1, D1 = (self.ff(B), self.g(L), self.ff(U), self.f(R), D, F)
        x = [U, L, F, R, B, D]
        y = [U1, L1, F1, R1, B1, D1]
        t = copy.deepcopy(y)
        for i in range(len(x)):
            x[i][0] = t[i][0]
        x = [self.f(U), self.f(L), self.f(F), self.f(R), self.ff(self.f(B)), self.f(D)]
        x = self.list_to_string(x)
        return x

    def turnL(self, string):
        pairs = [string[i:i + 2] for i in range(0, len(string), 2)]
        U, L, F, R, B, D = ([list(pairs[9 * i:9 * i + 9][j * 3:j * 3 + 3]) for j in range(3)] for i in range(6))
        x = [self.f(U), self.ff(L), self.f(F), self.f(R), self.g(B), self.f(D)]
        U1, L1, F1, R1, B1, D1 = (self.ff(self.f(B)), self.ff(L), self.f(U), self.f(R), self.f(D), self.f(F))
        y = [U1, L1, F1, R1, B1, D1]
        t = copy.deepcopy(y)
        for i in range(len(x)):
            x[i][0] = t[i][0]
        new_list = []
        for i in x:
            new_list.append(self.g(i))
        x = new_list
        x[4] = self.ff(x[4])
        x = self.list_to_string(x)
        return x

    def turnL_r(self, string):
        pairs = [string[i:i + 2] for i in range(0, len(string), 2)]
        U, L, F, R, B, D = ([list(pairs[9 * i:9 * i + 9][j * 3:j * 3 + 3]) for j in range(3)] for i in range(6))
        x = [self.f(U), L, self.f(F), self.f(R), self.g(B), self.f(D)]
        U1, L1, F1, R1, B1, D1 = (self.f(F), L, self.f(D), self.f(R), self.f(U), self.ff(self.f(B)))
        y = [U1, L1, F1, R1, B1, D1]
        t = copy.deepcopy(y)
        for i in range(len(x)):
            x[i][0] = t[i][0]
        new_list = []
        for i in x:
            new_list.append(self.g(i))
        x = new_list
        x[4] = self.ff(x[4])
        x = self.list_to_string(x)
        return x

    def turnF(self, string):
        # F == Y + L + Y'
        x = self.turnY(string)
        x = self.turnL(x)
        x = self.turnY_r(x)
        return x

    def turnF_r(self, string):
        # F'== Y+L'+Y'
        x = self.turnY(string)
        x = self.turnL_r(x)
        x = self.turnY_r(x)
        return x

    def turnB(self, string):
        # B == Y'+L+Y
        x = self.turnY_r(string)
        x = self.turnL(x)
        x = self.turnY(x)
        return x

    def turnB_r(self, string):
        # B' == Y'+L'+Y
        x = self.turnY_r(string)
        x = self.turnL_r(x)
        x = self.turnY(x)
        return x

    def turnD(self, string):
        pairs = [string[i:i + 2] for i in range(0, len(string), 2)]
        U, L, F, R, B, D = ([list(pairs[9 * i:9 * i + 9][j * 3:j * 3 + 3]) for j in range(3)] for i in range(6))
        x = [U, L, F, R, B, self.f(D)]
        U1, L1, F1, R1, B1, D1 = (U, B, L, F, R, self.f(D))
        y = (U1, L1, F1, R1, B1, D1)
        t = copy.deepcopy(y)
        for i in range(len(x)):
            x[i][2] = t[i][2]
        x = self.list_to_string(x)
        return x

    def turnD_r(self, string):
        pairs = [string[i:i + 2] for i in range(0, len(string), 2)]
        U, L, F, R, B, D = ([list(pairs[9 * i:9 * i + 9][j * 3:j * 3 + 3]) for j in range(3)] for i in range(6))
        x = [U, L, F, R, B, self.g(D)]
        U1, L1, F1, R1, B1, D1 = (U, F, R, B, L, self.g(D))
        y = (U1, L1, F1, R1, B1, D1)
        t = copy.deepcopy(y)
        for i in range(len(x)):
            x[i][2] = t[i][2]
        x = self.list_to_string(x)
        return x

    def turnM(self, string):
        pairs = [string[i:i + 2] for i in range(0, len(string), 2)]
        U, L, F, R, B, D = ([list(pairs[9 * i:9 * i + 9][j * 3:j * 3 + 3]) for j in range(3)] for i in range(6))
        x = [self.f(U), self.f(L), self.f(F), self.f(R), self.g(B), self.f(D)]
        U1, L1, F1, R1, B1, D1 = (self.ff(self.f(B)), self.f(L), self.f(U), self.f(R), self.f(D), self.f(F))

        y = [U1, L1, F1, R1, B1, D1]
        t = copy.deepcopy(y)

        for i in range(len(x)):
            x[i][1] = t[i][1]

        new_list = []
        for i in x:
            new_list.append(self.g(i))
        x = new_list
        x[4] = self.ff(x[4])
        x = self.list_to_string(x)
        return x

    def turnM_r(self, string):
        pairs = [string[i:i + 2] for i in range(0, len(string), 2)]
        U, L, F, R, B, D = ([list(pairs[9 * i:9 * i + 9][j * 3:j * 3 + 3]) for j in range(3)] for i in range(6))
        x = [self.f(U), self.f(L), self.f(F), self.f(R), self.g(B), self.f(D)]
        U1, L1, F1, R1, B1, D1 = (self.f(F), self.f(L), self.f(D), self.f(R), self.f(U), self.ff(self.f(B)))
        y = [U1, L1, F1, R1, B1, D1]
        t = copy.deepcopy(y)

        for i in range(len(x)):
            x[i][1] = t[i][1]

        new_list = []
        for i in x:
            new_list.append(self.g(i))
        x = new_list
        x[4] = self.ff(x[4])
        x = self.list_to_string(x)
        return x

    def turnE(self, string):
        pairs = [string[i:i + 2] for i in range(0, len(string), 2)]
        U, L, F, R, B, D = ([list(pairs[9 * i:9 * i + 9][j * 3:j * 3 + 3]) for j in range(3)] for i in range(6))
        x = [U, L, F, R, B, D]
        U1, L1, F1, R1, B1, D1 = (U, B, L, F, R, D)
        y = (U1, L1, F1, R1, B1, D1)
        t = copy.deepcopy(y)
        for i in range(len(x)):
            x[i][1] = t[i][1]
        x = self.list_to_string(x)
        return x

    def turnE_r(self, string):
        pairs = [string[i:i + 2] for i in range(0, len(string), 2)]
        U, L, F, R, B, D = ([list(pairs[9 * i:9 * i + 9][j * 3:j * 3 + 3]) for j in range(3)] for i in range(6))
        x = [U, L, F, R, B, D]
        U1, L1, F1, R1, B1, D1 = (U, F, R, B, L, D)
        y = (U1, L1, F1, R1, B1, D1)
        t = copy.deepcopy(y)
        for i in range(len(x)):
            x[i][1] = t[i][1]
        x = self.list_to_string(x)
        return x

    def turnS(self, string):
        x = self.turnY(string)
        x = self.turnM(x)
        x = self.turnY_r(x)
        return x

    def turnS_r(self, string):
        x = self.turnY(string)
        x = self.turnM_r(x)
        x = self.turnY_r(x)
        return x

    def doubleu(self, string):
        # u == E'+U
        x = self.turnE_r(string)
        x = self.turnU(x)
        return x

    def doubleu_r(self, string):
        # u' == E+U'
        x = self.turnE(string)
        x = self.turnU_r(x)
        return x

    def doublel(self, string):
        # l = L+M
        x = self.turnL(string)
        x = self.turnM(x)
        return x

    def doublel_r(self, string):
        # l' == L'+M'
        x = self.turnL_r(string)
        x = self.turnM_r(x)
        return x

    def doublef(self, string):
        # f == F+S
        x = self.turnF(string)
        x = self.turnS(x)
        return x

    def doublef_r(self, string):
        # f' == F'+S'
        x = self.turnF_r(string)
        x = self.turnS_r(x)
        return x

    def doubler(self, string):
        # r == R+M'
        x = self.turnR(string)
        x = self.turnM_r(x)
        return x

    def doubler_r(self, string):
        # r' == R'+M
        x = self.turnR(string)
        x = self.turnM_r(x)
        return x

    def doubleb(self, string):
        # b == B+S'
        x = self.turnB(string)
        x = self.turnS_r(x)
        return x

    def doubleb_r(self, string):
        # b' == B'+S
        x = self.turnB_r(string)
        x = self.turnS(x)
        return x

    def doubled(self, string):
        # d == D+E
        x = self.turnD(string)
        x = self.turnE(x)
        return x

    def doubled_r(self, string):
        # d' == D'+E'
        x = self.turnD_r(string)
        x = self.turnE_r(x)
        return x
#Generates the list of strings of the different colors (yellow, blue, red, green, orange and white) from 1 to 9 (y1,y2,y3,y4,y5,y6,y7,y8,y9)
#This to ensure that we are rotating the correct values in each face of the cube
c = ''
for i in "ybrgow":
    for j in range(1, 10):
        c += f'{i}{j}'

course = Rubik()
b = course.turnF_r(c)
c = course.turnR(b)
