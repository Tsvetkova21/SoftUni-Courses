Lili_age=int(input())
price_wash_machine = float(input())
price_toys = int(input())

money = 0
count_toys = 0

for num in range (1, Lili_age+1):
    if num%2 == 0:
        money+=10*num/2-1
    if num%2 != 0:
        count_toys+=1

money=money+count_toys*price_toys

if money>=price_wash_machine:
    print(f'Yes! {(money-price_wash_machine):.2f}')
else:
    print(f'No! {(abs(money - price_wash_machine)):.2f}')
