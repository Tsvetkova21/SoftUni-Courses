numbers = [string.split() for string in input().split("|")]
print(*' '.join(string) for string in numbers[::-1] if string)