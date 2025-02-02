import math
import time

print("Задача 3. Аналог Steam")
# Вы пишете программу-инсталлятор для компьютерной игры.
# Пока инсталлятор скачивает обновление, для пользователя необходимо отображать количество скачанных процентов,
# чтобы он понимал, успеет ли заварить чай, прежде чем завершится процесс.
# Каждое обновление игры требует разного количества мегабайт,
# при этом у разных игроков разная скорость интернет-соединения.
# Напишите программу, принимающую на вход размер файла обновления в мегабайтах и скорость интернет-соединения
# в мегабайтах в секунду. Для каждой секунды программа должна рассчитывать
# и выводить на экран процент скачанного объёма до тех пор, пока скачивание не завершится.
# В конце программа должна показать, сколько секунд заняло скачивание обновления. Обеспечьте контроль ввода.
# Пример:
# Укажите размер файла для скачивания: 123
# Какова скорость вашего соединения: 27
# Прошло 1 сек. Скачано 27 из 123 Мб (22%)
# Прошло 2 сек. Скачано 54 из 123 Мб (44%)
# Прошло 3 сек. Скачано 81 из 123 Мб (66%)
# Прошло 4 сек. Скачано 108 из 123 Мб (88%)
# Прошло 5 сек. Скачано 123 из 123 Мб (100%)

# size = int(input("Enter a size of the file: "))
# steam = int(input("Enter the speed of your connection: "))
# clock = 0
#
# for line in range(0, size, steam):
#     if line <= size:
#         clock += 1
#         line += steam
#         # count = round((line / size) * 100)
#         # time.sleep(1)
#         print("Time passed: ", clock, "sec.", "Downloaded ", line , "out of ", size, "mb", "(", round((line / size) * 100),"%)")
#     else:
#         print("Time passed: ", clock, "sec.", "Downloaded ", size , "out of ", size, "mb", "("'100%'")")

mb = int(input('A size of the file: '))
speed = int(input('Stream of the connection: '))
time = math.ceil(mb / speed)
total = speed
percent = math.ceil(speed / mb * 100)

for i in range(1, time+1):
  print('Passed time', i, 'sec. Downloaded:', total, 'out of', mb, '(', percent, '%)')
  total += speed
  percent += math.ceil(speed / mb * 100)
  if total > mb:
    total = mb
  if percent > 100:
    percent = 100