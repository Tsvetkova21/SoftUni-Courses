number = int(input())
text=str(number)
m = sorted(text, reverse=False)
for d, digit in enumerate(m):
    print(digit, end="")