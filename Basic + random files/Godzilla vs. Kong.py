movie_budget=float(input())
movie_statist=int(input())
price_1clothing=float(input())
decor_movie=movie_budget*0.1
if movie_statist>150:
    price_clothing=price_1clothing*movie_statist*0.9
else:
    price_clothing = price_1clothing * movie_statist
all_price=decor_movie+price_clothing
if all_price>movie_budget:
    print("Not enough money!")
    need_money=all_price-movie_budget
    print(f"Wingard needs {need_money:.2f} leva more.")
else:
    print("Action!" )
    left_money=movie_budget-all_price
    print(f"Wingard starts filming with {left_money:.2f} leva left.")