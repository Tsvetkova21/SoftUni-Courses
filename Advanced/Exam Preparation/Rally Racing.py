size = int(input())
racing_car_number = input()
matrix = [input().split() for _ in range(size)]
tunel_start_position = []
tunel_end_position = []
my_position = [0,0]
directions={
    "down": (1,0),
    "up": (-1,0),
    "right": (0,1),
    "left": (0,-1),
}
kilometers_passed = 0
command = input()
while command!="End":
    if command in directions:
        my_position=[(my_position[0]+directions[command][0]),(my_position[1]+directions[command][1])]
        if matrix[my_position[0]][my_position[1]]=="T":
            for row in range(size):
                if "T" in matrix[row]:
                    matrix[my_position[0]][my_position[1]] = "."
                if "T" in matrix[row]:
                    my_position=[row, matrix[row].index("T")]
                    matrix[my_position[0]][my_position[1]] = "."
                    kilometers_passed+=30
        elif matrix[my_position[0]][my_position[1]]=="F":
            print(f"Racing car {racing_car_number} finished the stage!")
            matrix[my_position[0]][my_position[1]] = "C"
            kilometers_passed+=10
            break
        else:
            kilometers_passed+=10
    command = input()

for row in range(size):
    if "F" in matrix[row]:
        matrix[my_position[0]][my_position[1]] = "C"
        print(f"Racing car {racing_car_number} DNF.")
print(f"Distance covered {kilometers_passed} km.")
print(*[''.join(row) for row in matrix], sep='\n')
