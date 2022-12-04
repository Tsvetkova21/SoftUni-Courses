string = input()
beggar = int(input())
final_list=[]

sum_points = string.split(", ")
sum_points = ([int(x) for x in sum_points])
points_beggars = []
counter_of_index = 0
while counter_of_index<beggar:
    sum_for_current_beggar = 0
    for element in range(counter_of_index, len(sum_points), beggar):
        sum_for_current_beggar +=sum_points[element]
    counter_of_index+=1
    final_list.append(sum_for_current_beggar)
print(final_list)