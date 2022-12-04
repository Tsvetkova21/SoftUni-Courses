numbers_as_string = input().split(" ")
numbers =[]
for digit in numbers_as_string:
        numbers.append(int(digit))
sorted_numbers=sorted(numbers)
print(sorted_numbers)