# Печать матрицы
def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()

# Создание и заполнение матрицы нулями


def fill_blank_matrix(n, m):
    return [[0]*m for i in range(n)]

# Заполнение матрицы input()


def input_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = input()
    return matrix


print_matrix(input_matrix(fill_blank_matrix(int(input()), int(input()))))
