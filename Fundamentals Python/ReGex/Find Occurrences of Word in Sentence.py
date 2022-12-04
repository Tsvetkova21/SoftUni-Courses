import re
text = input()
some_word = input()
pattern = fr'\b{some_word}\b'
result = re.findall(pattern, text, flags = re.IGNORECASE)
print(len(result))

