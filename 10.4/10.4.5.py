country = {}

for i in range(int(input())):
    a, *b = input().split()
    country[a] = b

for _ in range(int(input())):
    buffer = input()
    for j in country:
        for k in range(len(country[j])):
            if buffer == country[j][k]:
                print(j)
