def kanobu(a, b):
    if a == 'камень' and b == 'ножницы':
        return True
    elif a == 'ножницы' and b == 'бумага':
        return True
    elif a == 'бумага' and b == 'камень':
        return True
    elif a == b:
        return None
    else:
        return False


a = input().lower()  # Тимур
b = input().lower()  # Руслан

if kanobu(a, b) == True:
    print('Тимур')
elif kanobu(a, b) == False:
    print('Руслан')
else:
    print('ничья')
