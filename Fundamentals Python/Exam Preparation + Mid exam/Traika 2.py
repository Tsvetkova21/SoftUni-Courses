chat_messages = []
while True:
    command_chat = input()

    if command_chat == "end":
        break
    if "Chat" in command_chat:
        command, message = command_chat.split(" ")
        chat_messages.append(message)
    elif "Delete" in command_chat:
        command, message = command_chat.split(" ")
        if message in chat_messages:
            chat_messages.remove(message)
        else:
            continue
    elif "Edit" in command_chat:
        command, message, edit_messagde = command_chat.split(" ")
        if message in chat_messages:
            for i in range(len(chat_messages)):
                if message == chat_messages[i]:
                    chat_messages.remove(message)
                    chat_messages.insert(i,edit_messagde)
        else:
            continue
    elif "Pin" in command_chat:
        command, message = command_chat.split(" ")
        if message in chat_messages:
            chat_messages.remove(message)
            chat_messages.append(message)
    elif "Spam" in command_chat:
        command_chat = command_chat.replace("Spam ", '')
        words = command_chat.split(" ")
        for items in words:
            chat_messages.append(items)

for items in chat_messages:
    print(items)



