n = int(input())

a = []

for i in range(n):
    for j in range(i+1):
        a[i][j].append(i)

print(a)