season = input()
group = input()
count_students = int(input())
count_nights = int(input())
sport = ' '
discount = 0

if season == 'Winter':
    if group == 'girls':
        price_night = 9.6
        sport = 'Gymnastics'
    elif group == 'boys':
        price_night = 9.6
        sport = 'Judo'
    elif group == 'mixed':
        price_night = 10
        sport = 'Ski'

elif season == 'Spring':
    if group == 'girls':
        price_night = 7.2
        sport = 'Athletics'
    elif group == 'boys':
        price_night = 7.2
        sport = 'Tennis'
    elif group == 'mixed':
        price_night = 9.5
        sport = 'Cycling'

elif season == 'Summer':
    if group == 'girls':
        price_night = 15
        sport = 'Volleyball'
    elif group == 'boys':
        price_night = 15
        sport = 'Football'
    elif group == 'mixed':
        price_night = 20
        sport = 'Swimming'

if count_students>=50:
    discount = 0.5
elif 20<=count_students<50:
    discount = 0.15
elif 10<=count_students<20:
    discount = 0.05

all_price=count_nights*price_night*count_students*(1-discount)
print(f'{sport} {all_price:.2f} lv.')
