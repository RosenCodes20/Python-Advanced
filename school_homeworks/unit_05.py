import re

found_words_and_nums = r"[a-zA-Z0-9]+"

with open("data.txt", "r") as data_file:
    found = re.findall(found_words_and_nums, data_file.read())

with open("clean_data.txt", "a") as clean_data_file:
    clean_data_file.write("".join(found))
