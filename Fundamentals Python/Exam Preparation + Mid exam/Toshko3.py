import math


def info_cars(car):
    taxes_agency =0
    kilometers_distance = 0
    for element in car:
        type, years_paid, kilometers = element.split(" ")
        if type == 'family':
            all_tax= 50-5*int(years_paid)
            if float(kilometers)>=3000:
                kilometers_distance =math.floor(float(kilometers)/3000)
                all_tax+=kilometers_distance*12
            print(f"A {type} car will pay {all_tax:.2f} euros in taxes.")
            taxes_agency+=all_tax

        elif type == 'heavyDuty':
            all_tax = 80 -8*int(years_paid)
            if float(kilometers) >= 9000:
                kilometers_distance =math.floor(float(kilometers) / 9000)
                all_tax += kilometers_distance * 14
            print(f"A {type} car will pay {all_tax:.2f} euros in taxes.")
            taxes_agency += all_tax


        elif type =='sports':
            all_tax = 100 - 9 * int(years_paid)
            if float(kilometers) >= 2000:
                kilometers_distance = math.floor(float(kilometers) / 2000)
                all_tax += kilometers_distance * 18
            print(f"A {type} car will pay {all_tax:.2f} euros in taxes.")
            taxes_agency += all_tax

        else:
            print('Invalid car type.')
    print(f"The National Revenue Agency will collect {taxes_agency:.2f} euros in taxes.")
string_input = input()
vehicles = string_input.split(">>")
info_cars(vehicles)

