activation_key = input()

while True:
    command = input().split(">>>")
    current_command = command[0]
    if current_command == "Generate":
        print(f"Your activation key is: {activation_key}")
        break
    elif current_command=="Contains":
        substring = command[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")
    elif current_command=="Flip":
        if command[1]=="Upper":
            start = int(command[2])
            end = int(command[3])
            activation_key=activation_key[:start]+activation_key[start:end].upper()+activation_key[end:]
            print(activation_key)
        if command[1]=="Lower":
            start = int(command[2])
            end = int(command[3])
            activation_key = activation_key[:start] + activation_key[start:end].lower() + activation_key[end:]
            print(activation_key)
    elif current_command=="Slice":
        start = int(command[1])
        end = int(command[2])
        activation_key=activation_key[:start]+activation_key[end:]
        print(activation_key)
