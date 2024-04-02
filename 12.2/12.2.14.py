import random
n, m = int(input()), int(input())


def generate_password(count, length):
    num = ['2', '3', '4', '5', '6', '7', '8', '9']
    low = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm',
           'n', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    upp = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M',
           'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    passwords = []
    for i in range(count):
        buffer = []
        buffer.append(random.choice(num))
        buffer.append(random.choice(low))
        buffer.append(random.choice(upp))
        if length-3 > 0:
            for k in range(length-3):
                rnd = random.randint(0, 2)
                if rnd == 0:
                    buffer.append(random.choice(num))
                elif rnd == 1:
                    buffer.append(random.choice(low))
                elif rnd == 2:
                    buffer.append(random.choice(upp))
        random.shuffle(buffer)
        print(*buffer, sep='')


generate_password(n, m)
