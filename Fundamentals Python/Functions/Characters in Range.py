def collect_characters(first, second):
    character=[]
    for current_character in range(ord(first)+1, ord(second)):
        character.append(chr(current_character))
    return character

first_character = input()
second_character = input()
result= collect_characters(first_character,second_character)
print(' '.join(result))
