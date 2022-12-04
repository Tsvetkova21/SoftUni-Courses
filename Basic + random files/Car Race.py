import math

time =input().split(" ")
left_racer = []
right_racer= []
time_left = 0
time_right = 0
for i in range (math.floor(len(time)/2)):
    left_racer.append(int(time[i]))
for i in range (len(time)-1,math.floor(len(time)/2),-1):
    right_racer.append(int(time[i]))
for elements in left_racer:
    time_left +=elements
    if elements==0:
        time_left = time_left*0.8

for elements in right_racer:
    time_right +=elements
    if elements==0:
        time_right = time_right*0.8
if time_right<time_left:
    print(f'The winner is right with total time: {time_right:.1f}')
else:
    print(f'The winner is left with total time: {time_left:.1f}')
