from math import hypot


def otnulya(*args):
    for i in args:
        return hypot(i[0], i[1])


points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2),
          (0, 0), (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)]

points.sort(key=otnulya)

print(points)
