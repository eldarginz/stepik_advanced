from math import sqrt, sin, fabs


def kvadrat(number):
    return number**2


def kub(number):
    return number**3


def koren(number):
    return sqrt(number)


def modul(number):
    return fabs(number)


def sinus(number):
    return sin(number)


functions = {'квадрат': kvadrat, 'куб': kub,
             'корень': koren, 'модуль': modul, 'синус': sinus}

n = int(input())
print(functions[input().lower()](n))
