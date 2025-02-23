# User enters a list of N figures and divisor K. Write a code which displays a sum of indexes of the list which
# equals to a divisor K.

num = int(input('Enter a number of figures: '))
numbers = []
for _ in range(num):
    N = int(input('Enter a number: '))
    numbers.append(N)
print(numbers)

summ = 0
div = int(input('Enter a divisor: '))
print()

for i in  range(num):
    if numbers[i] % div == 0:
        summ += i
    print(numbers[i], i)
print(summ)

# newList = [x / div for x in numbers]
# print(newList)
# for i, val in enumerate(newList, start=1):
#     if val < 1:
#         print(f'N {i} => {val}')





