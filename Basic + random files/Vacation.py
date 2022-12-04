budget = float(input())
season = input()

if budget<= 1000:
    place = 'Camp'
    if season == 'Summer':
        location = 'Alaska'
        price=0.65*budget
    elif season == 'Winter':
        location = 'Morocco'
        price = 0.45 * budget
if 1000< budget <= 3000:
    place = 'Hut'
    if season == 'Summer':
        location = 'Alaska'
        price=0.8*budget
    elif season == 'Winter':
        location = 'Morocco'
        price = 0.60 * budget
if budget>3000:
    place = 'Hotel'
    price = 0.9 * budget
    if season == 'Summer':
        location = 'Alaska'
    elif season == 'Winter':
        location = 'Morocco'
print(f'{location} - {place} - {price:.2f}')