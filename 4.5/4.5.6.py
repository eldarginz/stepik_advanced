matrix = [input().split() for _ in range(int(input()))]
matrix.reverse()

for i in matrix:
    print(*i)
