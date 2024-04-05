ip = [int(i) for i in input().split('.') if i.isdigit()]

len_check = False
firstoktet = False
secondoktet = False
thirdoktet = False
fouroktet = False

if len(ip) == 4:
    len_check = True
    if 0 <= ip[0] <= 255:
        firstoktet = True

    if 0 <= ip[1] <= 255:
        secondoktet = True

    if 0 <= ip[2] <= 255:
        thirdoktet = True

    if 0 <= ip[3] <= 255:
        fouroktet = True

print(all([len_check, firstoktet, secondoktet, thirdoktet, fouroktet]))
