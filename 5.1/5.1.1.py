matrix = input().split()
n = int(input())
rez = []

for i in range(n):
    rez.append(matrix[i::n])
print(rez)
