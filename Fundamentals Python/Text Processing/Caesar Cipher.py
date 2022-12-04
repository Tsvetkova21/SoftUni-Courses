message = input()
final_message =''
for character in message:
    character=chr(ord(character)+3)
    final_message+=character
print(final_message)