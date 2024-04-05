# abscissas = [float(i) for i in input().split()]
# ordinates = [float(i) for i in input().split()]
# applicates = [float(i) for i in input().split()]
# R = 2
# l = zip(abscissas, ordinates, applicates)
#
# rez = list(map(lambda x,y,z: x**2+y**2+z**2<=4, abscissas,ordinates,applicates))
#
# print(all(rez))

print(all(list(map(lambda x, y, z: x**2+y**2+z**2 <= 4, [float(i) for i in input().split()], [
      float(i) for i in input().split()], [float(i) for i in input().split()]))))
