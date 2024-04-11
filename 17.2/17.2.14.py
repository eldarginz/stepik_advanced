file = open('numbers.txt', 'r')
linestxt = file.readlines()
print(int(linestxt[0])+int(linestxt[1]))
file.close()
