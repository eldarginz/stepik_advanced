n = int(input())
m = int(input())
matrix = []

for i in range(n):
    matrix.append(input().split())

maximum = matrix[0][0]
a = 0
b = 0

for i in range(n):
    for j in range(m):
        if int(matrix[i][j]) > int(maximum):
            maximum = matrix[i][j]
            a = i
            b = j

print(a, b)
