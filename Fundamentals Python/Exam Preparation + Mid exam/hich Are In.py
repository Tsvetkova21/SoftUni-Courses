first_list = input().split(', ')
second_list = input().split(', ')
#for first_word in first_list:
#    for second_word in second_list:
#       if first_word in second_word and not first_word in substrings:
#            substrings.append(first_word)

substrings = [first for first in first_list if any (first in second for second in second_list)]

print(substrings)