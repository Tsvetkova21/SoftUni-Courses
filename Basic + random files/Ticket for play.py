budget = float(input())
category = input()
count_people_group = int(input())

if category == 'VIP':
    price = 499.99
elif category == 'Normal':
    price = 249.99

if 1<=count_people_group<=4:
    percentage_transport=0.75
elif 5<=count_people_group<=9:
    percentage_transport=0.6
elif 10<=count_people_group<=24:
    percentage_transport=0.5
elif 25<=count_people_group<=49:
    percentage_transport=0.4
elif count_people_group>=50:
    percentage_transport=0.25

all_price=count_people_group*price
left_price = budget*(1-percentage_transport)
diff=abs(left_price-all_price)

if left_price>= all_price:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f'Not enough money! You need {diff:.2f} leva.')