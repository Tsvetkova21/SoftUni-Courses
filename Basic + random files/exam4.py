import math

days = int(input())
kilometers = float(input())
percentage = 0
sum_km = kilometers
diff = 0

for i in range(1, days +1):
    percentage = int(input())
    kilometers=kilometers*(1+percentage/100)
    sum_km +=kilometers

if sum_km < 1000:
    diff = 1000 - sum_km
    print (f'Sorry Mrs. Ivanova, you need to run '
            f'{math.ceil(diff)} more kilometers')
else:
    diff = sum_km - 1000
    print(f'You\'ve done a great job running '
            f'{math.ceil(diff)} more kilometers!')
