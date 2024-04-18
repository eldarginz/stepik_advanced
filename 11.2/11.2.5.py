def merge(values):      # values - это список словарей
    rez = {}
    for i in values:
        for j in i:
            rez.setdefault(j, set()).add(i[j])
    return (rez)
