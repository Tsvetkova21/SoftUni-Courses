type_fuel = input()
fuel_litres = float(input())
club_card = input()
discount = 0

if type_fuel == 'Gasoline':
    price_liter = 2.22
    if club_card == 'Yes':
        price_liter=price_liter - 0.18
elif type_fuel == 'Diesel':
    price_liter = 2.33
    if club_card == 'Yes':
        price_liter=price_liter - 0.12
elif type_fuel == 'Gas':
    price_liter = 0.93
    if club_card == 'Yes':
        price_liter=price_liter - 0.08

if 20 <= fuel_litres <= 25:
    discount = 0.08
elif fuel_litres > 25:
    discount = 0.1

all_price = fuel_litres*price_liter*(1-discount)
print(f'{all_price:.2f} lv.')

