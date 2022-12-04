budget = float(input())
season = input()
class_car = " "
car = " "
price = 0
if budget<= 100:
    class_car = 'Economy class'
    if season == 'Summer':
        car = 'Cabrio'
        price=0.35*budget
    elif season == 'Winter':
        car = 'Jeep'
        price = 0.65 * budget
if 100< budget <= 500:
    class_car = 'Compact class'
    if season == 'Summer':
        car = 'Cabrio'
        price=0.45*budget
    elif season == 'Winter':
        car = 'Jeep'
        price = 0.80 * budget
if budget>500:
    class_car = 'Luxury class'
    car = 'Jeep'
    price = 0.9 * budget

print(f'{class_car}')
print(f'{car} - {price:.2f}')