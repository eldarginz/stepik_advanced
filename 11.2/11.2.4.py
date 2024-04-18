def build_query_string(params):
    list = []
    for i in params:
        list.append(f'{i}={params[i]}')

    list.sort()
    if len(list) == 1:
        a = list[0]
        return (a)
    else:
        a = '&'.join((map(str, list)))
        return (a)
