# формуля для хода ферзя abs(x1 - x2) == abs(y1 - y2) or x1 == x2 or y1 == y2:

map = [['.']*8 for _ in range(8)]

xy = input()
x = '87654321'.index(xy[1])
y = 'abcdefgh'.index(xy[0])

map[x][y] = 'Q'

for i in range(len(map)):
    for j in range(len(map)):
        if abs(i-x) == abs(j-y) or x == i or y == j:
            map[i][j] = '*'
            map[x][y] = 'Q'
        print(map[i][j], end=' ')
    print()
