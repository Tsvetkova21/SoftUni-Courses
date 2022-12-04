import math

vineyard=int(input())
grapes_sq_m=float(input())
litres_wine=int(input())
workers=int(input())

made_wine=vineyard*0.4*grapes_sq_m/2.5

if made_wine<litres_wine:
    print(f'It will be a tough winter! More'
          f' {math.floor(litres_wine-made_wine)} liters wine needed.')
if made_wine>=litres_wine:
    print(f'Good harvest this year! Total wine: '
          f'{math.floor(made_wine)} liters.')
    print(f'{math.ceil(made_wine-litres_wine)} liters left '
          f'-> {math.ceil((made_wine-litres_wine)/workers)} '
          f'liters per person.')

