command = input()
liked_meal = {}
unliked_meals = {}
count_unliked_meals = 0

while command != "Stop":
    current_command, guest, meal = command.split("-")
    if current_command=="Like":
        if guest not in liked_meal:
            liked_meal[guest] = []
        if guest in liked_meal:
            if meal not in liked_meal[guest]:
                liked_meal[guest].append(meal)
    if current_command=="Dislike":
        if guest not in liked_meal:
            print(f"{guest} is not at the party.")
        if guest in liked_meal:
            if meal not in liked_meal[guest]:
                print(f"{guest} doesn't have the {meal} in his/her collection.")
            else:
                print(f"{guest} doesn't like the {meal}.")
                unliked_meals[guest]=[]
                unliked_meals[guest].append(meal)
                del liked_meal[guest]
                if guest not in liked_meal:
                    liked_meal[guest]=[]
                count_unliked_meals +=1
    command=input()
for (key,value) in liked_meal.items():
    print(f"{key}: {', '.join(value)}")
print(f"Unliked meals: {count_unliked_meals}")


