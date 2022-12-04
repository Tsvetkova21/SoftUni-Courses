strings = input().split(" ")
result = ""
for word in strings:
    lenght = len(word)
    result += word*(lenght)
print(result)