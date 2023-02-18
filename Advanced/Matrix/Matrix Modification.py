size = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(size)]
command = input().split()

while command[0]!="END":
    type_command, row, col, num = [int(el) if el.isdigit() else el for el in command]
    if not (0 <= int(row) < size and 0 <= int(col) < size):
        print("Invalid coordinates")
    elif type_command =="Add":
        matrix[int(row)][int(col)]+=num
    elif type_command == "Subtract":
        matrix[int(row)][int(col)]-=num

    command=input().split()

[print(*row) for row in matrix]