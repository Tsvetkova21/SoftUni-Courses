count_hr = int(input())
count_r = int(input())
count_t = int(input())
season = input()
day_off = input()

if season == 'Spring' or season == 'Summer':
    price_hr = 2
    price_r = 4.1
    price_t = 2.5
elif season == 'Autumn' or season == 'Winter':
    price_hr = 3.75
    price_r = 4.5
    price_t = 4.15

if day_off == 'Y':
    if season == 'Spring' or season == 'Summer':
        price_hr = 2*1.15
        price_r = 4.1*1.15
        price_t = 2.5*1.15
    elif season == 'Autumn' or season == 'Winter':
        price_hr = 3.75*1.15
        price_r = 4.5*1.15
        price_t = 4.15*1.15

count_fl=count_r+count_hr+count_t
all_price=price_hr*count_hr + price_r*count_r + price_t*count_t

if count_t>7 and season == 'Spring':
    all_price=all_price*0.95

if count_r>= 10 and season == 'Winter':
    all_price=all_price*0.9

if count_fl>20:
    all_price=all_price*0.8

all_price=all_price+2
print(f'{all_price:.2f}')