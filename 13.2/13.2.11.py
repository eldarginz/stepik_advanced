from fractions import Fraction
from math import factorial

n = int(input())

rez = Fraction(1, factorial(1))

if n == 1:
    print(rez)
else:
    for i in range(2, n+1):
        rez += Fraction(1, factorial(i))
    print(rez)
