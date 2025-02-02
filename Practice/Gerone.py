import math

a = int(input("Enter a length of triangle: "))
b = int(input("Enter a length of triangle: "))
c = int(input("Enter a length of triangle: "))

p = (a + b + c)/2
s = math.sqrt((p * (p - a) * (p - b) * (p - c)))

print(round(s))