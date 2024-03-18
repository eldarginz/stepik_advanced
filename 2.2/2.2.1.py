def opredelenie(x, y):
    if x > 0 and y > 0:
        return (1)
    if x < 0 and y > 0:
        return (2)
    if x < 0 and y < 0:
        return (3)
    if x > 0 and y < 0:
        return (4)


count1 = 0
count2 = 0
count3 = 0
count4 = 0

for i in range(int(input())):
    num = input().split()
    if opredelenie(int(num[0]), int(num[1])) == 1:
        count1 += 1
    if opredelenie(int(num[0]), int(num[1])) == 2:
        count2 += 1
    if opredelenie(int(num[0]), int(num[1])) == 3:
        count3 += 1
    if opredelenie(int(num[0]), int(num[1])) == 4:
        count4 += 1

print(f'Первая четверть: {count1}')
print(f'Вторая четверть: {count2}')
print(f'Третья четверть: {count3}')
print(f'Четвертая четверть: {count4}')
