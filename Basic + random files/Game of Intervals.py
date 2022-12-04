turns = int(input())
number = 0
number_0_9 =0
number_10_19 = 0
number_20_29 = 0
number_30_39 = 0
number_40_50 = 0
number_invalid = 0
numbers = 0
points = 0
for num in range(0,turns):
    number = int(input())
    if 0<=number<=9:
        points += 0.2*number
        number_0_9+=1
    if 10<=number<=19:
        points += 0.3*number
        number_10_19+= 1
    if 20<=number<=29:
        points += 0.4*number
        number_20_29 += 1
    if 30<=number<=39:
        points += 50
        number_30_39 += 1
    if 40<=number<=50:
        points += 100
        number_40_50 += 1
    if number<0 or number>50:
        number_invalid += 1
        points = points/2
    numbers+=1
print (f'{points:.2f}')
print(f'From 0 to 9: {(number_0_9/numbers*100):.2f}%')
print(f'From 10 to 19: {(number_10_19/numbers*100):.2f}%')
print(f'From 20 to 29: {(number_20_29/numbers*100):.2f}%')
print(f'From 30 to 39: {(number_30_39/numbers*100):.2f}%')
print(f'From 40 to 50: {(number_40_50/numbers*100):.2f}%')
print(f'Invalid numbers: {(number_invalid/numbers*100):.2f}%')