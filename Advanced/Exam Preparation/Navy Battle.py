size = int(input())
matrix = [list(input()) for _ in range(size)]
submarine_pos = []
mine_hits = 3
destroid_cr = 3
positions = {
    "down": (1,0),
    "up": (-1,0),
    "right": (0,1),
    "left": (0,-1,)
}
for row in range(size):
    if "S" in matrix[row]:
        submarine_pos=[row,matrix[row].index("S")]
        matrix[submarine_pos[0]][submarine_pos[1]] = "-"
while True:
    command = input()
    if command in positions:
        submarine_pos=[submarine_pos[0]+positions[command][0], submarine_pos[1]+positions[command][1]]
    for row in range(size):
        if matrix[submarine_pos[0]][submarine_pos[1]]=="*":
            mine_hits-=1
            if mine_hits<1:
                print(f"Mission failed, U-9 disappeared! Last known coordinates [{submarine_pos[0]}, {submarine_pos[1]}]!")
                matrix[submarine_pos[0]][submarine_pos[1]] = "S"
                print(*[''.join(row) for row in matrix], sep='\n')
                quit()
            matrix[submarine_pos[0]][submarine_pos[1]]="-"
        if matrix[submarine_pos[0]][submarine_pos[1]]=="C":
            destroid_cr -= 1
            if destroid_cr<=0:
                print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
                matrix[submarine_pos[0]][submarine_pos[1]] = "S"
                print(*[''.join(row) for row in matrix], sep='\n')
                quit()
        matrix[submarine_pos[0]][submarine_pos[1]] = "-"
