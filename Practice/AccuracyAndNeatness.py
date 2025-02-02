x = float(input("Enter a horizontal placement: "))
y = float(input("Enter a vertical placement: "))

xSquare = int(x * 10)
ySquare = int(y * 10)
a = float(0.750 - x)
b = float(0.150 - y)

print("Figure located at the position: ", round(xSquare), round(ySquare))
print(round(a, 3) ,round(b, 3))


