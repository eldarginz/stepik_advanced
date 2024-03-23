def fill_blank_matrix(n, m):  # Создание и заполнение матрицы нулями
    return [[int(0)]*m for i in range(n)]


n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
matrixrev = fill_blank_matrix(n, n)

flag = True

for i in range(n):
    if sorted(matrix[i]) != [*range(1, n+1)]:
        flag = False
        break

matrix.reverse()

for i in range(n):
    for j in range(n):
        matrixrev[i][j] = matrix[j][i]

for i in range(n):
    if sorted(matrixrev[i]) != [*range(1, n+1)]:
        flag = False
        break

if flag:
    print('YES')
else:
    print('NO')
