import math


def myDistance(x ,y):
    distance = math.sqrt(x ** 2 + y ** 2)
    print(distance)

def betweenDistance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    print(distance)

choice = int(input("1 - distance to a point, 2 - distance between: "))
if choice == 1:
    x = float(input("Enter x coordinate: "))
    y = float(input("Enter y coordinate: "))
    myDistance(x, y)
elif choice == 2:
    x1 = float(input("Enter first x coordinate: "))
    y1 = float(input("Enter first y coordinate: "))
    x2 = float(input("Enter first x2 coordinate: "))
    y2 = float(input("Enter first y2 coordinate: "))
    betweenDistance(x1, y1, x2, y2)
else:
    print("Error")