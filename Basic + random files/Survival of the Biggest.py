list_of_integer = input().split(" ")
numbers_to_remove = int(input())
new_list = []
sorted_new_list=[]
string=""
for elements in list_of_integer:
    new_list.append(int(elements))
    sorted_new_list.append(int(elements))

sorted_new_list.sort()

for index in range(numbers_to_remove):
    new_list.remove(sorted_new_list[index])

print(*new_list, sep=", ")
