numbers_as_string = input().split(" ")
numbers =[]
for digit in numbers_as_string:
        numbers.append(int(digit))

def even(x): return x % 2 == 0

even_numbers = list(filter(even, numbers))
print(even_numbers)

