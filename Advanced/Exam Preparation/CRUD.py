size = 6
matrix = [[x for x in  input().split()] for _ in range(size)]
position = [int(x) for x in  input().strip("(").strip(")").split(", ")]
#position = list(map(int, input().strip("(").strip(")").split(", ")))
directions = {
    "down": (1,0),
    "up": (-1,0),
    "right": (0,1),
    "left": (0,-1),
}
line = input()
while line!="Stop":
    current_line = line.split(", ")
    command, direction = current_line[0], current_line[1]
    row, col = position[0] + directions[direction][0], position[1] + directions[direction][1]
    position=[row,col]
    if command=="Create":
        value = current_line[2]
        if matrix[row][col]==".":
            matrix[row][col]=value
    elif command=="Update":
        value = current_line[2]
        if matrix[row][col]!=".":
            matrix[row][col] = value
    elif command =="Delete":
        if matrix[row][col]!=".":
            matrix[row][col]="."
    elif command=="Read":
        if matrix[row][col]!=".":
            print(matrix[row][col])
    line = input()
print(*[' '.join(row) for row in matrix], sep='\n')