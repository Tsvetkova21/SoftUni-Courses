from operator import not_
number=int(input())
valid=number>=100 and number<=200 or number==0

if not valid:
    print('invalid')