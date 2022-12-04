n = int(input())
list_positive = []
list_negative = []
count_positive = 0
sum_negative = 0
for i in range(1,n+1):
    number = int(input())
    if number>=0:
        list_positive.append(number)
        count_positive+=1
    if number<0:
        list_negative.append(number)
        sum_negative+=number
print(list_positive)
print(list_negative)
print(f'Count of positives: {count_positive}')
print(f'Sum of negatives: {sum_negative}')