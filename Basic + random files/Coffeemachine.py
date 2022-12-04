drink = input()
sugar = input()
count_drinks = int(input())

if drink == 'Espresso':

    if sugar == 'Without':

        price=0.9*0.65*count_drinks

    elif sugar == 'Normal':

        price=1*count_drinks

    elif sugar == 'Extra':

        price=1.2*count_drinks

    if count_drinks>=5 :

        price=price*0.75

if drink == 'Cappuccino':

    if sugar == 'Without':

        price=1*0.65*count_drinks

    elif sugar == 'Normal':

        price=1.2*count_drinks

    elif sugar == 'Extra':

        price=1.6*count_drinks

if drink == 'Tea':

    if sugar == 'Without':

        price=0.5*0.65*count_drinks

    elif sugar == 'Normal':

        price=0.6*count_drinks

    elif sugar == 'Extra':

        price=0.7*count_drinks

if price>15:

    price=price*0.8
print(f'You bought {count_drinks} cups of {drink} for '
      f'{price:.2f} lv.')