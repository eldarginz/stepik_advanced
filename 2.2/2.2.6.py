nums = []
out = 'НЕТ'

n = int(input())

for i in range(n):
    nums.append(int(input()))

rez = int(input())

for i in range(n):
    for j in range(n):
        if i != j:
            if nums[i] * nums[j] == rez:
                out = 'ДА'
                break

print(out)
