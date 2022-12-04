money_vacation = float(input())
money_on_hand = float(input())
count_spend = 0
saved_money = True
action = " "
day_money = 0
counter_days = 0
sum_money = 0

while True:
    action = input()
    day_money = float(input())
    counter_days += 1
    if action == 'spend':
        count_spend+=1
        if money_on_hand >= day_money:
            money_on_hand = money_on_hand - day_money
        else:
            money_on_hand = 0
    if action == 'save':
        money_on_hand = money_on_hand + day_money
        count_spend = 0
    if money_on_hand >= money_vacation:
        saved_money = False
        break
    if count_spend == 5:
        print (f'You can\'t save the money.')
        print (f'{counter_days}')
        break
if not saved_money:
    print (f'You saved the money for {counter_days} days.')




