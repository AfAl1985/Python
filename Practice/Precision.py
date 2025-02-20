import math

precision = float(input("Precision: "))

result = 0
i = 0
addMember = 1

while addMember > precision:
    addMember = 1 / math.factorial(i)
    result += addMember
    i += 1

print(result)
print(math.e)