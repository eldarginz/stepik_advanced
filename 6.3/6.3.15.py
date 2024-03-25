n = int(input())

i1, i2, i3 = 1, 1, 1

if n <= 3:
    for i in range(n):
        print(1, end=' ')
    quit()

print(i1, i2, i3, end=' ')

for i in range(n-3):
    i1, i2, i3 = i2, i3, i1 + i2 + i3
    print(i3, end=' ')
