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


if __name__ == "__main__":
    a1 = [[1, 0, 2],
     [-1, 3, 1]]
    b1 = [ [1, 1, 1],
     [1, 1, 1] ]
    c1 = [[3, 1], [2, 1], [1, 0]]

    a = Matrix(a1)
    b = Matrix((2,3),constant=1)
    c = Matrix(c1)


    print(transpose(a))
    print(a+b)
    print(a*c)

