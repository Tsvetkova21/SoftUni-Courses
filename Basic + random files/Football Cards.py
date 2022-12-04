text = input()
players = text.split(" ")
numbers_A=[]
numbers_B=[]
players_A=11
players_B=11
Terminate= False
for elements in players:
    numbers_A.append(elements.strip("A-"))
    if "B" in elements:
        numbers_A.remove(elements)
numbers_A = ([int(x) for x in numbers_A])
set_numbers_A = set(numbers_A)
numbers_A=list(set_numbers_A)
for elements in players:
    numbers_B.append(elements.strip("B-"))
    if "A" in elements:
        numbers_B.remove(elements)
numbers_B = ([int(x) for x in numbers_B])
set_numbers_B = set(numbers_B)
numbers_B=list(set_numbers_B)
for i in range(1,11+1):
    players_A -= int(numbers_A.count(i))
    players_B -= int(numbers_B.count(i))
    if players_A < 7 or players_B < 7:
        print(f'Team A - {players_A}; Team B - {players_B}')
        print('Game was terminated')
        Terminate = True
        break

if Terminate!=True:
    print(f'Team A - {players_A}; Team B - {players_B}')


