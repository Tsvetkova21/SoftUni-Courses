def password_validation(input):
    validation = []
    if len(input)<6 or len(input)>10:
       validation.append("Password must be between 6 and 10 characters")

    if not input.isalnum():
        validation.append("Password must consist only of letters and digits")

    digit_counter = 0
    for char in input:
        if char.isdigit():
            digit_counter+=1
    if digit_counter<2:
        validation.append("Password must have at least 2 digits")

    return validation

password = input()
password_is_not_valid=password_validation(password)
if len(password_is_not_valid)==0:
    print("Password is valid")
else:
    print('\n'.join(password_is_not_valid))