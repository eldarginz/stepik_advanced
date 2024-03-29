first_word = {}
second_word = {}

for word in input().lower():
    if word.isalpha():
        first_word[word] = first_word.get(word, 0) + 1

for word in input().lower():
    if word.isalpha():
        second_word[word] = second_word.get(word, 0) + 1

for i in first_word:
    if i in second_word:
        if int(first_word[i]) != second_word[i]:
            print('NO')
            quit()
    elif i not in second_word:
        print('NO')
        quit()

print('YES')
