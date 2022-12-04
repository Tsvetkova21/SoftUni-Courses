message = input()
new_text = ""
strenght = 0
for index in range(len(message)):
    if strenght>0 and message[index]!=">":
        strenght-=1
    elif message[index] == ">":
        new_text+=message[index]
        strenght+=int(message[index+1])
    else:
        new_text+=message[index]
print(new_text)