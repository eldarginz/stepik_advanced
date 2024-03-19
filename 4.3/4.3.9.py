n = int(input())

a = []

for i in range(n):
    for j in range(i):
        a[i][j].row(i)

print(a)