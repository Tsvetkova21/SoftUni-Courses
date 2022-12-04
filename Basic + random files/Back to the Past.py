money_inherited = float(input())
year = int(input())
money_left = money_inherited
Ivan_age = 18
for num in range(1800, year+1):
    if num%2 == 0:
        money_left = money_left - 12000
    else:
        money_left = money_left - 12000 - 50*Ivan_age
    Ivan_age = Ivan_age + 1
if money_left>=0:
    print(f"Yes! He will live a carefree life and will "
          f"have {money_left:.2f} dollars left." )
else:
    print(f"He will need {(abs(money_left)):.2f} "
          f"dollars to survive." )
