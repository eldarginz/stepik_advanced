n, m = input().split()

matrix = [([i for i in ('.' * int(m))]) for i in range(int(n))]

for i in range(int(n)):
    for j in range(int(m)):
        if (i+j) % 2 != 0:
            matrix[i][j] = '*'
        print(matrix[i][j], end=' ')
    print()
