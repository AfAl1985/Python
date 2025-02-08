def maimMenu():
    print('1. Do something good')
    print('2. Do something bad')
    choice = int(input("What's your choice: "))
    if choice == 1:
        good()
    elif choice == 2:
        bad()
    else:
        print('Error')
        maimMenu()

def good():
    print('Everything is OK')
    input('Push any button to return: ')
    maimMenu()
def bad():
    print("That's bad")

maimMenu()