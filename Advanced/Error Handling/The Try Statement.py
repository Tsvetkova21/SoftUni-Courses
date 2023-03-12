#try:
#    x = int("Peter")
#except ValueError:
#    print("Cannot convert str to int")
#finally:
#    print("Finally block")

try:
    x = int(input())
except ValueError as error:
    print(error)