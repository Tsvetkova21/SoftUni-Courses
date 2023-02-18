size = int(input())
commands = input().split()

matrix = []
miner_pos = []
collected_coal, total_coal = 0, 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    matrix.append(input().split())
    total_coal += matrix[row].count("c")

    if "s" in matrix[row]:
        miner_pos=[row, matrix[row].index("s")]
        matrix[row][miner_pos[1]]='*'

for command in commands:
    row, col = miner_pos[0] + directions[command][0], miner_pos[1] + directions[command][1]
    if not (0<=row<size and 0<=col<size):
        continue
    miner_pos = [row,col]
    if matrix[row][col]=="c":
        collected_coal+=1
        if collected_coal == total_coal:
            print(f"You collected all coal! ({miner_pos[0]}, {miner_pos[1]})")
            break
    elif matrix[row][col]=="e":
        print(f"Game over! ({miner_pos[0]}, {miner_pos[1]})")
        break

    matrix[row][col] = "*"

else:
    print(f"{total_coal - collected_coal} pieces of coal left. ({miner_pos[0]}, {miner_pos[1]})")
