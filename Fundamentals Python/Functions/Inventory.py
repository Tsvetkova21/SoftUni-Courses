items = input().split(", ")
command = input()
command_item = ''
old_item = ''
old_item_index = 0
combine_items = []
new_item = ''
renew_item = ''
while command!='Craft!':
    if 'Collect' in command:
        command_item=command.replace("Collect - ", '')
        for char in items:
            if char != command_item:
                items.append(command_item)
                break
            else:
                continue
    elif 'Drop' in command:
        command_item=command.replace("Drop - ", '')
        for char in items:
            if char == command_item:
                items.remove(command_item)
            else:
                continue
    elif 'Combine Items' in command:
        command_item = command.replace("Combine Items - ", '')
        combine_items=command_item.split(":")
        old_item=combine_items[0]
        new_item=combine_items[1]
        for i in range (len(items)):
            if old_item==items[i]:
                old_item = i
                items.insert(i+1, new_item)
            else:
                continue
    elif 'Renew' in command:
        command_item = command.replace("Renew - ", '')
        for i in range (len(items)):
            if command_item==items[i]:
                renew_item =items.pop(i)
                items.append(renew_item)
            else:
                continue
    command = input()
print(*items, sep=', ')