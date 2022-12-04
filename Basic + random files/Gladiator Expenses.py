lost_counts=int(input())
helmet_price = float(input())
sword_price =float(input())
shield_price=float(input())
armor_price=float(input())
price = 0

for i in range (1,lost_counts+1):
    if i%2==0:
        price+=helmet_price
    if i%3==0:
        price+=sword_price
    if i%6==0:
        price+=shield_price
    if i%12==0:
        price+=armor_price
print(f'Gladiator expenses: {price:.2f} aureus')