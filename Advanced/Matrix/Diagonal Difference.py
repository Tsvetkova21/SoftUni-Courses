n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]

primary, secondary = 0,0

for i in range(n):
    primary +=matrix[i][i]
    secondary+=matrix[n-i-1][i]

print(abs(primary - secondary))