needed_exp = float(input())
battle_counts = int(input())
lock = True
count = 0
made_experience = 0
for i in range(1,battle_counts+1):
    if lock == False:
        break
    count += 1
    attack_exp = float(input())
    if i % 3 == 0:
        attack_exp = attack_exp * 1.15
    if i % 5 == 0:
        attack_exp = attack_exp * 0.9
    if i % 15 == 0:
        attack_exp = attack_exp * 1.05

    made_experience += attack_exp
    if made_experience >=needed_exp:
        lock = False
difference = needed_exp-made_experience
if lock == False:
    print(f"Player successfully collected his needed experience for {count} battles.")
elif lock == True:
    print(f"Player was not able to collect the needed experience, {(difference):.2f} more needed.")