import re
text = input()
pattern = r'\b(([a-z0-9]+[a-z0-9\.\-\_]*)@[a-z\-]+(\.[a-z]+)+)\b'

emails = re.findall(pattern,text)
for email in emails:
    print(''.join(email[0]))