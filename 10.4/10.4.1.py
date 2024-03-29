programmer_dict = {}

for i in range(int(input())):
    key, value = input().split(': ')
    programmer_dict[key.lower()] = value

ask = [input().lower() for i in range(int(input()))]

for i in ask:
    if i in programmer_dict:
        print(programmer_dict[i])
    else:
        print('Не найдено')
