numbers_as_string = input().split(", ")
numbers =[]
reversed_numbers=[]
for digit in numbers_as_string:
        numbers.append(int(digit))
        reversed_numbers.append(int(digit[::-1]))
for i in range(len(numbers)):
        if numbers[i]==reversed_numbers[i]:
                print("True")
        else:
                print("False")
