import math

distance = float(input("Enter the distance: "))
angle = float(input("Enter the degree: "))

angle /= 57.2958
x = math.cos(angle) * distance
y = math.sin(angle) * distance

print("Coordinate: ", x, ',', y)