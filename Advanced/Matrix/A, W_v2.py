size = int(input())
alice_pos = []
collected_bags = 0

positions = {
    "down": (1,0),
    "up": (-1,0),
    "right": (0,1),
    "left": (0,-1,)
}

matrix = [input().split() for _ in range(size)]

for r in range(size):
    if "A" in matrix[r]:
        alice_pos=[r,matrix[r].index("A")]
        matrix[alice_pos[0]][alice_pos[1]]="*"

while collected_bags<10:
    command=input()
    if command in positions:
        row, col = alice_pos[0]+positions[command][0], alice_pos[1]+positions[command][1]
    if not (0 <= row < size and 0 <= col < size):
        break
    alice_pos = [row, col]
    position = matrix[row][col]
    matrix[row][col] = "*"
    if position.isdigit():
        collected_bags+=int(position)
    if position == "R":
        break

if collected_bags <10:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")

print(*[' '.join(row) for row in matrix], sep='\n')