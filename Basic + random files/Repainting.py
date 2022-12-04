neobhodim_nailon=int(input())
neobhodimo_kolichestvo_boq=int(input())
kolichestvo_razreditel=int(input())
chasove_maistori=int(input())
razhodi_materiali=(neobhodim_nailon+2)*1.5+neobhodimo_kolichestvo_boq*1.1*14.5+kolichestvo_razreditel*5+0.4
vsichki_razhodi=razhodi_materiali+razhodi_materiali*chasove_maistori*0.3*1
print(vsichki_razhodi)