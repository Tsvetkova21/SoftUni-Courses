input_operator = input()
first_number = int(input())
second_number = int(input())
def calculation(first_number, second_number, input_operator):
    if input_operator=="multiply":
        return first_number*second_number
    elif input_operator=="divide":
        return int(first_number/second_number)
    elif input_operator=="add":
        return first_number+second_number
    elif input_operator=='subtract':
        return first_number-second_number

print(calculation(first_number,second_number, input_operator))
