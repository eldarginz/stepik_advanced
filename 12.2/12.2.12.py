import random
n = int(input())
friends = [input() for _ in range(n)]
friends2 = friends.copy()

random.shuffle(friends2)

while friends == friends2:
    random.shuffle(friends2)

for i in range(n):
    print(f'{friends[i]} - {friends2[i]}')
