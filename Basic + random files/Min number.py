import sys

inpt=input()
min=sys.maxsize

while inpt!='Stop':
    number=int(inpt)

    if number<min:
        min=number
    inpt=input()

print(min)