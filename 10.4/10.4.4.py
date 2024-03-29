sinonim_dict = {}

for i in range(int(input())):
    key, value = input().split(' ')
    sinonim_dict[key] = value
    sinonim_dict[value] = key

ask = input()

if ask in sinonim_dict:
    print(sinonim_dict[ask])
