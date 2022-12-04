number = int(input())
sum_positive_divisors = 0
for i in range (number+1):
    if i!=0:
        if number%i ==0:
            sum_positive_divisors+=i
if sum_positive_divisors/2==number:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")