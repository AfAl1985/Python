nums_list = []
N = int(input('Enter a number of figures: '))
for _ in range(N):
    num = int(input('Enter a number: '))
    nums_list.append(num)

max = 0
min = 1

for i in nums_list:
    if max < i:
        max = i
    if min > i:
        min = i

print(max)
print(min)