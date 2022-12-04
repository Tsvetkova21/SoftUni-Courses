command = input()
final_phonebook = {}
while "-" in command:
    phonebook = command.split("-")
    name, phone = phonebook[0], phonebook[1]
    if name not in final_phonebook:
        final_phonebook[name]=[]
    final_phonebook[name]=phone
    command = input()
for i in range(int(command)):
    search_name = input()
    if search_name in final_phonebook.keys():
        print(f"{search_name} -> {final_phonebook[search_name]}")
    else:
        print(f"Contact {search_name} does not exist.")
