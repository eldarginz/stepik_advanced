from fractions import Fraction
from math import gcd

sp = []
n = int(input())

for i in range(1, n):
    for j in range(0, n):
        if Fraction(i, n-j) < 1 and Fraction(i, n-j) not in sp:
            sp.append(Fraction(i, n-j))

for i in sorted(sp):
    print(i)
