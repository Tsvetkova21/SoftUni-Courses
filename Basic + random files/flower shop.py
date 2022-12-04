import math

count_m = int(input())
count_z = int(input())
count_r = int(input())
count_c = int(input())
price_gift = float(input())

all_price = (count_m*3.25 +count_z*4+\
    count_r*3.5+count_c*8)*0.95

diff =abs(all_price - price_gift)

if all_price>=price_gift:
    print(f"She is left with {math.floor(diff)} leva.")
if all_price<price_gift:
    print(f"She will have to borrow {math.ceil(diff)} leva.")

