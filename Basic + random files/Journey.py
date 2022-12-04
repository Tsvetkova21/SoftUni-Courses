budget=float(input())
season=input()
journey=" "
destination=" "
price=0
if budget<=100:
    destination="Somewhere in Bulgaria"
    if season=="summer":
        price=budget*0.3
        journey="Camp"
    if season=="winter":
        price=budget*0.7
        journey = "Hotel"
elif budget>100 and budget<=1000:
    destination = "Somewhere in Balkans"
    if season=="summer":
        price=budget*0.4
        journey = "Camp"
    if season=="winter":
        price=budget*0.8
        journey = "Hotel"
elif budget>1000:
    price = budget * 0.9
    destination = "Somewhere in Europe"
    journey = "Hotel"
print(f" {destination}")
print(f"{journey} - {price:.2f}")