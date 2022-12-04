command = input()
dictionary = {}
while command != "stop":
    if command not in dictionary:
        dictionary[command]=0
    dictionary[command]+=int(input())
    command = input()
for (key, value) in dictionary.items():
    print(f"{key} -> {value}")