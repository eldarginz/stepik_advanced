def isoif_flaviya(n, k):
    rez = 0
    for i in range(1, n+1):
        rez = (rez+k) % i
    return (rez+1)


n = int(input())
k = int(input())

print(isoif_flaviya(n, k))
