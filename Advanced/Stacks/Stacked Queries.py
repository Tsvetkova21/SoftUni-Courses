lines = int(input())
stack = []

for i in range(lines):
    command = input()
    if command.startswith("1"):
        current_command, number = command.split(" ")
        stack.append(int(number))
    elif command.startswith("2"):
        if len(stack)>0:
            stack.pop()
    elif command.startswith("3"):
        if len(stack)>0:
            print(max(stack))
    elif command.startswith("4"):
        if len(stack)>0:
            print(min(stack))
stack.reverse()
print(*stack, sep=", ")