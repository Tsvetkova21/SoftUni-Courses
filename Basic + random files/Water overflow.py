n = int(input())
capacity =255
sum_liters = 0
for i in range (0,n):
    liters=int(input())
    sum_liters +=liters
    if sum_liters>capacity:
        print("Insufficient capacity!")
        sum_liters = sum_liters - liters

print(sum_liters)