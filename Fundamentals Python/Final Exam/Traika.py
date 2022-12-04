text = input()
value_substring = 0
while True:
    command = input().split(" ")
    current_command = command[0]
    if current_command=="Replace":
        current_char, new_char = command[1], command[2]
        for ch in text:
            if ch==current_char:
                text = text.replace(current_char, new_char)
        print(text)
    elif current_command=="Cut":
        start_index, end_index = int(command[1]), int(command[2])
        if 0<start_index<end_index and end_index<len(text):
            text = text[:(start_index)]+text[(end_index+1):]
            print(text)
        else:
            print("Invalid indices!")
    elif current_command == "Make":
        case = command[1]
        if case=="Upper":
            text = text.upper()
            print(text)
        if case=="Lower":
            text = text.lower()
            print(text)
    elif current_command=="Check":
        string = command[1]
        if string in text:
            print(f"Message contains {string}")
        else:
            print(f"Message doesn't contain {string}")
    elif current_command=="Sum":
        start_sum_index, end_sum_index = int(command [1]), int(command[2])
        if 0<start_sum_index<end_sum_index and end_sum_index<len(text):
            substring = text[(start_sum_index):(end_sum_index+1)]
            for ch in substring:
                value_substring +=ord(ch)
            print(value_substring)
        else:
            print("Invalid indices!")
    elif current_command=="Finish":
        break