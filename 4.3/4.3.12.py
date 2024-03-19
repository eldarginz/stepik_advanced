char_list = []
a = []

for char in input().split():
    if not a:
        a.append(char)
    elif a:
        if a[-1] == char:
            a.append(char)
        elif a[-1] != char:
            char_list.append(a)
            a = []
            a.append(char)

if a:
    char_list.append(a)

print(char_list)
