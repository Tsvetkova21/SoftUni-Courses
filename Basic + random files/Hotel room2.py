month=input()
count_nights=int(input())
price_apartment=0
price_studio=0
discount_studio=0
discount_apartment=0
if month=='May' or month=='October':
    price_apartment = 65
    price_studio = 50
elif month=='June' or month=='September':
    price_apartment = 68.70
    price_studio = 75.20
elif month=='July' or month=='August':
    price_apartment = 77
    price_studio = 76
if count_nights>7 and count_nights<=14:
    if month=='May' or month=='October':
        discount_studio=0.05
elif count_nights>14 and month=='May' or month=='October':
    discount_studio=0.3
if count_nights>14 and month=='June' or month=='September':
    discount_studio=0.2
if count_nights>14:
    discount_apartment=0.1
all_price_app=(price_apartment-price_apartment*discount_apartment)*count_nights
all_price_studio=(price_studio-price_studio*discount_studio)*count_nights
print(f'Apartment: {all_price_app:.2f} lv.')
print(f'Studio: {all_price_studio:.2f} lv.')
