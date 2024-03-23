def fill_blank_matrix(n, m):  # Создание и заполнение матрицы нулями
    return [[int(0)]*m for i in range(n)]


def print_matrix(matrix):  # Печать матрицы
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()


n = int(input())
matrix = fill_blank_matrix(n, n)

for i in range(n):
    for j in range(n):
        matrix[i][j] = abs(i-j)

print_matrix(matrix)
