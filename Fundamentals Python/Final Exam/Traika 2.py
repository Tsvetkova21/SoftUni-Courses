import re
lines = int(input())
encrypted_message = ''
pattern = r'^(\S{1,})>(\d{3})\|([a-z]{3})\|([A-Z]{3})\|([^<>]{3})<\1$'
for i in range(lines):
    message = input()
    match_mesage = re.findall(pattern,message)
    if len(match_mesage)<1:
        print("Try another password!")
    else:
        for match in match_mesage:
            encrypted_message=match[1]+match[2]+match[3]+match[4]
        print(f"Password: {encrypted_message}")