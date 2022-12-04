lines = int(input())
register = {}

for i in range(lines):
    command = input().split(" ")
    if 'register' == command[0]:
        username = command[1]
        plate = command [2]
        if username not in register:
            register[username]=plate
            print(f"{username} registered {register[username]} successfully")
        else:
            print(f"ERROR: already registered with plate number {register[username]}")
    if 'unregister' == command[0]:
        username = command[1]
        if username in register:
            del register[username]
            print(f"{username} unregistered successfully")
        else:
            print(f"ERROR: user {username} not found")
for key,value in register.items():
    print(f"{key} => {value}")