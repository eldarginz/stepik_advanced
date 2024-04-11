file = open('nums.txt', 'r')

a,b = map(int, file.read().split())
print(a+b)

file.close()
