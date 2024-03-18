num = [int(i) for i in input().split()]
num.insert(0, num.pop(-1))
print(*num)
