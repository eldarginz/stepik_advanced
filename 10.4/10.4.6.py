phones = {}

for i in range(int(input())):
    number, name = input().split(' ')
    if name.lower() in phones:
        phones[name.lower()].append(number)
    else:
        phones[name.lower()] = [number]

for i in range(int(input())):
    buffer = input().lower()
    if buffer in phones:
        print(*phones[buffer])
    else:
        print('абонент не найден')
