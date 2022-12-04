period = int(input())
examined_patiants = 0
not_examined_patiants = 0
doctors = 7

for num in range(1, period+1):

    patiants = int(input())
    if num % 3 == 0:
        if not_examined_patiants > examined_patiants:
            doctors += 1
    if patiants >= doctors:
        examined_patiants+=doctors
    else:
        examined_patiants += patiants

    diff = patiants - doctors
    if diff>0:
        not_examined_patiants  += diff

print(f'Treated patients: {examined_patiants}.')
print(f'Untreated patients: {not_examined_patiants}.')




