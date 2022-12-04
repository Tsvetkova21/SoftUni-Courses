fire= input().split("#")
effort = 0
water = int(input())
water_cell=0
cells=[]
total_fire=0
for elements in fire:
    if 'High =' in elements:
        water_cell = int(elements.strip('High ='))
        if 81<=water_cell<=125:
            if water_cell<=water:
                water-=water_cell
                cells.append(water_cell)
                effort+=0.25*water_cell
                total_fire+=water_cell
    if 'Low =' in elements:
        water_cell=int(elements.strip('Low ='))
        if 1<=water_cell<=50:
            if water_cell<=water:
                water-=water_cell
                cells.append(water_cell)
                effort += 0.25 * water_cell
                total_fire += water_cell
    if 'Medium =' in elements:
        water_cell=int(elements.strip('Medium ='))
        if 51<=water_cell<=80:
            if water_cell<=water:
                water-=water_cell
                cells.append(water_cell)
                effort += 0.25 * water_cell
                total_fire += water_cell
print('Cells:')
for elements in cells:
    print(f' - {elements}')
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')