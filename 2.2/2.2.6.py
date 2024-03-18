n = int(input())
nums = []

for i in range(n):
    nums.append(int(input()))

rez = int(input())

for i in range(0, n-1):
    for j in range(i+1, n-1):
        print(nums[i],nums[j],rez)
        if nums[i]*nums[j] == rez:
            print('ДА')
            break

print('НЕТ')
