import math

count_tournament = int(input())
start_points = int(input())
points=start_points
win_tournaments=0
for num in range(0, count_tournament):
    stage_tournament=input()
    if stage_tournament == 'W':
        points+=2000
        win_tournaments+=1
    if stage_tournament == 'F':
        points+=1200
    if stage_tournament == 'SF':
        points+=720
print(f"Final points: {points}")
print(f"Average points: {(math.floor((points-start_points)/count_tournament))}")
print(f"{((win_tournaments/count_tournament)*100):.2f}%")
