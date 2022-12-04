followers = {}
while True:
    command = input().split(": ")
    current_command=command[0]
    if current_command=="Log out":
        break

    elif current_command=="New follower":
        username = command[1]
        if username not in followers:
            followers[username]=0
        else:
            pass
    elif current_command=="Like":
        username = command[1]
        count_likes = int(command[2])
        if username not in followers:
            followers[username] = count_likes
        else:
            followers[username] += count_likes
    elif current_command=="Comment":
        username = command[1]
        if username not in followers:
            followers[username] = 1
        else:
            followers[username] += 1
    elif current_command=="Blocked":
        username = command[1]
        if username not in followers:
            print(f"{username} doesn't exist.")
        else:
            del followers[username]
print(f"{len(followers)} followers")

for (key, value) in followers.items():
    print(f"{key}: {value}")

