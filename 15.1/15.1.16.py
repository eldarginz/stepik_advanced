def matrix(n=1, m=None, value=0):
    if not m:
        m = n
    elif n == 1 and not m:
        m = 1
    rez = [([value for i in range(m)]) for j in range(int(n))]
    return (rez)
