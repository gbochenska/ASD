
class Matrix:
    def __init__(self, mat, constant=0):
        if isinstance(mat, tuple):
            self.__mat = [[constant for i in range(mat[1])] for k in range(mat[0])]
        else:
            self.__mat = mat

    def __add__(self, b):
        if len(self.__mat) == len(b.__mat) and len(self.__mat[0]) == len(b.__mat[0]):
            matrix2 = Matrix(self)
            matrix2.__mat = []
            for i in range(len(self.__mat)):
                matrix1 = []
                for j in range(len(self.__mat[0])):
                    matrix1.append(self.__mat[i][j] + b.__mat[i][j])
                matrix2.__mat.append(matrix1)
            return matrix2

    def __mul__(self, b):
        if len(self.__mat) == len(b.__mat[0]) and len(self.__mat[0]) == len(b.__mat):
            matrix2 = Matrix(self)
            matrix2.__mat = []
            for i in range(len(self.__mat)):
                matrix1 = []
                for j in range(len(b.__mat[0])):
                    el = 0
                    for k in range(len(b.__mat)):
                        el += self.__mat[i][k] * b.__mat[k][j]
                    matrix1.append(el)
                matrix2.__mat.append(matrix1)
            return matrix2


    def __getitem__(self, item):
        return self.__mat[item]

    def __str__(self):
        string = []
        for i in range(len(self.__mat)):
            help_string = []
            for j in range(len(self.__mat[0])):
                help_string.append(self.__mat[i][j])
            string.append(help_string)
        return str(string)

    def __len__(self):
        rows = len(self.__mat)
        return rows

def transpose(matrix):
    new_matrix = Matrix((len(matrix[0]), len(matrix)))
    for i in range(len(new_matrix)):
        for j in range(len(new_matrix[0])):
            new_matrix[i][j] = matrix[j][i]
    return new_matrix

def chio1(a):
    new_matrix = Matrix((len(a)-1, len(a[0])-1))
    if a[0][0] == 0:
        a[0][0] = 0.000000000001               #w momencie gdy pierwszy wyraz jest równy 0, zakładamy że jest on bardzo bliski 0, wynik mimo wszystko jest bardzo zbliżony do oczekiwanego
    cons = (1 /((a[0][0]) ** (len(a) - 2)))
    while len(a) > 2:
        new_matrix = Matrix((len(a)-1, len(a)-1))
        for i in range(1, len(a)-1):
            for j in range(1, len(a)-1):
                new_matrix[i][j] = (a[0][0]*a[i][j] - a[0][j]*a[i][0])
        a = new_matrix
        cons *= (1 /((a[0][0]) ** (len(a) - 2)))
    result = (a[0][0] * a[1][1] - a[0][1] * a[1][0]) * cons
    return result

if __name__ == "__main__":
    a1 = [[5, 1, 1, 2, 3],
        [4, 2, 1, 7, 3],
        [2, 1, 2, 4, 7],
        [9, 1, 0, 7, 0],
        [1, 4, 7, 2, 2]]
    b1 =  [
     [0 , 1 , 1 , 2 , 3],
     [4 , 2 , 1 , 7 , 3],
     [2 , 1 , 2 , 4 , 7],
     [9 , 1 , 0 , 7 , 0],
     [1 , 4 , 7 , 2 , 2]
    ]
    a = Matrix(a1)
    b = Matrix(b1)

    print("Wyznacznik jest równy: ", chio1(a))
    print("Wyznacznik jest równy: ", chio1(b))




