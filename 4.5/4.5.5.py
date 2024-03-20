# 2   3  1   2       0|0 <-> 4|0
# 6 7    5 4        1|1 <-> 3|1
#  9      9         2|2 <-> 2|2
# 5 4    6 7        3|3 <-> 1|3
# 1   2  2   3       4|4 <-> 0|4

n = int(input())
matrix = [input().split() for _ in range(n)]

for i in range(n):
    h = matrix[i][i]
    matrix[i][i] = matrix[n-1-i][i]
    matrix[n-1-i][i] = h

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=' ')
    print()
