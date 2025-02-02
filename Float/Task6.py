print("Задача 6. Ход конём")
# В рамках разработки шахматного ИИ стоит новая задача:
# по заданным вещественным координатам коня и точки программа должна определить,
# может ли конь ходить в эту точку. Используйте как можно меньше конструкций if и логических операторов.
# Обеспечьте контроль ввода.
# Пример:
# Введите местоположение коня:
# 0.071
# 0.118
# Введите местоположение точки на доске:
# 0.213
# 0.068
# Конь в клетке (0, 1). Точка в клетке (2, 0).
# Да, конь может ходить в эту точку.

print("Enter a location of a horse: ")
a = float(input("point a: "))
b = float(input("point b: "))
print("Enter a location on the board: ")
c = float(input("point c: "))
d = float(input("point d: "))

x = int(a * 10)
y = int(b * 10)
x1 = int(c * 10)
y1 = int(d * 10)

diff_horse = abs(x - x1)
diff_board = abs(y - y1)
print(x,y)
print(x1, y1)
if diff_horse == 1 and diff_board == 2 or diff_horse == 2 and diff_board == 1:
    print("Yes")
else:
    print("No")










