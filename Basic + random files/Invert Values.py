text = input()

list = text.split(" ")
for elements in list:
    if int(elements)>=0:
        new_elements=-(int(elements))
        list[list.index(elements)]=(new_elements)
    if int(elements)<0:
        new_elements=-(int(elements))
        list[list.index(elements)]=(new_elements)
print(list)