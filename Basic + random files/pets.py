import math

days = int(input())
food_left= int (input())
food_dog_day = float(input())
food_cat_day = float(input())
food_turtle_day = float(input())

food_needed = food_dog_day*days+food_cat_day*days+food_turtle_day/1000*days

diff=abs(food_needed - food_left)

if food_needed<=food_left:
    print(f"{math.floor(diff)} kilos of food left.")

if food_needed > food_left:
    print(f"{math.ceil(diff)} more kilos of food are needed.")