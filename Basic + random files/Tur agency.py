city_name = input()
package = input()
VIP_discount = input()
days_stay = int(input())
discount_day = 0
price_1_day = 0
condition = False
if days_stay < 1:
    print('Days must be positive number!')
elif days_stay >= 1:
    if days_stay > 7:
        days_stay = days_stay - 1

    if city_name == 'Bansko' or city_name == 'Borovets':
        if package == 'withEquipment':
            price_1_day = 100
            if VIP_discount == 'yes':
                discount_day = 0.1
            if VIP_discount != 'yes' and VIP_discount != 'no':
                print('Invalid input!')
        elif package == 'noEquipment':
            price_1_day = 80
            if VIP_discount == 'yes':
                discount_day = 0.05
            if VIP_discount != 'yes' and VIP_discount != 'no':
                print('Invalid input!')
        else:
            print('Invalid input!')
            condition= True
    elif city_name == 'Varna' or city_name == 'Burgas':

        if package == 'withBreakfast':
            price_1_day = 130
            if VIP_discount == 'yes':
                discount_day = 0.12
            if VIP_discount != 'yes' and VIP_discount != 'no':
                print('Invalid input!')
        elif package == 'noBreakfast':
            price_1_day = 100
            if VIP_discount == 'yes':
                discount_day = 0.07
            if VIP_discount != 'yes' and VIP_discount != 'no':
                print('Invalid input!')
        else:
            print('Invalid input!')
            condition = True
    else:
        print('Invalid input!')
        condition = True
    if not condition:
        all_price = (price_1_day - price_1_day * discount_day) * days_stay
        print(f'The price is {all_price:.2f}lv! Have a nice time!')


