import re
text = input()
coolnes =1
cool_emojies = []
sum_letters=0
pattern = r'(\:{2}|\*{2})([A-Z][a-z]{2,})\1'
number = r'\d'
match_numbers=re.findall(number, text)
for match in match_numbers:
    coolnes*=int(match)
match_emojies = re.findall(pattern,text)
for emojies in match_emojies:
    for ch in emojies[1]:
        sum_letters +=ord(ch)
    if sum_letters>coolnes:
        cool_emojies.append(emojies[0]+emojies[1]+emojies[0])
    sum_letters=0

print(f"Cool threshold: {coolnes}")
print(f"{len(match_emojies)} emojis found in the text. The cool ones are:")
print("\n".join(cool_emojies))