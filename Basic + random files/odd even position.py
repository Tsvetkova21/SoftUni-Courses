import sys

number = int(input())
odd_max=-sys.maxsize
odd_min=sys.maxsize
odd_sum = 0
even_max=-sys.maxsize
even_min=sys.maxsize
even_sum = 0
odd_number = 0
even_number = 0

for i in range (1, number+1):
    if i%2==0:
        even_number = float(input())
        even_sum += even_number
        if even_max <= even_number:
            even_max = even_number
        if even_min >= even_number:
            even_min = even_number
    elif i%2!=0:
        odd_number = float(input())
        odd_sum += odd_number
        if odd_max <= odd_number:
            odd_max = odd_number
        if odd_min >= odd_number:
            odd_min = odd_number
print(f'OddSum={odd_sum:.2f},')
if odd_min!= sys.maxsize:
    print(f'OddMin={odd_min:.2f},')
else:
    print(f'OddMin=No,')
if odd_max!= -sys.maxsize:
    print(f'OddMax={odd_max:.2f},')
else:
    print(f'OddMax=No,')
print(f'EvenSum={even_sum:.2f},')
if even_min!= sys.maxsize:
    print(f'EvenMin={even_min:.2f},')
else:
    print(f'EvenMin=No,')
if even_max!= -sys.maxsize:
    print(f'EvenMax={even_max:.2f}')
else:
    print(f'EvenMax=No')