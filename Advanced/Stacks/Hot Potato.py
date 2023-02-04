
from collections import deque
name_of_players = input().split(' ')
step = int(input())

players = deque(name_of_players)
counter =  0

while len(players)>1:
    counter += 1
    current_name_player = players.popleft()
    if counter == step:
        print(f"Removed {current_name_player}")
        counter = 0
    else:
        players.append(current_name_player)
print(f"Last is {players[0]}")