numbers = input().split(" ")
sum = 0
string=input()
new_string=[]
str=''
for elements in numbers:
   for char in elements:
       sum+=int(char)
   for letters in string:
       if sum>len(string):
           sum-=len(string)
   new_string.append(string[sum])
   string = string.replace(string[sum],'',1)
   sum=0
for element in new_string:
    str+=element

print(str)