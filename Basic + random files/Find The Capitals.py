text = input()
upper_list = []

for char in range(len(text)):
    if text[char].isupper()==True :
        upper_list.append(char)
print(upper_list)