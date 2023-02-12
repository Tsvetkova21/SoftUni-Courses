def words_sorting(*words):
    words_ascii = {}
    sum_ascii = 0
    all_sum = 0
    result = []
    for word in words:
        for ch in word:
            sum_ascii+=ord(ch)
        if word not in words_ascii:
            words_ascii[word]=0
        words_ascii[word]+=sum_ascii
        all_sum+=sum_ascii
        sum_ascii=0
    if all_sum%2!=0:
        sorted_words_info = sorted(words_ascii.items(), key=lambda a: -a[1])
    else:
        sorted_words_info = sorted(words_ascii.items(), key=lambda a: a[0])
    for w in sorted_words_info:
        word, ascii = w[0], w[1]
        result.append(f"{word} - {ascii}")
    return '\n'.join(result)

print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))


print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))

print(
    words_sorting(
        'cacophony',
        'accolade'
  ))
