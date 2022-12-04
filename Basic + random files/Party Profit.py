import math

group_size=int(input())
days=int(input())
price = 0

for i in range (1,days+1):

    if i % 10 == 0:
        group_size = group_size - 2

    if i % 15 == 0:
        group_size = group_size + 5

    if i % 5 == 0:
        price += 20*group_size

    if i % 3 == 0:
        price -= 3 * group_size

    if i%15==0:
        price -=2*group_size
    price = price + 50 - 2 * group_size

print(f"{group_size} companions received"
      f" {math.floor(price/group_size)} coins each.")