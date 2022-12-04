count_groups= int(input())
musala_gr=0
monblan_gr=0
kilimandjaro_gr=0
k2_gr=0
everest_gr=0
sum=0
for num in range (0,count_groups):
    people_in_group= int(input())
    sum+=people_in_group
    if people_in_group<=5:
        musala_gr+=people_in_group
    if 6<=people_in_group<=12:
        monblan_gr+=people_in_group
    if 13<=people_in_group<=25:
        kilimandjaro_gr+=people_in_group
    if 26<=people_in_group<=40:
        k2_gr+=people_in_group
    if people_in_group>=41:
        everest_gr+=people_in_group
print(f'{(musala_gr/sum*100):.2f}%')
print(f'{(monblan_gr/sum*100):.2f}%')
print(f'{(kilimandjaro_gr/sum*100):.2f}%')
print(f'{(k2_gr/sum*100):.2f}%')
print(f'{(everest_gr/sum*100):.2f}%')