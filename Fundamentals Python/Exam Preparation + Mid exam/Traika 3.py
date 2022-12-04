def commands_coffee(coffee, count):
    for i in range(count):
        new_coffee = input()
        if "Include" in new_coffee:
            command, coffee_type = new_coffee.split(" ")
            coffee.append(coffee_type)
        elif "Remove" in new_coffee:
            command, order, numbers_of_coffee = new_coffee.split(" ")
            if 0<=int(numbers_of_coffee)<=len(coffee):
                if order == "first":
                    removed = 0
                    for i in range(int(numbers_of_coffee)):
                        coffee.pop(i-removed)
                        removed+=1
                if order == "last":
                    len_num = len(coffee)-int(numbers_of_coffee)

                    for i in range(len(coffee),len_num,-1):
                        coffee.pop(i-1)
        elif "Prefer" in new_coffee:
            command, first_index, second_index = new_coffee.split(" ")
            if 0<=int(first_index)<=len(coffee) and 0<=int(second_index)<=len(coffee):
                coffee[int(first_index)], coffee[int(second_index)]=coffee[int(second_index)], coffee[int(first_index)]
            else:
                continue
        elif "Reverse" in new_coffee:
            coffee.reverse()

coffee_list = input().split(" ")
count_commands = int(input())
commands_coffee(coffee_list, count_commands)
print("Coffees:")
print(' '.join(str(coff) for coff in coffee_list))