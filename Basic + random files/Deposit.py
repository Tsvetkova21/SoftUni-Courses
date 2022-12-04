depozirana_suma=float(input())
srok_deposit=int(input())
lihven_prozent=float(input())
suma=depozirana_suma+srok_deposit*(depozirana_suma*lihven_prozent)/12/100
print(suma)