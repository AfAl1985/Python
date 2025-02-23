word = input('Enter any word: ')
replace_num = int(input('A number of a symbol : '))
replace_sym = input('Replaced symbol: ')

new_word = ''

count = 0
for sym  in word:
    count += 1
    if replace_num != count:
        new_word += sym
    else:
        new_word += replace_sym

print(new_word)