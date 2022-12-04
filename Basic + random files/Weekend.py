work_day=input()
i=0
if work_day=="Monday":
    print("Working day")
    i=1
if work_day=="Tuesday":
    print("Working day")
    i=2
if work_day=="Thursday":
    print("Working day")
    i=3
if work_day == "Wednesday":
    print("Working day")
    i=4
if work_day=="Friday":
    print("Working day")
    i=5
if work_day=="Saturday":
    print("Weekend")
    i=6
if work_day == "Sunday":
    print("Weekend")
    i=7
if i==0:
    print("Error")