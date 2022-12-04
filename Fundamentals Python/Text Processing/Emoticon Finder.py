message = input()
emoticons = []
for index in range(len(message)):
    if message[index]==":":
        emoticons.append(f"{message[index]+message[index+1]}")
for item in emoticons:
    print(item)