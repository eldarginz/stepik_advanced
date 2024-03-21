def fill_blank_matrix(n, m):  # Создание и заполнение матрицы нулями
    return [[0]*m for i in range(n)]


n = int(input())
matrix = fill_blank_matrix(n, n)
counter = 1

for i in range(n):
    for j in range(n):
        if i == j or i == n - j - 1 or (i < j and i < n-1-j) or (i > j and i > n-1-j):
            matrix[i][j] = 1

for i in range(n):
    for j in range(n):
        print(str(matrix[i][j]).ljust(2), end=' ')
    print()
