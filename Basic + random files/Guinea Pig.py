food_kg = float(input())
hay_kg = float (input())
cover_kg = float (input())
guinea_weight_kg = float(input())
happy = True

for i in range (1,30+1):
    food_kg-=300/1000
    if round(food_kg,2)<=0.00:
        happy=False
        break
    if i%2 ==0:
        hay_kg-=0.05*food_kg
    if round(hay_kg,2)<=0:
        happy=False
        break
    if i%3==0:
        cover_kg-=1/3*guinea_weight_kg
    if round(cover_kg,2)<=0:
        happy=False
        break
if not happy:
    print("Merry must go to the pet store!")
else:
    print(f"Everything is fine! Puppy is happy! Food: {food_kg:.2f}, Hay: {hay_kg:.2f}, Cover: {cover_kg:.2f}.")
