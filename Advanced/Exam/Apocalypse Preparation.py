from collections import deque
textiles = deque([int(x) for x in input().split()])
medicaments = deque([int(x) for x in input().split()])
items_collected = {}
items = {
    30: "Patch",
    40: "Bandage",
    100: "MedKit",
}

while textiles and medicaments:
    textile = textiles.popleft()
    medicament = medicaments.pop()
    sum = textile+medicament

    if items.get(sum):
        if items[sum] not in items_collected:
            items_collected[items[sum]]=0
        items_collected[items[sum]]+=1
    elif sum>100:
        if items[100] not in items_collected:
            items_collected[items[100]]=0
        items_collected[items[100]]+=1
        next_medication = medicaments.pop()
        next_medication+=(sum-100)
        medicaments.append(next_medication)
    elif not items.get(sum):
        medicament+=10
        medicaments.append(medicament)
if not medicaments and not textiles:
    print("Textiles and medicaments are both empty.")
elif textiles:
    print("Medicaments are empty.")
elif medicament:
    print("Textiles are empty.")

if items_collected:
    items_sorted = sorted(items_collected.items(), key=lambda a: (-a[1], a[0]))
    for item in items_sorted:
        print(f"{item[0]} - {item[1]}")
if medicaments:
    print(f"Medicaments left: {', '.join([str(x) for x in medicaments][::-1])}")
if textiles:
    print(f"Textiles left: {', '.join(str(x) for x in textiles)}")


