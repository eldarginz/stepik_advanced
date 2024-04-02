import random
list_num = [*range(1, 76)]

numbers = random.sample(list_num, 25)
bingo = [[str(numbers.pop()).ljust(3) for _ in range(5)] for _ in range(5)]
bingo[2][2] = str(0).ljust(3)

[print(*row, sep='') for row in bingo]
