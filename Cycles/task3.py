print('Задача 3. Обычный день на работе')

# Максим программирует целый день на работе и вечером идёт домой.
# Каждый час начальство кидает ему несколько задач,
# которые нужно решить до следующего рабочего часа.
# И вдобавок каждый час Максиму звонит супруга.
# Он знает, что если он возьмёт трубку, то жена попросит зайти вечером в магазин.

# Напишите программу,
# в которой считается, сколько задач выполнил Максим за день (8 часов).
# Если он хоть раз взял трубку,
# то в конце дополнительно выводите сообщение: «Нужно зайти в магазин».
# Дополнительно: сделайте так, чтобы жена не звонила Максиму, если он уже хотя бы раз ответил на звонок в течение рабочего дня.

# Пример  1
# (основная задача):
# Начался восьмичасовой рабочий день.
# 1-й час
# Сколько задач решит Максим? 1
# Звонит жена. Взять трубку? (1 — да, 0 — нет): 0
# 2-й час
# Сколько задач решит Максим? 2
# Звонит жена. Взять трубку? (1 — да, 0 — нет): 0
# 3-й час
# Сколько задач решит Максим? 3
# Звонит жена. Взять трубку? (1 — да, 0 — нет): 0
# 4-й час
# Сколько задач решит Максим? 4
# Звонит жена. Взять трубку? (1 — да, 0 — нет): 1
# 5-й час
# Сколько задач решит Максим? 5
# Звонит жена. Взять трубку? (1 — да, 0 — нет): 0
# 6-й час
# Сколько задач решит Максим? 1
# Звонит жена. Взять трубку? (1 — да, 0 — нет): 0
# 7-й час
# Сколько задач решит Максим? 2
# Звонит жена. Взять трубку? (1 — да, 0 — нет): 1
# 8-й час
# Сколько задач решит Максим? 3
# Звонит жена. Взять трубку? (1 — да, 0 — нет): 0
# Рабочий день закончился. Всего выполнено задач: 21
# Нужно зайти в магазин.


# Пример 2
# (с дополнительным условием)
# Начался восьмичасовой рабочий день.
# 1-й час
# Сколько задач решит Максим? 1
# Звонит жена. Взять трубку? (1 — да, 0 — нет): 0
# 2-й час
# Сколько задач решит Максим? 2
# Звонит жена. Взять трубку? (1 — да, 0 — нет): 1
# 3-й час
# Сколько задач решит Максим? 1
# 4-й час
# Сколько задач решит Максим? 2
# 5-й час
# Сколько задач решит Максим? 3
# 6-й час
# Сколько задач решит Максим? 4
# 7-й час
# Сколько задач решит Максим? 1
# 8-й час
# Сколько задач решит Максим? 1
# Рабочий день закончился. Всего выполнено задач: 15
# Нужно зайти в магазин.

print("Workday has begun")
count_hours = 0
total_tasks = 0
calls = True
while count_hours < 8:
    count_hours += 1
    print("It's", count_hours, "-", "hour")
    tasks = int(input("Enter the number: "))
    total_tasks += tasks
    if calls == 1:
        calls = int(input("The wife is calling. Answer or not? 1 - yes, 0 - no "))
        continue
        if calls == False:
            break
print("The workday is over. You have completed: ",total_tasks)
print("Go shopping")










