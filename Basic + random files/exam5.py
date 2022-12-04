meters = 5364
counter = 1

while meters<8848:
    sleeping = str(input())

    if sleeping == 'END':
        print("Failed!")
        print(f"{meters}")
        break

    meters_climbed = int(input())

    if sleeping == 'Yes':
        counter+=1
        if counter<=5:
            meters += meters_climbed
        else:
            print("Failed!")
            print(f"{meters}")
            break
    elif sleeping == 'No':
        meters +=meters_climbed
    if meters>=8848:
        print(f"Goal reached for {counter} days!")



