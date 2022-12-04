count_loads = int(input())
weight_load = 0
all_weight = 0
all_weight_price = 0
weight_microbus = 0
weight_microbus_price = 0
weight_truck_price = 0
weight_truck = 0
weight_train_price = 0
weight_train = 0


for num in range (1, count_loads+1):
    weight_load = int(input())

    if weight_load <= 3:
        price=200
        weight_microbus_price += price * weight_load
        weight_microbus +=weight_load
    elif 4<=weight_load<=11:
        price=175
        weight_truck_price += price * weight_load
        weight_truck+=weight_load
    elif weight_load>=12:
        price = 120
        weight_train_price += price * weight_load
        weight_train += weight_load
    all_weight +=weight_load
    all_weight_price=weight_train_price + weight_truck_price + weight_microbus_price


print(f'{(all_weight_price/all_weight):.2f}')
print(f'{(weight_microbus/all_weight*100):.2f}%')
print(f'{(weight_truck/all_weight*100):.2f}%')
print(f'{(weight_train/all_weight*100):.2f}%')
