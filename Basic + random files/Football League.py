stadium_capacity = int(input())
count_fens = int(input())
sector = " "
count_A = 0
count_B = 0
count_V = 0
count_G = 0
fens = 0

for num in range(0,count_fens):
    sector = input()
    if sector == 'A':
        count_A+=1
    if sector == 'B':
        count_B+=1
    if sector == 'V':
        count_V+=1
    if sector == 'G':
        count_G+=1
    fens+=1

print(f'{(count_A/fens*100):.2f}%')
print(f'{(count_B/fens*100):.2f}%')
print(f'{(count_V/fens*100):.2f}%')
print(f'{(count_G/fens*100):.2f}%')
print(f'{(fens/stadium_capacity*100):.2f}%')