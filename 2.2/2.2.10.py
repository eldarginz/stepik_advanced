n = int(input())

text = []
counter = []


for i in range(n):
    text.append(input())
    buffer = text[i]
    buffer2 = ''
    for j in range(len(buffer)):
        if buffer[j] in 'anton':
            buffer2 += buffer[j]
            if buffer2 == 'anton':
                counter.append(i+1)


print(*counter)
