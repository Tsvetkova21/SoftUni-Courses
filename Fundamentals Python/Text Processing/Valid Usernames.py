def lenght_is_valid(name):
    if 3<= len(name) <=16:
        return True
    return False


def characters_are_valid(name):
    for character in name:
        if not (character.isalnum() or character =="_" or character=="-"):
            return False
    return True

def no_redundant_symbols_(name):
    if ' ' in name:
        return False
    return True

def username_validation(name):
    if lenght_is_valid(name) and characters_are_valid(name) and no_redundant_symbols_(name):
        return True
    return False


username = input().split(", ")
for item in username:
    if username_validation(item):
        print(item)
