# m[k][i], m[k][j] = m[k][j], m[k][i]

n = int(input())
m = int(input())
matrix = []

for _ in range(n):
    matrix.append(input().split())

i, j = input().split()

for _ in range(n):
    matrix[_][int(i)], matrix[_][int(j)] = matrix[_][int(j)], matrix[_][int(i)]

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()
