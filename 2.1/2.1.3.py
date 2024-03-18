m = float(input())
h = float(input())

imt = m/h**2

if imt < 18.5:
    print('Недостаточная масса')
elif imt > 25:
    print('Избыточная масса')
else:
    print('Оптимальная масса')
