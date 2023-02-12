from collections import deque
maximum_caffeine = 300
total_caffeine = 0
milligrams_of_caffeine = deque([int(x) for x in input().split(", ")])
energy_drinks = deque([int(x) for x in input().split(", ")])
while milligrams_of_caffeine and energy_drinks:
    curr_miligrams = milligrams_of_caffeine.pop()
    curr_energy_drink = energy_drinks.popleft()
    caffeine = curr_energy_drink*curr_miligrams
    if caffeine<=(maximum_caffeine-total_caffeine):
        total_caffeine+=caffeine
    elif caffeine>(maximum_caffeine-total_caffeine):
        energy_drinks.append(curr_energy_drink)
        if total_caffeine>30:
            total_caffeine-=30
        else:
            continue
if energy_drinks:
    print(f"Drinks left: {', '.join(str(x) for x in energy_drinks)}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {total_caffeine} mg caffeine.")