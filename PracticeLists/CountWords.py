words_list =[]
counts = [0, 0, 0]

for i in range(3):
    print('Enter', i + 1, 'word:', end=' ')
    word = input()
    words_list.append(word)

text = input('Word of the list: ')
while text != 'end':
    for index in range(3):
        if words_list[index] == text:
            counts[index] += 1
    text = input('Word of the list: ')

print('\nCount words in the text')
for i in range(3):
    print(words_list[i], ':', counts[i])