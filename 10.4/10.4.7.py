crypted = input().split
crypted_dict = {}
buffer = {}

for word in crypted:
    crypted_dict[word] = crypted_dict.get(word, 0) + 1

key = {}

for i in range(int(input())):
    letter, count = input().split(': ')
    key[int(count)] = letter

print(key)
print(crypted_dict)

for word in crypted_dict:
    buffer[crypted_dict[word]] = word

print(buffer)