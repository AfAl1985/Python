import random

age = int(input("Enter the age: "))
temp = random.randint(35,37)
summ = float(age * 1.5 * temp)

print(age, '*', 1.5, '*', temp)
print(summ)
