text_input = input()
text_dict = {}
key = {}
d3 = {}

for word in text_input:
    text_dict[word] = text_dict.get(word, 0) + 1

for i in range(int(input())):
    a, b = input().split(': ')
    key[int(b)] = a

for z in text_dict:
    d3[z] = key[text_dict[z]]

for _ in text_input:
    print(d3[_], end='')
