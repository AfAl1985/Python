def calculate_tax(price, tax):
    total = price + (price * tax / 100)
    print(total)
    return  total

myPrice = float(input('Enter the price: '))
myTax = int(input('Enter the tax(%): '))

totalPrice = calculate_tax(myPrice, myTax)

newTax = int(input('Enter the tax(%): '))
totalPrice = calculate_tax(totalPrice, newTax)

print('Total price: ', totalPrice)