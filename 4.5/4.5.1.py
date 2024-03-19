n, m = int(input()), int(input())

for i in range(n):
    mult = []
    for j in range(m):
        mult.append(str(i*j).ljust(3))
    print(*mult)
