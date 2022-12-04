def sum_numbers(a,b):
    return a+b
def subtract(sum,c):
    return sum-c


first_number = int(input())
second_number = int(input())
third_number = int(input())
result = sum_numbers(first_number, second_number)
print(subtract(result,third_number))
