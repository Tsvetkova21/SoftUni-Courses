import re
text = input()
pattern = r'(=|\/)[A-Z][A-Za-z]{2,}\1'
result = re.finditer(pattern,text)
points = 0
all_destinations = []
for dest in result:
    current_destination = re.split("\/|=", dest.group())[1]
    points+=len(current_destination)
    all_destinations.append(current_destination)

print(f"Destinations: {', '.join(all_destinations)}")
print(f"Travel Points: {points}")