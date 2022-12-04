command = input()
company_users = {}

while command != "End":
    company, number = command.split(" -> ")
    if company not in company_users:
        company_users[company]=[]
    if number not in company_users[company]:
        company_users[company].append(number)
    command = input()

for key,value in company_users.items():
    print(f"{key}")
    for value in company_users[key]:
        print(f"-- {value}")