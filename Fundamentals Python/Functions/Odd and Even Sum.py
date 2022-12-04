def odd_and_even_sum(number):
    sum_odd_digits=0
    sum_even_digits=0
    for digit in number:
        if int(digit)%2==0: #digit is even
            sum_even_digits+=int(digit)
        else: #digit is odd
            sum_odd_digits+=int(digit)
    return sum_even_digits,sum_odd_digits
number_as_string=input()
sum_even_digits, sum_odd_digits =odd_and_even_sum(number_as_string)
print(f"Odd sum = {sum_odd_digits}, Even sum = {sum_even_digits}")