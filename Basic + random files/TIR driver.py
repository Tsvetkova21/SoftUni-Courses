season = input()
km_month = float(input())
price_km = 0

if km_month<= 5000:
    if season == 'Spring' or season == 'Autumn':
        price_km = 0.75
    elif season == 'Summer':
        price_km = 0.9
    elif season == 'Winter':
        price_km = 1.05
elif 5000<km_month<= 10000:
    if season == 'Spring' or season == 'Autumn':
        price_km = 0.95
    elif season == 'Summer':
        price_km = 1.1
    elif season == 'Winter':
        price_km = 1.25
elif 10000<km_month<= 20000:
    price_km = 1.45

all_price=price_km*4*km_month*0.9

print(f'{all_price:.2f}')