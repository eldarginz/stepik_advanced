def find_anton(text):
    counter = 0
    for i in 'anton':
        if i in text:
            text = text[text.find(i):]
            counter += 1
    if counter == 5:
        return True
    else:
        return False


text = [input() for i in range(int(input()))]

rez = []

for i in range(len(text)):
    if find_anton(text[i]):
        rez.append(i+1)

print(*rez)
