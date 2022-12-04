message = input()
final_text = ""
last_letter = ""
for current_leter in message:
    if current_leter !=last_letter:
        final_text+=current_leter
        last_letter=current_leter
print(final_text)