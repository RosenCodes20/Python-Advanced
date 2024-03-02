punctuation_marks = {"-", ",", ".", "!", "?"}

with open("text.txt", "r") as text_file:

    file = text_file.readlines()

for rows in range(0, len(file), 2):

    for symbol in punctuation_marks:
        if symbol in file[rows]:
            file[rows] = file[rows].replace(symbol, "@")

    print(*file[rows].split()[::-1])