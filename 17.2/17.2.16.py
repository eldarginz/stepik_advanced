file = open('prices.txt', 'r', encoding='utf-8')
sum = 0
for line in file:
    a, b, c = map(str, line.split('\t'))
    sum += int(b)*int(c)
print(sum)
file.close()
