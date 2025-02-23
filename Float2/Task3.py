print("Задача 3. Число наоборот 2")
# Что нужно сделать
# Пользователь вводит два числа: N и K.
# Напишите программу, которая заменяет каждое число на число,
# которое получается из исходного записью его цифр в обратном порядке, затем складывает их,
# снова переворачивает и выводит ответ на экран.
# Пример:
# Введите первое число: 102
# Введите второе число: 123
# Первое число наоборот: 201
# Второе число наоборот: 321
# Сумма: 522
# Сумма наоборот: 225
def contrary(first, second):
    reversed_sum = first + second
    rev = 0
    rev2 = 0
    while first != 0:
        digit = first % 10
        rev = rev * 10 + digit
        first //= 10
    print("first reversed number:", rev)
    while second != 0:
        digit = second % 10
        rev2 = rev2 * 10 + digit
        second //= 10
    print("second reversed number:", rev2)
    print("Sum: ", rev + rev2)
    print("Reversed sum: ", reversed_sum)

first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))

contrary(first, second)