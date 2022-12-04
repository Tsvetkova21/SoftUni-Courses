count_paper = int(input())
count_fabric_roll = int(input())
glue_liters = float(input())
discount = int(input())

all_money = (count_paper*5.8 + count_fabric_roll*7.2+\
             glue_liters*1.2)*(1-discount/100)
print(f'{all_money:.3f}')


