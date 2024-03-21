def fill_blank_matrix(n, m):  # Создание и заполнение матрицы нулями
    return [[0]*m for i in range(n)]


n, m = (input().split())
matrix = fill_blank_matrix(int(n), int(m))
counter = 1

for i in range(int(n)):
    for j in range(int(m)):
        matrix[i][j] = counter
        counter += 1

for i in range(1, int(n), 2):
    matrix[i].reverse()

for i in range(int(n)):
    for j in range(int(m)):
        print(str(matrix[i][j]).ljust(2), end=' ')
    print()
