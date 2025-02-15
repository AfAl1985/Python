import math

print("Задача 6. НОД")
# Что нужно сделать
# Напишите функцию, вычисляющую наибольший общий делитель двух чисел.
def GCD(first, second):
    first = int(input("Enter the first number: "))
    second = int(input("Enter the second number: "))

    while first != 0 and second != 0:
        if first > second:
            first = first % second
        else:
            second = second % first
    print(first + second)
GCD(first= '', second= '')