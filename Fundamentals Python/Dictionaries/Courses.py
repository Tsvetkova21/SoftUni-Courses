command = input()
data = {}
counter = 0
while command != "end":
    course, student = command.split(" : ")
    if course not in data:
        data[course]=[]
    data[course].append(student)
    command=input()

for key,value in data.items():
    counter = len(value)
    print(f"{key}: {len(data[key])}")
    for value in data[key]:
        print(f"-- {value}")

