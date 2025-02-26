print('Task: harmful software')

first = input('Enter a sentence: ')
second = input('Enter a sentence: ')

first_count = first.count('!') + first.count('?')
second_count = second.count('!') + second.count('?')
if first_count < second_count:
    first, second = second, first

print(first + second)