numbers=[int(x) for x in input().split()]
positives = []
negatives = []
positives_numbers = 0
negatives_numbers = 0

for num in numbers:
    if num<0:
        negatives_numbers  +=num
    else:
        positives_numbers+=num
print(negatives_numbers)
print(positives_numbers)
if abs(negatives_numbers)>abs(positives_numbers):
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
