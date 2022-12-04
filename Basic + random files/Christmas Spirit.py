quantity = int(input())
days = int(input())
spirit = 0
spend = 0
for i in range (1, days+1):
    if i%11==0:
        quantity=quantity + 2

    if i%10==0:
        spirit=spirit-20
        spend+=5+3+15
        if i == days:
            spirit = spirit - 30

    if i%5==0:
        spend+=15*quantity
        spirit+=17

    if i%15==0:
        spirit +=30

    if i%3==0:
        spend+=5*quantity+3*quantity
        spirit+=3+10

    if i%2==0:
        spend +=2*quantity
        spirit +=5

print (f'Total cost: {spend:.0f}')
print(f'Total spirit: {spirit:.0f}')
