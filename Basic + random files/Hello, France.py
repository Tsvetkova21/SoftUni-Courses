collection= input().split("|")
budget = int(input())
price_item = 0
new_prices=[]
profit=0
total=0
for elements in collection:
    if 'Clothes->' in elements:
        price_item = float((elements.strip('Clothes->')))
        if price_item<=50 and budget>=price_item:
            budget-=price_item
            new_prices.append(price_item*1.4)
            profit+=0.4*price_item
            total+=price_item*1.4
    if 'Shoes->' in elements:
        price_item = float(elements.strip('Shoes->'))
        if price_item<=35 and budget>=price_item:
            budget-=price_item
            new_prices.append(price_item*1.4)
            profit += 0.4 * price_item
            total += price_item*1.4
    if 'Accessories->' in elements:
        price_item = float(elements.strip('Accessories->'))
        if price_item<=20.5 and budget>=price_item:
            budget-=price_item
            new_prices.append(price_item*1.4)
            profit += 0.4 * price_item
            total += price_item*1.4

new_prices = ['{:.2f}'.format(elem) for elem in new_prices]
print(*new_prices, sep=" ")
print(f'Profit: {profit:.2f}')
if total+budget>=150:
    print('Hello, France!')
else:
    print('Not enough money.')