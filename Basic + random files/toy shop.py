exs_price=float(input())
count_puzzels=int(input())
count_dolls=int(input())
count_teddy_bears=int(input())
count_minions=int(input())
count_trucks=int(input())
toys=count_trucks+count_minions+count_dolls+count_teddy_bears+count_puzzels
if toys>=50:
    price=(count_puzzels*2.6+count_dolls*3+count_teddy_bears*4.1+count_minions*8.2
           +count_trucks*2)*0.75
else:
    price = count_puzzels * 2.6 + count_dolls * 3 + count_teddy_bears * 4.1 + \
            count_minions * 8.2 + count_trucks * 2
if price*0.9>=exs_price:
    left=price*0.9-exs_price
    print(f'Yes! {left:.2f} lv left.')
else:
    ostv = exs_price-price * 0.9
    print(f'Not enough money! {ostv:.2f} lv needed.')