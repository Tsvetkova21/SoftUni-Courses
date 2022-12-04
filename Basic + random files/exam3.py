count_dancers = int(input())
points = float(input())
season = input()
place = input()
price = 0
charity = 0
for_dancers = 0

if place == 'Bulgaria':

    if season == 'summer':
        price = points*count_dancers*0.95
    if season == 'winter':
        price =points*count_dancers*0.92

if place == 'Abroad':

    if season == 'summer':
        price = points*count_dancers*1.5*0.9
    if season == 'winter':
        price = points*count_dancers*1.5*0.85

charity = 0.75*price
for_dancers = 0.25*price/count_dancers

print(f"Charity - {charity:.2f}")
print(f"Money per dancer - {for_dancers:.2f}")


