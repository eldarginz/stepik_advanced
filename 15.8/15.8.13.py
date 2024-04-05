import string
password = input()
print('YES' if len(password) >= 7 and any(char for char in password if char in string.digits) and any(
    char for char in password if char in string.ascii_lowercase) and any(char for char in password if char in string.ascii_uppercase) else 'NO')
