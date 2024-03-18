num = [int(i) for i in input().split()]
num.sort()

counter = 1

for i in range(1, len(num)):
    if num[i-1] != num[i]:
        counter += 1
print(counter)
