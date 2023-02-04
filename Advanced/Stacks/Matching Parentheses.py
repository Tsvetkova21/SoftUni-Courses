text = input()
parenthesis = []

for i in range(len(text)):
    if text[i] == "(":
        parenthesis.append(i)
    elif text[i] == ")":
        start_index = parenthesis.pop()
        print(text[start_index:i+1])