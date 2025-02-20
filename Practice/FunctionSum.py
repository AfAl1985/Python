def count_two(number):
    res = 0
    for i in range(1, number +1):
        res += i
    print("Sum from 1 to",number,"-",res)

    count = 0
    for l in range(1, res +1):
        count += l
    print("Sum from 1 to",res,"-", count)

number = int(input("Enter the number: "))

count_two(number)







