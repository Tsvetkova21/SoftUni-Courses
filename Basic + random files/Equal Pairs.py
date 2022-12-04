number = int(input())
first_sum = int(input()) + int(input())
diff= 0

for i in range(number - 1):
    secont_sum = int(input()) + int(input())
    if abs(first_sum - secont_sum) > diff:
        diff = abs(secont_sum - first_sum)
    first_sum= secont_sum

if diff == 0:
    print(f"Yes, value={first_sum}")
else:
    print(f"No, maxdiff={diff}")

