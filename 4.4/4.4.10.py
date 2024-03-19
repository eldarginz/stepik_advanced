def print_matrix(matrix):
    # Печать матрицы
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()


def print_rev_matrix(matrix):
    # Печать перевернутой матрицы
    for j in range(len(matrix[0])):
        for i in range(len(matrix)):
            print(matrix[i][j], end=' ')
        print()


def fill_blank_matrix(n, m):
    # Создание и заполнение матрицы нулями
    return [[0]*m for i in range(n)]


n = int(input())
rez = []
sledmatrix = 0

for i in range(n):
    rez.append(input().split())

for i in range(n):
    sledmatrix += int(rez[i][i])

print(sledmatrix)
