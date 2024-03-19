n = int(input())
matrix = []
rez = 0

for i in range(n):
    matrix.append(input().split())

a = []
for i in range(n):
    for j in range(n):
        if (i >= j and i <= n-1-j) or (i <= j and i >= n-1-j):
            a.append(int(matrix[i][j]))

print(max(a))
