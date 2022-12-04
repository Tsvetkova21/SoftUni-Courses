quantity_food_in_kilograms = float(input())*1000
quantity_hay_in_kilograms = float(input())*1000
quantity_cover_in_kilograms = float(input())*1000
quineas_weight_in_kilograms = float(input())*1000
flag = False
for day in range(1, 31):
    quantity_food_in_kilograms-=300
    if day% 2 == 0:
        quantity_hay_in_kilograms-=quantity_food_in_kilograms*0.05
    if day% 3 == 0:
        quantity_cover_in_kilograms-=quineas_weight_in_kilograms/3
    if quantity_food_in_kilograms <= 0 or quantity_hay_in_kilograms <=0 or quantity_cover_in_kilograms<=0:
        flaf = True
        break
if not flag:
    print(f"Everything is fine! Puppy is happy! Food: {quantity_food_in_kilograms/1000:.2f}, Hay: {quantity_hay_in_kilograms/1000:.2f}, Cover: {quantity_cover_in_kilograms/1000:.2f}.")
else:
    print("Merry must go to the pet store!")