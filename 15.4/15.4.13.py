def by_name(args):
    return args[0]


def by_age(args):
    return args[1]


def by_height(args):
    return args[2]


def by_weight(args):
    return args[3]


athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30),
            ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]

sorting = {1: by_name, 2: by_age, 3: by_height, 4: by_weight}


for i in sorted(athletes, key=sorting[int(input())]):
    print(*i)
