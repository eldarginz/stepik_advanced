from math import sqrt


def summa(a, b):
    return (a+b)


def raznost(a, b):
    return (a-b)


def proizveden(a, b):
    return (a*b)


def chastnoy(a, b):
    return (a/b)


def celoeotdel(a, b):
    return (a//b)


def ostatok(a, b):
    return (a % b)


def koren10step(a, b):
    return (sqrt(a**10 + b**10))


a = int(input())
b = int(input())

print(summa(a, b), raznost(a, b), proizveden(a, b), chastnoy(
    a, b), celoeotdel(a, b), ostatok(a, b), koren10step(a, b), sep='\n')
