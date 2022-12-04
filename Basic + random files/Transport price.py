km = int(input())
day_or_night = input()
first_price = 0

if km < 20:
    if day_or_night == 'day':
        price=0.79
        first_price=0.7
    if day_or_night == 'night':
        price=0.9
        first_price = 0.7
if 20 <= km < 100:
    price = 0.09

if 100 <= km:
    price=0.06

all_price=first_price+price*km
print(f'{all_price:.2f}')