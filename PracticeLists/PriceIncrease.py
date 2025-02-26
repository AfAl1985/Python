def get_hugher_price(percent, price):
    return  round(price * (1 + percent / 100), 2)

prices_now = [1.09, 23.56, 57.84, 4.56, 6.78]
first = int(input('First year increase: '))
second = int(input('Second year increase: '))

prices_first = [get_hugher_price(first, i_price) for  i_price in prices_now]
prices_second = [get_hugher_price(second, i_price) for  i_price in prices_first]

print('Summ of prices every year:', round(sum(prices_now), 2), round(sum(prices_first), 2), round(sum(prices_second), 2))