n = int(input())
is_balanced = True
last_bracket = ''

for i in range (0,n):
    current = input()
    if current not in ['(',')']:
        continue
    if last_bracket == '' and current == ')' or last_bracket == current:
        is_balanced = False
        break
    last_bracket = current

if is_balanced:
    print('BALANCED')
else:
    print('UNBALANCED')