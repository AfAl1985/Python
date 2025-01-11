import random

print('Задача 5. Игра «Угадай число»')

# Папа-программист любит придумывать для сына небольшие компьютерные игры.

# Напишите программу-игру, в которой один человек загадывает число от 1 до 10,
# а другой пытается его угадать.
# Программа должна запрашивать число у пользователя до тех пор, пока тот не угадает загаданное.
# После каждой попытки выводите подсказки, больше или меньше загаданного введённое число.
# Также после отгадки выводите количество попыток.


# Пример (загадали число 7)
# Введите число: 3
# Число меньше, чем нужно. Попробуйте ещё раз!
# Введите число: 10
# Число больше, чем нужно. Попробуйте ещё раз!
# Введите число: 8
# Число больше, чем нужно. Попробуйте ещё раз!
# Введите число: 7
# Вы угадали! Число попыток: 4

uknown = random.randint(1, 100)
print(uknown)
guess = 0
attempts = 0

while uknown != guess:
    guess = int(input("Enter your number: "))
    attempts += 1
    if guess < uknown:
        print("Your number is less than guessed one, try again")
    elif guess > uknown:
        print("Your number is more than guessed one, try again")
    elif guess == uknown:
        print("You have guessed")
print("A number of attempts: ", attempts)

