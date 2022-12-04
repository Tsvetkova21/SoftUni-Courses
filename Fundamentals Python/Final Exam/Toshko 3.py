import re
messages_list = []
lines = int(input())
pattern = r'^(\$|\%)([A-Z][a-z]{2,})\1: \[(\d+)\]\|\[(\d+)\]\|\[(\d+)\]\|$'
decrypted_message = ''

for i in range(lines):
    message = input()
    match_message = re.findall(pattern,message)
    if len(match_message)<1:
        print("Valid message not found!")
    else:
        for single_message in match_message:

            decrypted_message = chr(int(single_message[2])) + chr(int(single_message[3])) + chr(int(single_message[4]))
        print(f"{single_message[1]}: {decrypted_message}")