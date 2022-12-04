budget=int(input())
season=input()
count_fishers=int(input())
price_boat=0
discount=0
if season =="Spring":
    price_boat=3000
elif season=="Summer" or season=="Autumn":
    price_boat=4200
elif season=="Winter":
    price_boat=2600
if count_fishers<=6:
    discount=0.1
elif count_fishers>7 and count_fishers<=11:
    discount=0.15
elif count_fishers>=12:
    discount=0.25
tax =  price_boat*(1-discount)
if count_fishers%2==0 and season!="Autumn":
    tax=tax*0.95
if budget>=tax:
    left_money=budget-tax
    print(f"Yes! You have {left_money:.2f} leva left.")
else:
    ness_money=tax-budget
    print(f"Not enough money! You need {ness_money:.2f} leva.")