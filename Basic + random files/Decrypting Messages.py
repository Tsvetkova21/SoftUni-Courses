key = int(input())
n = int(input())
for i in range(1,n+1):
    letters = input()
    new_letter =chr(key+ord(letters))
    print(new_letter,end="")