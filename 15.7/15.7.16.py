from functools import reduce


def evaluate(coefficients, x): return reduce(
    lambda s, a: s * x + a, coefficients, 0)


print(evaluate([*map(int, input().split())], int(input())))
