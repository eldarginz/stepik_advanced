import random

numbers = [random.randint(1, 49) for _ in range(7)]
numbers.sort()

print(*numbers, sep='\n')
