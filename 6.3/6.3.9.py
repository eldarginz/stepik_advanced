n = int(input())
rez = []
for i in range(n):
    rez.append(input().split())

for i in range(n):
    print(*rez[i])

print()

for i in range(n):
    if int(rez[i][1]) >= 4:
        print(*rez[i])
