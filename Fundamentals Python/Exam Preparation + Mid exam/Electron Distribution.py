
electrons = int(input())
i =1
shells = []
while electrons>0:
        if electrons >=0 and electrons>2*pow(i,2):
            shells.append(2*pow(i,2))
        if electrons - 2*pow(i,2)<0 and electrons>0:
            shells.append(electrons)
        electrons-=2*pow(i,2)
        i=i+1
print(shells)