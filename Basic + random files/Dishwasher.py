count_detergent = int(input())
dishes = 0
counter_using_washer = 0
left_detergent = 750 * count_detergent
counter_dishes = 0
counter_pots = 0
while left_detergent >=0:
    inpt = input()
    counter_using_washer += 1
    if inpt == 'End':
        break
    dishes = int(inpt)
    if counter_using_washer%3 == 0:
        left_detergent =left_detergent - dishes*15
        counter_pots+=dishes
    else:
        left_detergent = left_detergent - dishes * 5
        counter_dishes+=dishes

if left_detergent<0:
    print (f'Not enough detergent, {abs(left_detergent)} '
            f'ml. more necessary!')
else:
    print("Detergent was enough!")
    print(f"{counter_dishes} dishes and {counter_pots}"
              f" pots were washed.")
    print(f"Leftover detergent {left_detergent} ml.")






