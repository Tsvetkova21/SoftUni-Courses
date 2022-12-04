divisor = int(input())
boundary = int(input())

for i in range(divisor,boundary+1,1):
    if i%divisor==0:
        max = i
    i+=i
print(max)