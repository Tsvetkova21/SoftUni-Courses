targets_string = input().split(" ")
targets =[]
for char in targets_string:
    targets.append(int(char))
shots = int(input())
reduce_points = 0
reduce_index = 0
number_shot=0
shoot_counter = 0
while shots!='End':
    number_shot=int(shots)
    if 0<=number_shot<len(targets):
        for i in range (len(targets)):
            if i == number_shot and reduce_index!=-1:
                reduce_points=targets[i]
                reduce_index = i
                shoot_counter+=1
                targets[reduce_index]=-1
                for i in range (len(targets)):
                    if targets[i]>reduce_points:
                        targets[i]-=reduce_points
                    else:
                        targets[i]+=reduce_points

    shots = input()
convert_target_values_to_string = [str(num) for num in targets]
print(f"Shot targets: {shoot_counter} -> {' '.join(convert_target_values_to_string)}")
