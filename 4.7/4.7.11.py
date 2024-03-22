import copy

def print_matrix(matrix):  # Печать матрицы
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()


def fill_blank_matrix(n, m):  # Создание и заполнение матрицы нулями
    return [[0]*m for i in range(n)]


def proizvedenie_matrix(matrix1, matrix2, matrix_rez):
    for i in range(int(len(matrix1))):
        for j in range(len(matrix2[0])):
            for x in range(len(matrix2)):
                matrix_rez[i][j] += int(matrix1[i][x]) * int(matrix2[x][j])
    return matrix_rez


n = int(input())
matrix1 = [input().split() for _ in range(n)]
m = int(input())

matrix2 = copy.deepcopy(matrix1)

matrix_rez = fill_blank_matrix(n,n)

#for i in range(1,m):
print('-2-')
matrix1 = proizvedenie_matrix(matrix1, matrix2, matrix_rez)
print_matrix(matrix_rez)
matrix1 = copy.deepcopy(matrix_rez)
print('-3-')
matrix_rez = proizvedenie_matrix(matrix1, matrix2, matrix_rez)
print_matrix(matrix_rez)
matrix1 = copy.deepcopy(matrix_rez)
print('-4-')
matrix_rez = proizvedenie_matrix(matrix1, matrix2, matrix_rez)
print_matrix(matrix_rez)
matrix1 = copy.deepcopy(matrix_rez)
print('-5-')
matrix_rez = proizvedenie_matrix(matrix1, matrix2, matrix_rez)
print_matrix(matrix_rez)
matrix1 = copy.deepcopy(matrix_rez)


#n, m = [int(i) for i in input().split()]
#matrix1 = [input().split() for _ in range(n)]
#input()
#m, k = [int(i) for i in input().split()]
#matrix2 = [input().split() for _ in range(m)]
#matrix3 = fill_blank_matrix(n, k)
#matrix3 = proizvedenie_matrix(matrix1, matrix2, matrix3)
#
#print_matrix(matrix3)
#