from math import factorial


def pascal(n):
    a = []
    for i in range(n+1):
        a.append(int((factorial(n)) / (factorial(i) * factorial(n - i))))
    return a


a = int(input())

for i in range(a):
    print(*pascal(i))
