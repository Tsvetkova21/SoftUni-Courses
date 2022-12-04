tabs_browser = int(input())
salary = int(input())

for num in range(0,tabs_browser):
    browser = input()
    if browser == 'Facebook':
        salary-=150
    elif browser == 'Instagram':
        salary-=100
    elif browser == 'Reddit':
        salary-=50
    if salary<=0:
        print("You have lost your salary." )
        exit()
print(f'{(salary)}')
