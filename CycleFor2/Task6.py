print("Задача 6. Стипендия")
# Что нужно сделать
# Ежемесячная стипендия студента составляет educational_grant рублей,
# а расходы на проживание превышают стипендию и составляют expenses рублей в месяц.
# Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца.
# Обратите внимание, что каждый месяц цены увеличиваются на 3% относительного прошлого месяца.
# Составьте программу расчёта суммы денег, которую необходимо получить у родителей один раз в начале обучения,
# чтобы можно было прожить учебный год (десять месяцев), используя только эти деньги и стипендию.
# Пример
# Введите стипендию: 10000
# Введите расходы на проживание: 12000
# месяц траты 12000 не хватает 2000
# месяц траты 12360.0 не хватает 4360.0
# месяц траты 12730.8 не хватает 7090.8
# месяц траты 13112.7 не хватает 10203.52
# месяц траты 13506.1 не хватает 13709.63
# месяц траты 13911.2 не хватает 17620.92
# месяц траты 14328.6не хватает 21949.55
# месяц траты 14758.4 не хватает 26708.03
# месяц траты 15201.2 не хватает 31909.27
# месяц траты 15657.2 не хватает 37566.55
# Нужно попросить у родителей 37566.55 рублей

scolarship = int(input("Enter the scolarship: "))
expenses = int(input("Enter the living expenses: "))
summ = 0

for line in range(1, 12 -1):
    count = (scolarship - expenses) * -1
    print("month expenses: ", round(expenses), "Shortage of money: ", round(count))
    expenses *= 1.03
    summ = summ + count
print("It's neccesary to ask for parents: ", round(summ))