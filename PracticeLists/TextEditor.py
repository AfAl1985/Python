words = input('Enter a few words: ')
letters = list(words)
print(letters)
what_replace = ":"
for_what = ";"
count = 0
replace_count = 0
for i in letters:
    if i == what_replace:
        letters[count] = for_what
        replace_count += 1
    count += 1
print(end=' ')
for i in letters:
    print(i, end='')


