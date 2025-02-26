print("Задача 2. Функция максимума")
# Что нужно сделать
# Юра пишет различные полезные функции для Python,
# чтобы остальным программистам стало проще работать.
# Он захотел написать функцию, которая будет находить максимум из перечисленных чисел.
# Функция для нахождения максимума из двух чисел у него уже есть. Юра задумался:
# может быть, её можно как-то использовать для нахождения максимума уже от трёх чисел?
# Помогите Юре написать программу, которая находит максимум из трёх чисел.
# Для этого используйте только функцию нахождения максимума из двух чисел.
# По итогу в программе должны быть реализованы две функции:
# maximum_of_two — функция принимает два числа и возвращает одно (наибольшее из двух);
# maximum_of_three — функция принимает три числа и возвращает одно (наибольшее из трёх);
# при этом она должна использовать для сравнений первую функцию maximum_of_two.

def maxsimum_of_two(first, second):
    max = first
    if max < second:
        max = second
    print(max)

first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
maxsimum_of_two(first, second)

def maximum_of_two(first, second, third):
    max2 = third
    if max2 < first:
        max2 = first
    if max2 < second:
        max2 = second
    print(max2)

third = int(input("Enter the third number: "))
maximum_of_two(first, second, third)