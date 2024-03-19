def chunk(text, n):
    rez = []
    for i in range(0, len(text), n):
        rez.append(text[i:i+n])
    return rez


text = input().split()
n = int(input())


print(chunk(text, n))
