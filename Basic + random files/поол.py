import math

people_count=int(input())
tax=float(input())
tax_chair=float(input())
tax_umbrella=float(input())
sum=math.ceil(people_count*0.75)*tax_chair+math.ceil(people_count*0.5)*tax_umbrella+people_count*tax
print(f'{sum:.2f} lv.')

