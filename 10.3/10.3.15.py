lst = [word.strip('.,!?:;-') for word in input().lower().split()]

result = {}
result2 = {}

s_word = set(lst)

for word in s_word:
    result[word] = lst.count(word)

mx1 = min(result.values())

for key, value in result.items():
    if value == min(result.values()):
        result2[key] = result2.get(key, value)

mx2 = min(result2)

print(mx2)
