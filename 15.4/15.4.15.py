def fun(x):
    x = [int(i) for i in str(x)]
    return sum(x)


nums = input().split()
nums.sort(key=fun)

print(*nums)
