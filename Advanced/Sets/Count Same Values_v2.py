numbers = tuple(map(float, input().split(" ")))
nums_and_occurances = {}
for items in numbers:
    nums_and_occurances[items]=numbers.count(items)
[print(f"{key} - {value} times") for key, value in nums_and_occurances.items()]