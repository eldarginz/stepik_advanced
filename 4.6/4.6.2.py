def fill_blank_matrix(n, m):  # Создание и заполнение матрицы нулями
    return [[0]*m for i in range(n)]


n = int(input())

matrix = fill_blank_matrix(n, n)


for i in range(n):
    for j in range(n):
        if (i + j == n - 1):
            matrix[i][j] = '1'
        elif (i + j >= n):
            matrix[i][j] = '2'
        else:
            matrix[i][j] = '0'
        print(matrix[i][j], end=' ')
    print()
