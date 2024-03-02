def words_sorting(*args):
    word_sorting_dict = {word: sum(map(ord, word)) for word in args}
    result = []
    if not sum(word_sorting_dict.values()) % 2 == 0:
        for word, value in sorted(word_sorting_dict.items(), key=lambda x: -x[1]):
            result.append(f"{word} - {value}")
    else:
        for word, value in sorted(word_sorting_dict.items(), key=lambda x: x[0]):
            result.append(f"{word} - {value}")

    return "\n".join(result)


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
