n = int(input())
list =[]
new_list =[]
for i in range(1, n+1):
    list.append(int(input()))
command = input()
if command == 'even':
    for numbers in list:
        if numbers%2 == 0:
            new_list.append(numbers)

if command == 'odd':
    for numbers in list:
        if numbers%2 != 0:
            new_list.append(numbers)

if command == 'negative':
    for numbers in list:
        if numbers < 0:
            new_list.append(numbers)

if command == 'positive':
    for numbers in list:
        if numbers>= 0:
            new_list.append(numbers)

print(new_list)
