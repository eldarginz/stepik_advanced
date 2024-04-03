from fractions import Fraction

n = int(input())

rez = Fraction(1, 1**2)

if n == 1:
    print(rez)
else:
    for i in range(2, n+1):
        rez += Fraction(1, i**2)
    print(rez)
