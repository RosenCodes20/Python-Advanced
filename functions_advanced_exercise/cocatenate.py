def concatenate(*args, **kwargs):
    final_word = ""
    for word in args:
        final_word += word

    for k, v in kwargs.items():
        final_word = final_word.replace(k, v)
    return final_word


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))