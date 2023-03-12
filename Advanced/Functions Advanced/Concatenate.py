def concatenate(*args, **kwargs):
    concatenated_word=''
    for words in args:
        concatenated_word +=words
    for key, value in kwargs.items():
        if key in concatenated_word:
            print(concatenated_word)
            if kwargs[key]!='':
                start_index_word = concatenated_word.index(key)
                end_index_word = concatenated_word.index(key)+len(kwargs[key])
                concatenated_word = concatenated_word[:start_index_word] + kwargs[key] + concatenated_word[
                                                                                         end_index_word::]
            else:
                start_index_word = concatenated_word.index(key)
                end_index_word = concatenated_word.index(key)
                concatenated_word = concatenated_word[:start_index_word] + concatenated_word[
                                                                                         end_index_word::]
            print(start_index_word, end_index_word)
            print(kwargs[key])
    return concatenated_word

print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))