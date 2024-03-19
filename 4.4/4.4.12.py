n = int(input())
matrix = []
rez = 0

for i in range(n):
    matrix.append(input().split())

a = []
for i in range(n):
    for j in range(i+1):
        a.append(int(matrix[i][j]))

print(max(a))