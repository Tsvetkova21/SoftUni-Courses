def reduce_values(target_sequence, index):
    special_value = target_sequence[index]
    target_sequence[index]=-1

    for i in range(len(target_sequence)):
        if target_sequence[i] ==-1:
            continue
        if special_value < target_sequence[i]:
            target_sequence[i] -=special_value
        else:
            target_sequence[i]+=special_value
    return  target_sequence

def shoot_for_the_win_func(target_sequence):
    count_of_shot_targets = 0
    while True:
        command = input()
        if command == 'End':
            break
        index = int(command)
        if 0 <= index < len(target_sequence) and target_sequence[index]!= -1:
            count_of_shot_targets+=1
            reduce_values(target_sequence, index)
    convert_target_values_to_string = [str(num) for num in target_sequence]
    print(f"Shot targets: {count_of_shot_targets} -> {' '.join(convert_target_values_to_string)}")

data = list(map(int, input().split(' ')))

shoot_for_the_win_func(data)