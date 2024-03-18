counter = 0
num = input().split()
for i in range(1, len(num)):
    if int(num[i-1]) < int(num[i]):
        counter += 1

print(counter)
