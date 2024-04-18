def ways_protection(instruction):
    name, *way = instruction.split()
    for operation in way:
        access.setdefault(operation, []).append(name)


def control(command):
    instruction, way = command.split()
    decoded = decoding[instruction]
    if way in access[decoded]:
        print('OK')
    else:
        print('Access denied')


access = {'W': [], 'X': [], 'R': []}
decoding = {'write': 'W', 'execute': 'X', 'read': 'R'}

m = int(input())

for i in range(m):
    ways_protection(input())

n = int(input())

for i in range(n):
    control(input())
