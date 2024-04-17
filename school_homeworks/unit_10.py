import re

found_words = r"[A-Za-z]+"

words_startswith_the_same_letter = []
with open("input.txt", "r") as input_file:
    words = re.findall(found_words, input_file.read())

    for word in words:
        if word[0].lower() == "a":
            words_startswith_the_same_letter.append(word)

with open("output.txt", "a") as output_file:
    output_file.write("\n".join(words_startswith_the_same_letter))
