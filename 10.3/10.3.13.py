s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'

result = {}
result2 = {}
s_word = set(s.split())

for word in s_word:
    result[word] = s.count(word)

mx1 = max(result.values())

for key, value in result.items():
    if value == max(result.values()):
        result2[key] = result2.get(key, value)

mx2 = min(result2)

print(mx2)
