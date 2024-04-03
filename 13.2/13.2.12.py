from fractions import Fraction
from math import gcd

n = int(input())

a = n // 2
b = n - a

while gcd(a, b) != 1:
    a -= 1
    b += 1

print(Fraction(a, b))
