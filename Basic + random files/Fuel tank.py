type_fuel = input()
fuel_litres = float(input())
final_fuel=type_fuel.lower()

if type_fuel == 'Diesel' or type_fuel == 'Gasoline'\
        or type_fuel == 'Gas':
    if fuel_litres>= 25:
        print(f"You have enough {(final_fuel)}.")
    else:
        print(f"Fill your tank with {(final_fuel)}!")
else:
    print("Invalid fuel!")