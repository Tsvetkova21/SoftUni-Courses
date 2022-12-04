import sys
n=int(input())
max_number=-sys.maxsize
sum_numbers=0
for i in range (0,n):
    num = int(input())
    if num>max_number:
        max_number = num
    sum_numbers+=num
if (sum_numbers-max_number)==max_number:
    print('Yes')
    print(f'Sum = {sum_numbers-max_number}')
else:
    print('No')
    print(f'Diff = {abs(max_number-(sum_numbers-max_number))}')