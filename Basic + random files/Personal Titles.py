ages=float(input())
gender=input()

if gender=='m':
    if ages<16:
        print("Master")
    else:
        print("Mr.")
elif gender=='f':
    if ages<16:
        print("Miss")
    else:
        print("Ms.")