def print_products(*args):
    a = [i for i in args if type(i) is str and len(i) != 0]
    if len(a) > 0:
        for i in range(len(a)):
            print(f'{i+1}) {a[i]}')
    else:
        print('Нет продуктов')
