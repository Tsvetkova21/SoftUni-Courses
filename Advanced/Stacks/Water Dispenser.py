
from collections import deque

def add_names_in_deque():
    people_data = deque()
    while True:
        name= input()
        if name == "Start":
            break
        people_data.append(name)

    return people_data

water_amount = int(input())
people_deque = add_names_in_deque()

while True:
    command = input()
    if command == "End":
        print(f"{water_amount} liters left")
        break

    elif command.startswith("refill"):
        refill_command_data = command.split(' ')
        refill_water= int(refill_command_data[1])
        water_amount=water_amount+refill_water

    else:
        person = people_deque.popleft()
        current_litres = int(command)
        if current_litres <=water_amount:
            print(f"{person} got water")
            water_amount -=current_litres
        else:
            print(f"{person} must wait")