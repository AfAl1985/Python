print("Задача 5. Текстовый редактор")
# Что нужно сделать
# Продолжаем разрабатывать новый текстовый редактор.
# В этот раз нам поручили написать для него код, который считает,
# сколько раз в тексте встречается любая выбранная буква или цифра (а не только буквы Ы, как раньше).
# Напишите функцию count_letters(), которая принимает на вход текст и подсчитывает,
# какое в нём количество цифр K и букв N.
# Функция должна вывести на экран информацию о найденных буквах и цифрах в определённом формате.
# Пример:
# Введите текст: 100 лет в обед
# Какую цифру ищем? 0
# Какую букву ищем? Л
# Количество цифр 0: 2
# Количество букв Л: 1

def count_letters(string):
    count_letter = 0
    count_digit = 0
    letter = input("Which letter are we looking for: ")
    digit = input("Which digit are we looking for: ")
    for i in string:
        if i == letter:
            count_letter += 1
        elif i == digit:
            count_digit += 1
    print(count_letter)
    print(count_digit)

string = input('Enter any sentence: ')
count_letters(string)



