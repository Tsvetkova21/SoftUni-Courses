rows, columns = [int(x) for x in input().split()]
matrix=[input().split() for _ in range(rows)]
my_pos = []
made_moves = 0
touched_opponets = 0

positions = {
    "down": (1,0),
    "up": (-1,0),
    "right": (0,1),
    "left": (0,-1,)
}

for row in range(rows):
    if "B" in matrix[row]:
        my_pos=[row,matrix[row].index("B")]
        matrix[my_pos[0]][my_pos[1]] = "-"

while True:
    command = input()
    if command=="Finish":
        break
    for row in range(rows):
        if touched_opponets==3:
            break
        new_row, new_col =my_pos[0]+positions[command][0],my_pos[1]+positions[command][1]
        if 0<=new_row<rows and 0<=new_col<columns:
            if matrix[new_row][new_col]=="P":
                made_moves+=1
                touched_opponets+=1
                my_pos=[new_row,new_col]
                break
            if matrix[new_row][new_col]=="O":
                break
            if matrix[new_row][new_col]=="-":
                made_moves+=1
                my_pos = [new_row, new_col]
                break
matrix[my_pos[0]][my_pos[1]]="B"
print("Game over!")
print(f"Touched opponents: {touched_opponets} Moves made: {made_moves}")