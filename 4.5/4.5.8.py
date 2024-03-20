map = [['.']*8 for _ in range(8)]

xy = input()
x = '87654321'.index(xy[1])
y = 'abcdefgh'.index(xy[0])

map[x][y] = 'N'

for i in range(len(map)):
    for j in range(len(map)):
        if (i - x) ** 2 + (j - y) ** 2 == 5:
            map[i][j] = '*'
        print(map[i][j], end=' ')
    print()
