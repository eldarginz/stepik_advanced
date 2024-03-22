def print_matrix(matrix):  # Печать матрицы
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()


def fill_blank_matrix(n, m):  # Создание и заполнение матрицы нулями
    return [[0]*m for i in range(n)]


n, m = [int(i) for i in input().split()]
matrix1 = [input().split() for _ in range(n)]
input()
m, k = [int(i) for i in input().split()]
matrix2 = [input().split() for _ in range(m)]

matrix3 = fill_blank_matrix(n, k)


for i in range(n):
    for j in range(k):
        for x in range(m):
            matrix3[i][j] += int(matrix1[i][x]) * int(matrix2[x][j])

print_matrix(matrix3)
