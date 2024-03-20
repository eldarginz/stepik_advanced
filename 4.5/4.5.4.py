
# Матрица НЕ симметрична, если matrix[i][j] != matrix[j][i]

n = int(input())
matrix = [input().split() for _ in range(n)]
counter = 0

for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            counter += 1

if counter == 0:
    print('YES')
else:
    print('NO')
