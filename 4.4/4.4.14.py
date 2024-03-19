n = int(input())
matrix = []

upchet = 0
rightchet = 0
downchet = 0
leftchet = 0


for i in range(n):
    matrix.append(input().split())

a = []
for i in range(n):
    for j in range(n):
        if (i < j and i < n-1-j):
            upchet += int(matrix[i][j])
        if (i < j and i > n-1-j):
            rightchet += int(matrix[i][j])
        if (i > j and i > n-1-j):
            downchet += int(matrix[i][j])
        if (i > j and i < n-1-j):
            leftchet += int(matrix[i][j])

print(f'Верхняя четверть: {upchet}')
print(f'Правая четверть: {rightchet}')
print(f'Нижняя четверть: {downchet}')
print(f'Левая четверть: {leftchet}')
