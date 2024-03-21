n = int(input())  # Размер матрицы

numbers = [_+1 for _ in range(n**2)]  # 1..n**2

matrix = [input().split() for _ in range(n)]  # Ввод матрицы

diagonal = 0
second_diagonal = 0

for i in range(n):  # Сумма чисел двух диагоналей матрицы
    for j in range(n):
        diagonal += int(matrix[i][i])
        second_diagonal += int(matrix[n-1-i][i])
diagonal /= n
second_diagonal /= n

for i in range(n):  # Сумма строк
    sum = 0
    for j in range(n):
        sum += int(matrix[i][j])
        # print(matrix[i][j], end=' ')
    if sum == int(diagonal) and sum == int(second_diagonal):
        continue
    else:
        print('NO')
        quit()

for i in range(n):  # Сумма столбцов
    sum = 0
    for j in range(n):
        sum += int(matrix[j][i])
    if sum == int(diagonal) and sum == int(second_diagonal):
        continue
    else:
        print('NO')
        quit()

matrix_open = []  # Открытие матрицы
for i in range(n):
    for j in range(n):
        matrix_open.append(int(matrix[i][j]))
matrix_open.sort()

if matrix_open == numbers:  # Проверка 1,2..n**2 in matrix
    print('YES')
else:
    print('NO')
