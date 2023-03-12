def concatenate(*args, **kwargs):
    concatenated_word=''
    for words in args:
        concatenated_word +=words
        new_word = concatenated_word
    for key in kwargs:
        if key in concatenated_word:
            new_word = new_word.replace(key, kwargs[key])
    return new_word

print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))