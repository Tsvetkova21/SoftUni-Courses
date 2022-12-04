import re

number = input()
pattern = r'(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))'
result = re.finditer(pattern,number)
for match in result:
    print(match.group(),end=" ")
