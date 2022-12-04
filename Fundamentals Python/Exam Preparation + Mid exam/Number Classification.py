def positive(numbers):
    return (num for num in numbers if int(num)>=0)
def negative(numbers):
    return (num for num in numbers if int(num) <0)
def even(numbers):
    return (num for num in numbers if int(num)%2 ==0)
def odd(numbers):
    return (num for num in numbers if int(num)%2!=0)
numbers =  input().split(", ")

print(f"Positive: {', '.join(positive(numbers))}")
print(f"Negative: {', '.join(negative(numbers))}")
print(f"Even: {', '.join(even(numbers))}")
print(f"Odd: {', '.join(odd(numbers))}")