def triangle():
    star = 1
    for line in range(5):
        print(' ' * (5 - line - 1), end= '')
        print('*' * star)
        star += 2
def rectangle():
    for line in range(5):
        if line == 0 or line == 4:
            print('*' * 5)
        else:
            print('*' + ' ' * 3 + '*')

choice = int(input("Make your choice: 1 - triangle, 2 - rectangle"))
if choice == 1:
    triangle()
elif choice == 2:
    rectangle()
else:
    print('Error')