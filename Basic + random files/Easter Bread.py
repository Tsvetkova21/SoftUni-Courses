budget = float(input())
price_1kg_flour = float(input())
count_colored_eggs = 0

price_eggs = 0.75*price_1kg_flour
price_milk=0.25*1.25*price_1kg_flour
price_1_loaf = price_eggs+price_milk+price_1kg_flour

number_of_loaves=budget//price_1_loaf
budget=budget - number_of_loaves*price_1_loaf

for i in range (1, int(number_of_loaves+1),1):
    count_colored_eggs+=3
    if i%3==0:
        count_colored_eggs=count_colored_eggs - (i-2)
print(f"You made {number_of_loaves:.0f} loaves of Easter bread! "
      f"Now you have {count_colored_eggs:.0f} eggs and {budget:.2f}BGN left.")