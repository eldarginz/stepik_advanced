import random

length = int(input())    # длина пароля

for i in range(length):
    if random.randint(0, 1):
        print(chr(random.randint(65, 90)), end='')
    else:
        print(chr(random.randint(97, 122)), end='')
