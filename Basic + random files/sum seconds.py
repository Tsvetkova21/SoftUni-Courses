
import math
time_first=int(input())
time_second=int(input())
time_third=int(input())
total_time=time_first+time_second+time_third
min=total_time//60
sec=total_time%60
minutes=math.floor(min)
if sec<10:
    print(f'{min}:0{sec}')
else:
    print(f'{min}:{sec}')