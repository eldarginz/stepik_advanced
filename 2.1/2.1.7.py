num = input()
if len(num) == 5:
    num = num[::-1]
    print(int(num))

if len(num) == 6:
    print(num[0], num[1:][::-1], sep='')
