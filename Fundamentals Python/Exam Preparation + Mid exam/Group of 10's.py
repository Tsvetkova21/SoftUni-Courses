import math
def separeted_groups(x,age):
    group_list = []
    for elements in x:
        if age - 10 <elements<=age:
            group_list.append(elements)
    print(f"Group of {age}'s: {group_list}")


people = list(map(int, input().split(", ")))
group_max_age=math.ceil(max(people))
for i in range(10,group_max_age+10,10):
    separeted_groups(people,i)
