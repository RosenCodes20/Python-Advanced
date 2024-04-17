import re

found_words = r"[A-Za-z]+"
with open("data.txt", "r") as data_file:
    found_words = re.findall(found_words, data_file.read())

print(len(found_words))