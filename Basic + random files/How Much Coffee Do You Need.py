command = input()
count = 0

while command!='END':
    if command.islower() == True:
        if command == 'coding':
           count+=1
        elif command == 'cat' or command == 'dog':
            count+=1
        elif command == 'movie':
            count+=1

    elif command.isupper() == True:
        if command.upper() == 'CODING':
           count+=2
        elif command == 'CAT' or command == 'DOG':
            count+=2
        elif command == 'MOVIE':
            count+=2
    command = input()

if count>5:
    print ('You need extra sleep')
else:
    print(f'{count}')