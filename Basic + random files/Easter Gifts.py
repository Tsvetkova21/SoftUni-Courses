list_of_gifts = input().split(" ")
command = input()
list_commands=[]
new_gifts=[]
while command!='No Money':
    list_commands=command.split(" ")
    for i in range(len(list_of_gifts)):
        if list_commands[0]=="OutOfStock":
            if list_of_gifts[i]==list_commands[1]:
                list_of_gifts[i]='None'
    if list_commands[0]=='Required':
        if 0<int(list_commands[2])<len(list_of_gifts):
            list_of_gifts[int(list_commands[2])]=list_commands[1]
    if list_commands[0] == 'JustInCase':
        list_of_gifts[len(list_of_gifts)-1]=(list_commands[1])
    command = input()
for i in range(len(list_of_gifts)):
    if list_of_gifts[i]!='None':
        new_gifts.append(list_of_gifts[i])
print(*new_gifts, sep=" ")
