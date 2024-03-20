n = int(input())

numbers = [_+1 for _ in range(n**2)]  # 1..n**2

matrix = [input().split() for _ in range(n)]



for i in range(n):
    for j in range(n):
        matrix[i][i] = '*'
        matrix[n-1-i][i] = '*'


print('---')

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=' ')
    print()
