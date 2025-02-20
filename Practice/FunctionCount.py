def numeral_count(number):
    if number < 0:
        print('This is a negative number: ')
        return  0

    count = 0
    while number > 0:
        number //= 10
        count += 1

    return  count

firstTask = int(input('Enter the first number: '))
secondTask = int(input('Enter the second number: '))

firstNumeral = numeral_count(firstTask)
secondNumeral = numeral_count(secondTask)

if firstNumeral > secondNumeral:
    print('There are more digits in the first number')
elif firstNumeral < secondNumeral:
    print('There are more digits in the second number')
else:
    print("Equvivalent")