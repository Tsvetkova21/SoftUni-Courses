first_number = int(input())
second_number = int(input())
first_fact = 1
second_fact = 1
result = 0
for i in range(first_number+1):
    if i!=0:
        first_fact=first_fact*i
for i in range(second_number+1):
    if i!=0:
        second_fact=second_fact*i
result=first_fact/second_fact
print(f'{result:.2f}')
