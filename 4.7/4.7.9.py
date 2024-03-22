def print_matrix(matrix):  # Печать матрицы
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()


def fill_blank_matrix(n, m):  # Создание и заполнение матрицы нулями
    return [[0]*m for i in range(n)]


def summ_matrix(matrix1, matrix2):
    rez = [[0]*len(matrix1[0]) for i in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            rez[i][j] = int(matrix1[i][j]) + int(matrix2[i][j])
    return rez


n, m = [int(i) for i in input().split()]

matrix1 = [input().split() for _ in range(n)]
input()
matrix2 = [input().split() for _ in range(n)]
matrix3 = summ_matrix(matrix1, matrix2)

print_matrix(matrix3)
