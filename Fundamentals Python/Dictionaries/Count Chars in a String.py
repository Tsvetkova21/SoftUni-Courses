words = input()
dictionary={}
for char in words:
    if char!=" ":
        if char not in dictionary:
            dictionary[char] = 0
        dictionary[char]+=1
for (key, value) in dictionary.items():
    print(f"{key} -> {value}")