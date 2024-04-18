data = {}
for i in range(int(input())):
    name, product, count = input().split()
    data.setdefault(name, {})
    data[name][product] = data[name].get(product, 0) + int(count)

data = dict(sorted(data.items()))

for i in data:
    data[i] = dict(sorted(data[i].items()))
    print(i+':')
    for j in data[i]:
        print(j, data[i][j])
