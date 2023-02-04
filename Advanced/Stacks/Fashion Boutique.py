

clothes=[int(n) for n in input().split(" ")]
capacity_one_rack = int(input())
needed_racks = 1
current_space = capacity_one_rack
for numbers in clothes:
    if (current_space-numbers)>=0:
       current_space-=numbers
    else:
        needed_racks+=1
        current_space=capacity_one_rack-numbers

print(needed_racks)