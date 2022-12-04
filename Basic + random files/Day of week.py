week_day=int(input())

if week_day>=1 and week_day<=7:
    if week_day==1:
        print("Monday")
    if week_day==2:
        print("Tuesday")
    if week_day==3:
        print("Wednesday")
    if week_day==4:
        print("Thursday")
    if week_day==5:
        print("Friday")
    if week_day==6:
        print("Saturday")
    if week_day==7:
        print("Sunday")
else:
    print("Error")