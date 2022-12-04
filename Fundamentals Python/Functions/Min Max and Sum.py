numbers_as_string = input().split(" ")
numbers =[]
for digit in numbers_as_string:
        numbers.append(int(digit))
min_numbers = min(numbers)
max_numbers = max(numbers)
sum_numbers = sum(numbers)

print(f"The minimum number is {min_numbers}")
print(f"The maximum number is {max_numbers}")
print(f"The sum number is: {sum_numbers}")