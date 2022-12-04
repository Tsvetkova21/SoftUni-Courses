numbers_string = input().split(" ")
numbers=[]
for elements in numbers_string:
    numbers.append(round(float(elements)))
print(numbers)