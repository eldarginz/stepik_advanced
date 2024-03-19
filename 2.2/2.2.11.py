text = input() + ' запретил букву'

b = [chr(i) for i in range(1072, 1104)]

for i in b:
    if i in text:
        print(text, i)
        text = text.replace(i, '')
        text = ' '.join(text.split())
