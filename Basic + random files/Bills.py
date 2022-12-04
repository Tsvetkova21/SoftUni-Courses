months = int(input())
electr_bill_month = 0
electr_bill= 0
water_bill  = 0
internet_bill= 0
other_bill = 0

for nunm in range(0, months):
    electr_bill_month = float(input())
    electr_bill += electr_bill_month
    water_bill += 20
    internet_bill +=15
    other_bill+=(electr_bill_month+20+15)*1.2
all_bills = (electr_bill+other_bill+internet_bill+water_bill)/months
print(f'Electricity: {electr_bill:.2f} lv')
print(f'Water: {water_bill:.2f} lv')
print(f'Internet: {internet_bill:.2f} lv')
print(f'Other: {other_bill:.2f} lv')
print(f'Average: {all_bills:.2f} lv')