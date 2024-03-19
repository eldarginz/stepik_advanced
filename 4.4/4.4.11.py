n = int(input())
matrix = []
rez = 0

for i in range(n):
    matrix.append(input().split())

for i in range(n):
    mid = 0
    counter = 0
    for j in range(n):
        mid += int(matrix[i][j])
    mid /= n
    for j in range(n):
        if int(matrix[i][j]) > mid:
            counter += 1
    print(counter)
