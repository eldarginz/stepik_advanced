def fill_blank_matrix(n, m):  # Создание и заполнение матрицы нулями
    return [['.']*m for i in range(n)]


def print_matrix(matrix):  # Печать матрицы
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()


n = int(input())
matrix = fill_blank_matrix(n, n)

for i in range(n):
    matrix[i][n//2] = '*'
    matrix[n//2][i] = '*'
    for j in range(n):
        if i == j:
            matrix[i][j] = '*'
        if i+j+1 == n or n-i-1 == j:
            matrix[i][j] = '*'

print_matrix(matrix)
