def print_func(data):
    if data:
        for car_number in data:
            print(car_number)
    else:
        print("Parking Lot is Empty")

n = int(input())
command_in = 'IN'
command_out = 'OUT'
platte_number_records = [input() for _ in range(n)]
parking_lot_data = set()

for record in platte_number_records:
    command, platte_number = record.split(', ')

    if command == command_in:
        parking_lot_data.add(platte_number)
    elif command == command_out:
        parking_lot_data.remove(platte_number)

print_func(parking_lot_data)
