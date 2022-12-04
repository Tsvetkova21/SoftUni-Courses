list = []
n = int(input())
a = int(input())
b = int(input())
value = a + b
list.append(a+b)
statement = False
for i in range(0,n-1):
    list.append(int(input()) + int(input()))
if list.count(value) == n:
    statement = True
if statement:
    print("Yes, value={0}".format(value))
else:
    maxDiff = abs(list[0] - list[1])
    for i in range(0,n):
        maxDiff = max(maxDiff,abs(list[i-1] - list[i]))
    print("No, maxdiff={0}".format(maxDiff))