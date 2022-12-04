string=input().split(", ")
count_zeros=0
new_string=[]
for elements in string:
    if elements!="0":
        new_string.append(int(elements))
    else:
        count_zeros+=1
for i in range (count_zeros):
    new_string.append(0)
print(new_string)
