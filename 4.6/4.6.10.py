def fill_blank_matrix(n, m):  # Создание и заполнение матрицы нулями
    return [[0]*m for i in range(n)]


x, y = (input().split())
matrix = fill_blank_matrix(int(x), int(y))
counter = 1


for i in range(int(y)):
    matrix[0][i] = counter
    counter += 1

for j in range(int(x)):
    matrix[j][int(y)-1] = counter
    counter += 1



for i in range(int(x)):
    for j in range(int(y)):
        print(str(matrix[i][j]).ljust(2), end=' ')
    print()
