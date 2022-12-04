hour=int(input())
minutes=int(input())
minutes_new=minutes+15
if minutes_new>=60:
    hour=hour+1
    minutes_new=minutes_new-60
if hour>=24:
    hour=hour-24
if minutes_new<10:
    print(f'{hour}:0{minutes_new}')
else:
    print(f'{hour}:{minutes_new}')