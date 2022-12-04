city=input()
sales=float(input())
commitions=0
if city=='Sofia':
    if sales>=0 and sales<=500:
        commitions=0.05*sales
    elif sales>500 and sales<=1000:
        commitions=0.07*sales
    elif sales > 1000 and sales <= 10000:
        commitions = 0.08 * sales
    elif sales > 10000:
        commitions = 0.12 * sales
    else:
        print("error")
elif city=='Varna':
    if sales>=0 and sales<=500:
        commitions=0.045*sales
    elif sales>500 and sales<=1000:
        commitions=0.075*sales
    elif sales > 1000 and sales <= 10000:
        commitions = 0.1 * sales
    elif sales > 10000:
        commitions = 0.13 * sales
    else:
        print("error")
elif city=='Plovdiv':
    if sales>=0 and sales<=500:
        commitions=0.055*sales
    elif sales>500 and sales<=1000:
        commitions=0.08*sales
    elif sales > 1000 and sales <= 10000:
        commitions = 0.12 * sales
    elif sales > 10000:
        commitions = 0.145 * sales
    else:
        print("error")
else:
    print("error")
if commitions!=0:
    print(f"{commitions:.2f}")
