destination = input()
min_budget = float (input())
condition = False
money_saved = 0
all_saved = 0

while destination != 'End':
    money_saved = float(input())
    all_saved += money_saved
    if all_saved >= min_budget:
        print(f'Going to {destination}!')

        destination = input()
        min_budget = float(input())
        all_saved = 0

    if destination == 'End':
        break
