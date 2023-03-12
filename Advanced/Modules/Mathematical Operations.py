from math_module import mathematical_operator
try:
    data=mathematical_operator(*input('Please enter: first number, operator, second number:').split(' '))
    print(f"Result is: {data:.2f}")
except ValueError:
    print("Enter a valid data!")