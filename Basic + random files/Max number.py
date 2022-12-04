import sys

inpt=input()
max=-sys.maxsize

while inpt!='Stop':
    number=int(inpt)

    if number>max:
        max=number
    inpt=input()

print(max)