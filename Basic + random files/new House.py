flowers=input()
count_flowers=int(input())
budget=int(input())
price=0
if flowers=="Roses":
    if count_flowers>80:
        price=count_flowers*5*0.9
    else:
        price=count_flowers*5
if flowers=="Dahlias":
    if count_flowers>90:
        price=count_flowers*3.80*0.85
    else:
        price=count_flowers*3.80
if flowers=="Tulips":
    if count_flowers>80:
        price=count_flowers*2.80*0.85
    else:
        price=count_flowers*2.80
if flowers=="Narcissus":
    if count_flowers<120:
        price=count_flowers*3*1.15
    else:
        price=count_flowers*3
if flowers=="Gladiolus":
    if count_flowers<80:
        price=count_flowers*2.5*1.2
    else:
        price=count_flowers*2.5
if budget>=price:
    price_left=budget-price
    print(f"Hey, you have a great garden with {count_flowers} "
          f"{flowers} and {price_left:.2f} leva left.")
else:
    price_ness=price-budget
    print(f"Not enough money, you need {price_ness:.2f} leva more.")