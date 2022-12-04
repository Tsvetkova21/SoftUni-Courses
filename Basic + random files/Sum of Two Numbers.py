start_integral = int(input())
end_integral = int(input())
magic_numer = int(input())
sum_pairs = 0
counter = 0
condition = False
for i in range (start_integral, end_integral +1):
    for j in range (start_integral, end_integral+1):
        sum_pairs = i + j
        counter += 1
        if sum_pairs == magic_numer:
            print(f"Combination N:{counter} ({i} " \
                    f"+ {j} = {magic_numer})")
            condition = True
            quit()
if not condition:
    print(f"{counter} combinations -"
      f" neither equals {magic_numer}")

