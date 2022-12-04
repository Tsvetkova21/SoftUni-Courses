n = int(input())
list = []
first_text= input()
new_list = []
for i in range(1,n+1):
    text=input()
    list.append(text)
    if first_text in text:
        new_list.append(text)
print(list)
print(new_list)
