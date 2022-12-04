degrees=int(input())
time=input()
Outfit=" "
Shoes=" "
if degrees>=10 and degrees<=18:
    if time=='Morning':
        Outfit ="Sweatshirt"
        Shoes = "Sneakers"
    elif time == "Afternoon":
        Outfit = "Shirt"
        Shoes = "Moccasins"
    elif time == "Evening":
        Outfit = "Shirt"
        Shoes = "Moccasins"
if degrees>18 and degrees<=24:
    if time=='Morning':
        Outfit="Shirt"
        Shoes = "Moccasins"
    elif time == "Afternoon":
        Outfit = "T-Shirt"
        Shoes = "Sandals"
    elif time == "Evening":
        Outfit = "Shirt"
        Shoes = "Moccasins"
if degrees>=25:
    if time=='Morning':
        Outfit="T-Shirt"
        Shoes = "Sandals"
    elif time == "Afternoon":
        Outfit = "Swim Suit"
        Shoes = "Barefoot"
    elif time == "Evening":
        Outfit = "Shirt"
        Shoes = "Moccasins"
print(f'It\'s {degrees} degrees, get your {Outfit} and {Shoes}.')