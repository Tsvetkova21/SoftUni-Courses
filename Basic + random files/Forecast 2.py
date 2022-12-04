Degrees=float(input())
if Degrees>=26.00 and Degrees<=35.00:
    print("Hot")
elif Degrees>=20.1 and Degrees<=25.9:
    print("Warm")
elif Degrees>=15.00 and Degrees<=20.00:
    print("Mild")
elif Degrees>=12.00 and Degrees<=14.9:
   print("Cool")
elif Degrees>=5 and Degrees<=11.9:
   print("Cold")
else:
    print("unknown")