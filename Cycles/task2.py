from itertools import count

print('Задача 2. Слишком большие числа')

# У неудачливого бухгалтера всё опять идёт наперекосяк: ему приносят такие большие счета,
# что числа не помещаются на бумаге.

# Напишите программу, которая считала бы, сколько цифр во вводимом числе.
# Учтите, что программа должна получать только положительные числа и что число 0 имеет одну цифру.

# Пример 1
# Введите число: 58
# Кол-во цифр в числе: 2

# Пример 2
# Введите число: 0
# Кол-во цифр в числе: 1

number = int(input("enter any number starts from 0: "))
count = 0

if number == 0:
    count = 1
else:
    number = number
    while number > 0:
        number //= 10
        count += 1
print("number of digits: ",count)









