#a,b = int(input()), int(input())+1
#data = [i for i in range(a,b) if '0' not in str(i)]
##k = []
##for i in data:
##    if all(i%int(x)==0 for x in str(i)):
##        k.append(i)
##print(k)
#
#print(*list(i for i in data if all(i%int(x) == 0 for x in str(i))))

print(*list(i for i in [i for i in range(int(input()),int(input())+1) if '0' not in str(i)] if all(i%int(x) == 0 for x in str(i))))
