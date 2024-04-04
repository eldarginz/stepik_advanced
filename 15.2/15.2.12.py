def mean(*args):
    sum = 0
    cnt = 0
    for i in args:
        if type(i) in {int, float}:
            cnt += 1
            sum += i
    if sum == 0 and cnt == 0:
        return (0)
    else:
        return (sum/cnt)

