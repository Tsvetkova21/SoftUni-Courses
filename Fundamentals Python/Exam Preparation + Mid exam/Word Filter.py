words = input().split(" ")
#check if len() is even
filter_words=[num for num in words if len(num)%2==0]
print('\n'.join(filter_words))