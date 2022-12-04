budget = int(input())
price = input()
sum = 0
while price != 'End':
    price_products=int(price)
    budget -=price_products
    if budget<0:
        print('You went in overdraft!')
        break
    price = input()
else:
    print('You bought everything needed.')