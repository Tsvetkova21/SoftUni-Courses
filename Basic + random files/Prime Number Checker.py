num= int(input())
condition = True
if num >1:
    for i in range(2,num):
        if num%i == 0:
            condition = False
            break
print(condition)