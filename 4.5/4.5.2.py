n = int(input())
m = int(input())
matrix = []

for i in range(n):
    matrix.append(input().split())

max_in_matrix = max(max(matrix, key=max))
print(max_in_matrix)

a = 0
b = 0

for i in range(n):
    for j in range(m):
        if (matrix[i][j]) == max_in_matrix:
            a = i
            b = j
            print(a,b)
