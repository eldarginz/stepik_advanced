import random
file = open('lines.txt', 'r')
linestxt = file.readlines()
print(linestxt[random.randint(1, len(linestxt))])
file.close()
