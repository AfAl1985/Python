word = input('Enter any word: ')
replace_num = int(input('A number of a symbol : '))
replace_sym = input('Replaced symbol: ')

sym_list = []
for sym in word:
    sym_list.append(sym)
sym_list[replace_num - 1] = replace_sym

for i in sym_list:
    print(i, end='')

print(sym_list)