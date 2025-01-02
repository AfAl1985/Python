print('Задача 4. Вклады')

# Вклад в банке составляет X рублей.
# Ежегодно он увеличивается на P процентов,
# после чего дробная часть копеек отбрасывается.

# Определите, через сколько лет вклад составит не менее Y рублей.

# Напишите программу,
# которая по данным числам X, Y, P определяет,
# сколько лет пройдёт, прежде чем сумма достигнет значения Y.

# Пример
# Вклад в банке: 50
# Проценты: 5
# Порог вклада: 60
# 1 год. 50 + 5% = 52
# 2 год. 52 + 5% = 54
# 3 год. 54 + 5% = 56
# 4 год. 56 + 5% = 58
# 5 год. 58 + 5% = 60
# Кол-во лет для достижения порога: 5

bank_deposit = int(input("Enter the sum: "))
percentage = int(input("Enter %: "))
point = int(bank_deposit * 1.2)
years = 0

print("desirable income: ", point)
while bank_deposit < point:
    bank_deposit *= 1 + percentage / 100
    years += 1
    if bank_deposit == point:
        break
    print(years, "year", bank_deposit, "+", percentage,"%", "=", bank_deposit)
print("Period: ", years,"years")

