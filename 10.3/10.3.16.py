text_input = input().split()

out_dict = {}

for i in text_input:
    out_dict[i] = out_dict.get(i, -1) + 1
    if out_dict.get(i, -1) + 1 == 1:
        print(i, end=' ')
    elif out_dict.get(i, -1) + 1 != 0:
        print(i, '_', out_dict.get(i, -1), sep='', end=' ')
