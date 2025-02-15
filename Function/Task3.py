print("Задача 4. Апгрейд калькулятора")
#  Что нужно сделать
# Степан использует калькулятор для расчёта суммы и разности чисел,
# но на работе ему требуются не только обычные арифметические действия.
# Он ничего не хочет делать вручную, поэтому решил немного расширить функционал калькулятора.
# Напишите программу, запрашивающую у пользователя число и действие,
# которое нужно сделать с числом: вывести сумму его цифр, максимальную или минимальную цифру.
# Каждое действие оформите в виде отдельной функции, а основную программу зациклите.
# Запрошенные числа должны передаваться в функции суммы, максимума и минимума при помощи аргументов.
def sum(numberA):
    res = 0
    while numberA > 0:
        res += (numberA % 10)
        numberA //= 10
    print(res)

def max(numberA):
    maxD = -1
    while numberA > 0:
        if numberA % 10 > maxD:
            maxD = numberA % 10
        numberA //= 10
    print(maxD)

def min(numberA):
    min = 10
    while numberA > 0:
        if numberA % 10 < min:
            min = numberA % 10
        numberA //= 10
    print(min)


choice = int(input("Make your choice: 1 - sum: , 2 - max: , 3 - min: "))
numberA = int(input("Enter the number: "))
if choice == 1:
    sum(numberA)
elif choice == 2:
    max(numberA)
else:
    min(numberA)
